#!/usr/bin/env python3
"""Original silent 2D motion study; no API, voice generation or input image editing."""
import argparse,math,os,pathlib
import numpy as np
from PIL import Image,ImageDraw,ImageFont
import imageio_ffmpeg

def font(size,bold=False):
    names=['DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf']
    if os.name=='nt':names.insert(0,str(pathlib.Path(os.environ.get('WINDIR','C:/Windows'))/'Fonts'/('segoeuib.ttf' if bold else 'segoeui.ttf')))
    for name in names:
        try:return ImageFont.truetype(name,size)
        except OSError:pass
    return ImageFont.load_default(size=size)

def draw_frame(t):
    w,h=1280,720;im=Image.new('RGB',(w,h),'#f5f2e7');d=ImageDraw.Draw(im)
    green='#173e2a';gold='#f2c64f';muted='#65715f';ink='#173e2a'
    d.text((64,40),'CampusCart',font=font(30,True),fill=green)
    d.text((920,48),'SILENT MOTION STUDY',font=font(17,True),fill=muted)
    stage=min(2,int(t//4));head=['Find the camera.','Agree the handoff.','Bring it back.'][stage]
    d.text((64,108),head,font=font(52,True),fill=ink)
    for x,label in [(280,'OWNER'),(1000,'BORROWER')]:
        d.ellipse((x-48,265,x+48,361),fill='#c9dfbc',outline=green,width=4)
        d.arc((x-20,292,x+20,323),0,180,fill=green,width=3)
        d.rounded_rectangle((x-72,368,x+72,478),radius=18,fill=green)
        d.text((x-54,497),label,font=font(19,True),fill=green)
    if stage==0:
        x=390;y=315
        radius=82+7*math.sin(t*4)
        d.ellipse((x-radius,y-radius,x+radius,y+radius),outline=gold,width=7)
    else:
        p=min(1,max(0,(t-stage*4)/3));ease=p*p*(3-2*p)
        x=390+(500*ease if stage==1 else 500*(1-ease));y=315-30*math.sin(math.pi*p)
        d.line((400,390,880,390),fill='#b8c7ae',width=3)
    d.rounded_rectangle((x-61,y-39,x+61,y+39),radius=12,fill=gold,outline=green,width=4)
    d.rectangle((x-28,y-55,x+6,y-36),fill=gold,outline=green,width=3)
    d.ellipse((x-24,y-25,x+24,y+23),fill='#d6e7ef',outline=green,width=4)
    labels=['1  FIND','2  BORROW','3  RETURN']
    for i,label in enumerate(labels):
        bx=64+i*382;active=i==stage
        d.rounded_rectangle((bx,588,bx+348,647),radius=10,fill=green if active else '#e2e9db')
        d.text((bx+22,604),label,font=font(22,True),fill='#fff8df' if active else green)
    d.text((64,673),'FICTIONAL CONCEPT • No narration included',font=font(16),fill=muted)
    return im

def render(output_dir):
    out=pathlib.Path(output_dir);out.mkdir(parents=True,exist_ok=True)
    targets=[out/'motion-study.mp4',out/'motion-study.gif',out/'motion-study-frame.png']
    if any(p.exists() for p in targets):raise ValueError('Refusing to overwrite existing motion-study outputs; choose an empty output directory.')
    writer=imageio_ffmpeg.write_frames(str(targets[0]),(1280,720),fps=30,codec='libx264',quality=7,pix_fmt_out='yuv420p')
    writer.send(None);gif=[]
    try:
        for i in range(360):
            frame=draw_frame(i/30);writer.send(np.asarray(frame))
            if i%3==0:gif.append(frame.resize((640,360)).convert('P',palette=Image.Palette.ADAPTIVE,colors=128))
            if i==165:frame.save(targets[2])
    finally:writer.close()
    gif[0].save(targets[1],save_all=True,append_images=gif[1:],duration=100,loop=0,optimize=False)
    print(f'Wrote original 12-second silent MP4, GIF preview and frame to {out}')

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output-dir',required=True);a=p.parse_args()
    try:render(a.output_dir)
    except (ValueError,OSError) as exc:p.exit(1,str(exc)+'\n')
