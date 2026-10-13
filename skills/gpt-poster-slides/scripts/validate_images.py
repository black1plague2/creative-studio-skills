#!/usr/bin/env python3
import argparse,json,sys
from _deck_tools import images_in,inspect_image

def main():
    p=argparse.ArgumentParser(description='Validate local 16:9 slide images, allowing at most one-pixel native rounding.')
    p.add_argument('directory');p.add_argument('--min-width',type=int,default=1280);p.add_argument('--min-height',type=int,default=720)
    args=p.parse_args()
    try:
        rows=[inspect_image(f,args.min_width,args.min_height) for f in images_in(args.directory)]
    except (ValueError,OSError) as exc: p.exit(1,str(exc)+'\n')
    print(json.dumps({'status':'pass','count':len(rows),'images':rows,'scope':'Dimensions/loadability only; visual/text review is separate.'},indent=2))

if __name__=='__main__':main()
