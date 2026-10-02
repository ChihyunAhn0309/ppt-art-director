import importlib.util
import json
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SKILL=ROOT
def module(name):
    spec=importlib.util.spec_from_file_location(name,SKILL/'scripts'/f'{name}.py')
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
palette=module('palette_check');pptx=module('pptx_audit')

def package(file, broken=False, bad_target=False, duplicate=False, reordered=False):
    P,A,R,PR=pptx.P,pptx.A,pptx.R,pptx.PR
    body=f'<p:sld xmlns:p="{P}" xmlns:a="{A}"><p:cSld><p:spTree><p:sp><p:nvSpPr><p:cNvPr id="2" name="target"/></p:nvSpPr><p:txBody><a:p><a:r><a:t>연구 결과</a:t></a:r></a:p></p:txBody></p:sp></p:spTree></p:cSld>'
    if duplicate: body=body.replace('</p:spTree>','<p:sp><p:nvSpPr><p:cNvPr id="2" name="duplicate"/></p:nvSpPr></p:sp></p:spTree>')
    body+=f'<p:timing><p:tnLst><p:par><p:cTn id="1"><p:childTnLst><p:anim><p:cBhvr><p:tgtEl><p:spTgt spid="{99 if bad_target else 2}"/></p:tgtEl></p:cBhvr></p:anim></p:childTnLst></p:cTn></p:par></p:tnLst></p:timing></p:sld>'
    with zipfile.ZipFile(file,'w') as z:
        z.writestr('[Content_Types].xml','<Types/>')
        z.writestr('ppt/presentation.xml',f'<p:presentation xmlns:p="{P}" xmlns:r="{R}"><p:sldIdLst><p:sldId id="256" r:id="rId1"/></p:sldIdLst><p:sldSz cx="12192000" cy="6858000"/></p:presentation>')
        target='slides/missing.xml' if broken else 'slides/slide7.xml' if reordered else 'slides/slide1.xml'
        z.writestr('ppt/_rels/presentation.xml.rels',f'<Relationships xmlns="{PR}"><Relationship Id="rId1" Type="{R}/slide" Target="{target}"/></Relationships>')
        z.writestr('ppt/slides/slide7.xml' if reordered else 'ppt/slides/slide1.xml',body)

class Checks(unittest.TestCase):
    def test_black_white(self): self.assertAlmostEqual(palette.contrast('000000','#FFFFFF'),21)
    def test_identical(self): self.assertAlmostEqual(palette.contrast('2458A6','2458A6'),1)
    def test_bad_hex(self):
        for value in ['ABC','FFFFFFFF','evil',None]:
            with self.assertRaises(ValueError):palette.rgb(value)
    def test_low_contrast(self):
        result=palette.check_palette({'colors':{'a':'FFFFFF','b':'EEEEEE'},'pairs':[{'fg':'a','bg':'b'}]})
        self.assertFalse(result['pass'])
    def test_palettes(self):
        data=json.loads((SKILL/'assets/palettes.json').read_text(encoding='utf-8'))
        self.assertEqual(len(data['palettes']),12)
        self.assertTrue(all(palette.check_palette(p)['pass'] for p in data['palettes']))
    def test_relationship_paths(self):
        self.assertEqual(pptx.resolve_target('ppt/slides/slide1.xml','../media/image1.png'),'ppt/media/image1.png')
        self.assertEqual(pptx.resolve_target('ppt/presentation.xml','/ppt/slides/slide1.xml'),'ppt/slides/slide1.xml')
        with self.assertRaises(ValueError):pptx.resolve_target('ppt/a.xml','../../escape.xml')
    def test_package_failures(self):
        with tempfile.TemporaryDirectory() as folder:
            file=Path(folder)/'case.pptx'
            for flags,expected in [({},True),({'reordered':True},True),({'broken':True},False),({'bad_target':True},False),({'duplicate':True},False)]:
                package(file,**flags)
                self.assertEqual(pptx.audit(file,1)['pass'],expected,flags)
            package(file)
            self.assertFalse(pptx.audit(file,2)['pass'])
    def test_xml_entities(self):
        with self.assertRaises(ValueError):pptx.parse_xml(b'<!DOCTYPE x [<!ENTITY e "test">]><x>&e;</x>')
    def test_skill_links(self):
        import re
        for file in SKILL.rglob('*.md'):
            for link in re.findall(r'\]\(([^)]+)\)',file.read_text(encoding='utf-8')):
                if not link.startswith(('http:','https:','#')):
                    self.assertTrue((file.parent/link.split('#')[0]).is_file(),f'{file}: {link}')

if __name__=='__main__':unittest.main(verbosity=2)
