def write_text(self, content, font_size=12, alignment='left'):
    """
        निर्दिष्ट सामग्री को एक Word दस्तावेज़ में लिखता है।
        :param content: str, लिखने के लिए पाठ सामग्री।
        :param font_size: int, वैकल्पिक, पाठ का फ़ॉन्ट आकार (डिफ़ॉल्ट 12 है)।
        :param alignment: str, वैकल्पिक, पाठ की संरेखण ('left', 'center', या 'right'; डिफ़ॉल्ट 'left' है)।
        :return: bool, यदि लिखने का कार्य सफल होता है तो True, अन्यथा False।
        """
    try:
        doc = Document(self.file_path)
        paragraph = doc.add_paragraph(content)
        run = paragraph.runs[0]
        run.font.size = Pt(font_size)
        paragraph.alignment = self._get_alignment_value(alignment)
        doc.save(self.file_path)
        return True
    except:
        return False