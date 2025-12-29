def read_excel(self, file_name):
    """
        एक्सेल फ़ाइलों से डेटा पढ़ना
        :param file_name:str, पढ़ने के लिए एक्सेल फ़ाइल का नाम
        :return:list of data, एक्सेल में डेटा
        """
    try:
        workbook = openpyxl.load_workbook(file_name, data_only=True)
        sheet = workbook.active
        data = []
        for row in sheet.iter_rows(values_only=True):
            data.append(row)
        workbook.close()
        return data
    except Exception as e:
        return None