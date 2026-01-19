def process_excel_data(self, N, save_file_name):
    """
    निर्दिष्ट कॉलम को Excel फ़ाइल में बड़े अक्षरों में बदलें
    :param N: int, उस कॉलम का अनुक्रमांक जिसे बदलना है
    :param save_file_name: str, स्रोत फ़ाइल का नाम
    :return:(int, str), पहला write_excel का लौटने वाला मान है, जबकि दूसरा संसाधित डेटा का सहेजा गया फ़ाइल नाम है
    >>> processor = ExcelProcessor()
    >>> success, output_file = processor.process_excel_data(1, 'test_data.xlsx')
    """
    import openpyxl
    import os
    
    # Read the Excel file
    workbook = openpyxl.load_workbook(save_file_name)
    sheet = workbook.active
    
    # Process the specified column (convert to uppercase)
    for row in sheet.iter_rows(min_row=1, min_col=N, max_col=N):
        for cell in row:
            if cell.value is not None and isinstance(cell.value, str):
                cell.value = cell.value.upper()
    
    # Generate output filename
    base_name = os.path.splitext(save_file_name)[0]
    extension = os.path.splitext(save_file_name)[1]
    output_file_name = f"{base_name}_processed{extension}"
    
    # Save the workbook
    try:
        workbook.save(output_file_name)
        workbook.close()
        result = self.write_excel(output_file_name)
        return (result, output_file_name)
    except Exception as e:
        workbook.close()
        return (0, output_file_name)