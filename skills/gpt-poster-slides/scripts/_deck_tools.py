"""Local-only image-deck validation; no generators or external services."""
from __future__ import annotations
import json,re,pathlib
from PIL import Image

IMAGE_SUFFIXES={'.png','.jpg','.jpeg','.webp'}

def natural_key(path):
    return [int(s) if s.isdigit() else s.lower() for s in re.split(r'(\d+)',path.name)]

def images_in(folder):
    folder=pathlib.Path(folder)
    if not folder.is_dir(): raise ValueError(f'Image directory not found: {folder}')
    files=sorted([p for p in folder.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_SUFFIXES],key=natural_key)
    if not files: raise ValueError(f'No supported slide images in {folder}')
    return files

def inspect_image(path,min_width=1280,min_height=720):
    path=pathlib.Path(path)
    if not path.is_file(): raise ValueError(f'Missing image: {path}')
    try:
        with Image.open(path) as im:
            im.load();w,h=im.size
    except Exception as exc: raise ValueError(f'Cannot decode image {path}: {exc}') from exc
    if w<min_width or h<min_height: raise ValueError(f'Image is too small: {path.name} {w}x{h}; minimum {min_width}x{min_height}')
    # One pixel in the height direction permits integer rounding from native tools.
    residual=abs(w*9-h*16)
    if residual>16: raise ValueError(f'Image is not 16:9 within one-pixel rounding: {path.name} {w}x{h}')
    return {'path':str(path),'width':w,'height':h,'aspect_ratio':w/h,'exact_16_9':residual==0,'native_rounding_pixels':abs(h-w*9/16)}

def load_manifest(path,allow_unreviewed=False):
    path=pathlib.Path(path).resolve();root=path.parent
    with path.open(encoding='utf-8') as f: data=json.load(f)
    if not isinstance(data,dict) or data.get('schema_version')!=1: raise ValueError('Manifest needs schema_version 1')
    if not isinstance(data.get('title'),str) or not data['title'].strip(): raise ValueError('Manifest needs a non-empty title')
    if data.get('aspect_ratio')!='16:9': raise ValueError('Manifest aspect_ratio must be 16:9')
    color=data.get('canvas_color','#FFFFFF')
    if not isinstance(color,str) or not re.fullmatch(r'#[0-9a-fA-F]{6}',color): raise ValueError('canvas_color must be a six-digit hex color')
    slides=data.get('slides')
    if not isinstance(slides,list) or not slides: raise ValueError('Manifest needs a non-empty slides list')
    ids=set();image_paths=set();validated=[]
    for i,slide in enumerate(slides,1):
        if not isinstance(slide,dict): raise ValueError(f'Slide {i} must be an object')
        sid=slide.get('id');relative=slide.get('image')
        if not isinstance(sid,str) or not sid.strip() or sid in ids: raise ValueError(f'Slide {i} needs a unique non-empty id')
        if not isinstance(relative,str) or not relative.strip() or pathlib.Path(relative).is_absolute(): raise ValueError(f'Slide {sid} needs a relative image path')
        image_path=(root/relative).resolve()
        if not image_path.is_relative_to(root): raise ValueError(f'Slide {sid} image escapes manifest directory')
        if image_path in image_paths: raise ValueError(f'Duplicate image: {relative}')
        if type(slide.get('reviewed')) is not bool: raise ValueError(f'Slide {sid} needs Boolean reviewed')
        if not slide['reviewed'] and not allow_unreviewed: raise ValueError(f'Slide {sid} has not been reviewed; use --allow-unreviewed only for a draft')
        if 'expected_text' not in slide: raise ValueError(f'Slide {sid} needs expected_text; use an empty list only for an intentionally text-free poster')
        copy=slide['expected_text']
        if not isinstance(copy,list) or any(not isinstance(s,str) for s in copy): raise ValueError(f'Slide {sid} expected_text must be a string list')
        ids.add(sid);image_paths.add(image_path)
        validated.append({**slide,'resolved_image':image_path,'image_check':inspect_image(image_path)})
    return data,validated

def contain(w,h,canvas_w,canvas_h):
    scale=min(canvas_w/w,canvas_h/h);pw=w*scale;ph=h*scale
    return ((canvas_w-pw)/2,(canvas_h-ph)/2,pw,ph)

def ensure_outputs(paths,overwrite=False):
    collisions=[str(p) for p in paths if p.exists()]
    if collisions and not overwrite: raise ValueError('Outputs already exist; pass --overwrite intentionally: '+', '.join(collisions))
