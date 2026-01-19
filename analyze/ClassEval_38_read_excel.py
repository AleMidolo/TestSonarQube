def read_excel(self, file_name):
    """
    एक्सेल फ़ाइलों से डेटा पढ़ना
    :param file_name:str, पढ़ने के लिए एक्सेल फ़ाइल का नाम
    :return:list of data, एक्सेल में डेटा
    """
    import openpyxl
    
    # एक्सेल फ़ाइल खोलें
    workbook = openpyxl.load_workbook(file_name)
    
    # पहली शीट प्राप्त करें
    sheet = workbook.active
    
    # डेटा को लिस्ट में संग्रहीत करें
    data = []
    
    # सभी पंक्तियों को पढ़ें
    for row in sheet.iter_rows(values_only=True):
        data.append(list(row))
    
    # वर्कबुक बंद करें
    workbook.close()
    
    return data