def process_excel_data(self, N, save_file_name):
    """
    Change the specified column in the Excel file to uppercase
    :param N: int, The serial number of the column that want to change
    :param save_file_name: str, source file name
    :return:(int, str), The former is the return value of write_excel, while the latter is the saved file name of the processed data
    >>> processor = ExcelProcessor()
    >>> success, output_file = processor.process_excel_data(1, 'test_data.xlsx')
    """
    try:
        data = self.read_excel(save_file_name)
        if data is None:
            return (0, save_file_name)
        for i in range(len(data)):
            if len(data[i]) > N:
                data[i] = list(data[i])
                data[i][N] = str(data[i][N]).upper()
        output_file_name = 'processed_' + save_file_name
        success = self.write_excel(data, output_file_name)
        return (success, output_file_name)
    except:
        return (0, save_file_name)