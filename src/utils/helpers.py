from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def style_as(txt, size=13, bold=False, italic=False, name="Times New Roman"):
    txt.font.name=name
    txt.font.size=Pt(size)
    txt.bold=bold
    txt.italic=italic

def add_hlink(Input_para, url, Input_text, size=10, bold=False):
    part = Input_para.part
    reID = part.relate_to(url, "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink", is_external=True)
    hlink = OxmlElement('w:hyperlink')
    hlink.set(qn('r:id'), reID)

    txtRun = OxmlElement('w:r')
    txtEdits = OxmlElement('w:rPr')
    color = OxmlElement('w:color'); color.set(qn('w:val'), '0000FF'); txtEdits.append(color)
    underline = OxmlElement('w:u'); underline.set(qn('w:val'), 'single'); txtEdits.append(underline)
    txtRun.append(txtEdits)
    txt = OxmlElement('w:t'); txt.text = Input_text; txtRun.append(txt)
    hlink.append(txtRun); Input_para._p.append(hlink)
    return hlink
