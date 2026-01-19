def write_text(self, content, font_size=12, alignment='left'):
    """
    निर्दिष्ट सामग्री को एक Word दस्तावेज़ में लिखता है।
    :param content: str, लिखने के लिए पाठ सामग्री।
    :param font_size: int, वैकल्पिक, पाठ का फ़ॉन्ट आकार (डिफ़ॉल्ट 12 है)।
    :param alignment: str, वैकल्पिक, पाठ की संरेखण ('left', 'center', या 'right'; डिफ़ॉल्ट 'left' है)।
    :return: bool, यदि लिखने का कार्य सफल होता है तो True, अन्यथा False।
    """
    try:
        from docx import Document
        from docx.shared import Pt
        from docx.enum.text import WD_ALIGN_PARAGRAPH
        
        # Check if document exists, otherwise create new one
        if not hasattr(self, 'document') or self.document is None:
            self.document = Document()
        
        # Add paragraph with content
        paragraph = self.document.add_paragraph(content)
        
        # Set font size
        for run in paragraph.runs:
            run.font.size = Pt(font_size)
        
        # Set alignment
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