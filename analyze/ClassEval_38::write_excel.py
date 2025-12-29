def write_excel(self, data, file_name):
    """
        निर्दिष्ट Excel फ़ाइल में डेटा लिखें
        :param data: सूची, लिखने के लिए डेटा
        :param file_name: स्ट्रिंग, लिखने के लिए Excel फ़ाइल का नाम
        :return: 0 या 1, 1 सफल लेखन का प्रतिनिधित्व करता है, 0 असफल लेखन का प्रतिनिधित्व करता है
        >>> processor = ExcelProcessor()
        >>> new_data = [
        >>>     ('नाम', 'उम्र', 'देश'),
        >>>     ('जॉन', 25, 'यूएसए'),
        >>>     ('ऐलिस', 30, 'कनाडा'),
        >>>     ('बॉब', 35, 'ऑस्ट्रेलिया'),
        >>>     ('जूलिया', 28, 'जर्मनी')
        >>> ]
        >>> data = processor.write_excel(new_data, 'test_data.xlsx')
        """
    try:
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        for row_idx, row_data in enumerate(data, start=1):
            for col_idx, cell_value in enumerate(row_data, start=1):
                sheet.cell(row=row_idx, column=col_idx, value=cell_value)
        workbook.save(file_name)
        workbook.close()
        return 1
    except Exception as e:
        return 0