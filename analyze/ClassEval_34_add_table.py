def add_table(self, data):
    """
        निर्दिष्ट डेटा के साथ Word दस्तावेज़ में एक तालिका जोड़ता है।
        :param data: सूचियों की सूची, तालिका को भरने के लिए डेटा।
        :return: bool, यदि तालिका सफलतापूर्वक जोड़ी गई है तो True, अन्यथा False।
        """
    try:
        doc = Document(self.file_path)
        table = doc.add_table(rows=len(data), cols=len(data[0]))
        for i, row in enumerate(data):
            for j, cell in enumerate(row):
                table.cell(i, j).text = str(cell)
        doc.save(self.file_path)
        return True
    except:
        return False