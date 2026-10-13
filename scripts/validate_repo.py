#!/usr/bin/env python3
"""Validate skill metadata and local Markdown/HTML asset references."""
from __future__ import annotations
import csv,json,pathlib,re,sys,urllib.parse
import yaml

ROOT=pathlib.Path(__file__).resolve().parents[1]

def validate(root=ROOT):
    root=pathlib.Path(root).resolve();errors=[];skills=[]
    for file in sorted((root/'skills').glob('*/SKILL.md')):
        text=file.read_text(encoding='utf-8');match=re.match(r'^---\r?\n(.*?)\r?\n---(?:\r?\n|$)',text,re.S)
        if not match:errors.append(f'{file.relative_to(root)}: missing frontmatter');continue
        try:meta=yaml.safe_load(match.group(1))
        except yaml.YAMLError as exc:errors.append(f'{file.relative_to(root)}: invalid YAML {exc}');continue
        if not isinstance(meta,dict):errors.append(f'{file.relative_to(root)}: metadata is not an object');continue
        name=meta.get('name');description=meta.get('description')
        if not isinstance(name,str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',name) or len(name)>64 or name!=file.parent.name:errors.append(f'{file.relative_to(root)}: invalid/mismatched name')
        if not isinstance(description,str) or not 1<=len(description.strip())<=1024:errors.append(f'{file.relative_to(root)}: invalid description')
        if len(text.splitlines())>500:errors.append(f'{file.relative_to(root)}: entry point exceeds 500 lines')
        if '[TODO:' in text:errors.append(f'{file.relative_to(root)}: unfinished scaffold')
        for reference in ['production.md','intake.md','quality.md','example.md']:
            if not (file.parent/'references'/reference).is_file():errors.append(f'{file.relative_to(root)}: missing {reference}')
        skills.append(name)
    if len(set(skills))!=len(skills):errors.append('Duplicate skill names')
    index=json.loads((root/'skills-index.json').read_text(encoding='utf-8'))
    if set(skills)!={s['name'] for s in index}:errors.append('Skill index does not match actual folders')
    for name in skills:
        if not (root/'skills'/name/'assets'/'production-template.md').is_file():errors.append(f'{name}: missing reusable production template')
    domain_index=json.loads((root/'domains'/'index.json').read_text(encoding='utf-8'))
    domains=domain_index.get('domains',[])
    if not domains or len({d['slug'] for d in domains})!=len(domains):errors.append('Domain index missing/duplicate entries')
    for d in domains:
        p=(root/'domains'/d['brief_path']).resolve()
        if not p.is_relative_to(root/'domains') or not p.is_file():errors.append(f"Domain {d['slug']}: missing/escaping brief")
    if set(domain_index.get('skills',[]))!=set(skills):errors.append('Domain/skill composition index mismatch')
    if domain_index.get('composition_count')!=len(domains)*len(skills):errors.append('Domain composition count mismatch')
    registry=list(csv.DictReader((root/'research'/'sources.csv').open(encoding='utf-8-sig',newline='')))
    coverage=json.loads((root/'research'/'source-coverage.json').read_text(encoding='utf-8')).get('coverage',[])
    if {r['repository'] for r in registry}!={r['repository'] for r in coverage} or len(coverage)!=len(registry):errors.append('Research source/coverage mapping mismatch')
    for row in coverage:
        for target in row.get('integration_files',[]):
            p=(root/target).resolve()
            if not p.is_relative_to(root) or not p.is_file():errors.append(f"{row['repository']}: missing/escaping mapped file {target}")
    for file in list(root.rglob('*.md'))+list(root.rglob('*.html')):
        if any(part in {'.git','work','node_modules'} for part in file.relative_to(root).parts):continue
        text=file.read_text(encoding='utf-8')
        links=re.findall(r'!?\[[^\]]*\]\(([^\s)]+)(?:\s+"[^\"]*")?\)',text)
        if file.suffix=='.html':links+=re.findall(r'(?:src|href)=["\']([^"\']+)["\']',text)
        for link in links:
            if link.startswith(('http:','https:','mailto:','data:','#')):continue
            target=urllib.parse.unquote(link.split('#',1)[0].split('?',1)[0])
            if not target:continue
            path=(file.parent/target).resolve()
            if not path.is_relative_to(root):errors.append(f'{file.relative_to(root)}: local link escapes repo: {link}')
            elif not path.exists():errors.append(f'{file.relative_to(root)}: missing local target: {link}')
    for file in root.rglob('*'):
        if not file.is_file() or '.git' in file.relative_to(root).parts:continue
        if file.resolve()==pathlib.Path(__file__).resolve():continue
        if file.suffix.lower() in {'.md','.json','.py','.html','.css','.txt','.csv','.yml','.yaml'}:
            text=file.read_text(encoding='utf-8-sig',errors='replace')
            if re.search(r'C:\\Users\\|C:/Users/|\.codex[/\\]generated_images|gho_[A-Za-z0-9]{20,}',text):errors.append(f'{file.relative_to(root)}: private host path or credential-like value')
    return {'status':'pass' if not errors else 'fail','skills':len(skills),'domains':len(domains),'domain_skill_compositions':len(domains)*len(skills),'research_sources_mapped':len(coverage),'errors':errors,'scope':'Metadata, coverage, local links and selected publication hygiene; not universal AI behavior.'}

if __name__=='__main__':
    result=validate();print(json.dumps(result,indent=2));sys.exit(0 if result['status']=='pass' else 1)
