from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

def write_text(self, content, font_size=12, alignment='left'):
    """
    将指定的内容写入Word文档。
    :param content: str,要写入的文本内容。
    :param font_size: int,可选,文本的字体大小(默认为12)。
    :param alignment: str,可选,文本的对齐方式('left'、'center'或'right'; 默认为'left')。
    :return: bool,如果写入操作成功则返回True,否则返回False。
    """
    try:
        # 添加段落
        paragraph = self.document.add_paragraph(content)
        
        # 设置字体大小
        for run in paragraph.runs:
            run.font.size = Pt(font_size)
        
        # 设置对齐方式
        alignment_map = {
            'left': WD_ALIGN_PARAGRAPH.LEFT,
            'center': WD_ALIGN_PARAGRAPH.CENTER,
            'right': WD_ALIGN_PARAGRAPH.RIGHT
        }
        
        if alignment.lower() in alignment_map:
            paragraph.alignment = alignment_map[alignment.lower()]
        else:
            paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT
        
        return True
    except Exception as e:
        return False