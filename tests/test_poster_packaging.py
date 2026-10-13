import importlib.util,json,pathlib,sys,tempfile,unittest,zipfile,xml.etree.ElementTree as ET
from PIL import Image
from pypdf import PdfReader

ROOT=pathlib.Path(__file__).resolve().parents[1]
HELPERS=ROOT/'skills'/'gpt-poster-slides'/'scripts'
sys.path.insert(0,str(HELPERS))
from _deck_tools import inspect_image,load_manifest
from package_slides import package

class PosterPackagingTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=pathlib.Path(self.temp.name)
        Image.new('RGB',(1600,900),'#114433').save(self.root/'a.png')
        Image.new('RGB',(1600,900),'#cc8822').save(self.root/'b.png')
        self.manifest={'schema_version':1,'title':'Fixture','aspect_ratio':'16:9','slides':[{'id':'second','image':'b.png','expected_text':['SECOND'],'reviewed':True},{'id':'first','image':'a.png','expected_text':['FIRST'],'reviewed':True}]}
        self.path=self.root/'deck.json';self.write()
    def tearDown(self):self.temp.cleanup()
    def write(self):self.path.write_text(json.dumps(self.manifest),encoding='utf-8')
    def test_order_pages_and_one_picture_per_slide(self):
        report=package(self.path,self.root/'exports')
        self.assertEqual(report['order'],['second','first'])
        pdf=PdfReader(self.root/'exports'/'fixture.pdf');self.assertEqual(len(pdf.pages),2)
        for page in pdf.pages:self.assertAlmostEqual(float(page.mediabox.width)/float(page.mediabox.height),16/9)
        ns={'p':'http://schemas.openxmlformats.org/presentationml/2006/main','a':'http://schemas.openxmlformats.org/drawingml/2006/main'}
        with zipfile.ZipFile(self.root/'exports'/'fixture.pptx') as z:
            p=ET.fromstring(z.read('ppt/presentation.xml'));size=p.find('p:sldSz',ns);self.assertEqual(int(size.get('cx'))*9,int(size.get('cy'))*16)
            for i in [1,2]:
                slide=ET.fromstring(z.read(f'ppt/slides/slide{i}.xml'))
                self.assertEqual(len(slide.findall('.//p:pic',ns)),1)
                self.assertEqual(len(slide.findall('.//a:t',ns)),0)
        transcript=(self.root/'exports'/'fixture-transcript.md').read_text(encoding='utf-8')
        self.assertLess(transcript.index('SECOND'),transcript.index('FIRST'))
    def test_wrong_aspect_fails_before_export(self):
        Image.new('RGB',(1600,1000)).save(self.root/'b.png')
        with self.assertRaisesRegex(ValueError,'not 16:9'):package(self.path,self.root/'exports')
        self.assertFalse((self.root/'exports'/'fixture.pdf').exists())
    def test_native_one_pixel_rounding_is_reported(self):
        Image.new('RGB',(1672,941)).save(self.root/'rounding.png')
        check=inspect_image(self.root/'rounding.png');self.assertFalse(check['exact_16_9']);self.assertEqual(check['native_rounding_pixels'],.5)
    def test_unreviewed_output_requires_draft(self):
        self.manifest['slides'][0]['reviewed']=False;self.write()
        with self.assertRaisesRegex(ValueError,'not been reviewed'):package(self.path,self.root/'exports')
        report=package(self.path,self.root/'exports',formats=('pdf',),allow_unreviewed=True)
        self.assertTrue(report['draft']);self.assertTrue((self.root/'exports'/'DRAFT-fixture.pdf').exists())
    def test_output_collision_refuses_overwrite(self):
        out=self.root/'exports';out.mkdir();existing=out/'fixture.pdf';existing.write_bytes(b'KEEP')
        with self.assertRaisesRegex(ValueError,'already exist'):package(self.path,out)
        self.assertEqual(existing.read_bytes(),b'KEEP')
    def test_duplicate_ids_and_paths_rejected(self):
        self.manifest['slides'][1]['id']='second';self.write()
        with self.assertRaisesRegex(ValueError,'unique'):load_manifest(self.path)
        self.manifest['slides'][1]['id']='first';self.manifest['slides'][1]['image']='b.png';self.write()
        with self.assertRaisesRegex(ValueError,'Duplicate image'):load_manifest(self.path)
    def test_manifest_path_cannot_escape_project(self):
        self.manifest['slides'][0]['image']='../outside.png';self.write()
        with self.assertRaisesRegex(ValueError,'escapes'):load_manifest(self.path)
    def test_missing_image_and_non_boolean_review_rejected(self):
        self.manifest['slides'][0]['image']='missing.png';self.write()
        with self.assertRaisesRegex(ValueError,'Missing image'):load_manifest(self.path)
        self.manifest['slides'][0]['image']='b.png';self.manifest['slides'][0]['reviewed']='true';self.write()
        with self.assertRaisesRegex(ValueError,'Boolean'):load_manifest(self.path)
    def test_exact_copy_record_is_required(self):
        del self.manifest['slides'][0]['expected_text'];self.write()
        with self.assertRaisesRegex(ValueError,'needs expected_text'):load_manifest(self.path)

if __name__=='__main__':unittest.main()
