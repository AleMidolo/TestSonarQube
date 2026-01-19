def read_text(self):
    """
        एक वर्ड दस्तावेज़ की सामग्री को पढ़ता है और इसे एक स्ट्रिंग के रूप में लौटाता है।
        :return: str, वर्ड दस्तावेज़ की सामग्री।
        """
    try:
        doc = Document(self.file_path)
        content = []
        for paragraph in doc.paragraphs:
            content.append(paragraph.text)
        return '\n'.join(content)
    except Exception as e:
        return str(e)