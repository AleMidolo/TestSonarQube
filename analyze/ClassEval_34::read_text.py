def read_text(self):
        """
        读取Word文档的内容并将其作为字符串返回。
        :return: str，Word文档的内容。
        """
        try:
            doc = Document(self.file_path)
            content = []
            for paragraph in doc.paragraphs:
                content.append(paragraph.text)
            return '\n'.join(content)
        except Exception as e:
            return str(e)