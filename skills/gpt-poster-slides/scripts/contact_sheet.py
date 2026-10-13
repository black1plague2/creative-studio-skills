#!/usr/bin/env python3
import argparse,pathlib
from PIL import Image,ImageDraw,ImageOps
from _deck_tools import images_in,inspect_image,ensure_outputs

def make_sheet(directory,output,columns=3,overwrite=False):
    if columns<1: raise ValueError('columns must be positive')
    files=images_in(directory)
    for f in files:inspect_image(f)
    output=pathlib.Path(output);ensure_outputs([output],overwrite)
    width=480;height=270;label=30
    sheet=Image.new('RGB',(columns*width,((len(files)+columns-1)//columns)*(height+label)),'#dedede')
    draw=ImageDraw.Draw(sheet)
    for i,f in enumerate(files):
        x=i%columns*width;y=i//columns*(height+label)
        with Image.open(f) as im: thumb=ImageOps.contain(im.convert('RGB'),(width,height))
        sheet.paste(thumb,(x+(width-thumb.width)//2,y+label+(height-thumb.height)//2))
        draw.text((x+8,y+8),f'{i+1:02} {f.name}',fill='#111111')
    output.parent.mkdir(parents=True,exist_ok=True);sheet.save(output)
    return len(files)

def main():
    p=argparse.ArgumentParser(description='Create a separate QA contact sheet from numbered slide images.')
    p.add_argument('directory');p.add_argument('--output',required=True);p.add_argument('--columns',type=int,default=3);p.add_argument('--overwrite',action='store_true');a=p.parse_args()
    try: count=make_sheet(a.directory,a.output,a.columns,a.overwrite)
    except (ValueError,OSError) as exc:p.exit(1,str(exc)+'\n')
    print(f'Wrote contact sheet for {count} images: {a.output}')

if __name__=='__main__':main()
