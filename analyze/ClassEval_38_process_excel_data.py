def process_excel_data(self, N, save_file_name):
    """
    निर्दिष्ट कॉलम को Excel फ़ाइल में बड़े अक्षरों में बदलें
    :param N: int, उस कॉलम का अनुक्रमांक जिसे बदलना है
    :param save_file_name: str, स्रोत फ़ाइल का नाम
    :return:(int, str), पहला write_excel का लौटने वाला मान है, जबकि दूसरा संसाधित डेटा का सहेजा गया फ़ाइल नाम है
    >>> processor = ExcelProcessor()
    >>> success, output_file = processor.process_excel_data(1, 'test_data.xlsx')
    """
    import pandas as pd
    import os
    
    # Read the Excel file
    df = pd.read_excel(save_file_name)
    
    # Convert the specified column (N) to uppercase
    # N is 1-indexed, so we need to convert to 0-indexed
    if N > 0 and N <= len(df.columns):
        column_name = df.columns[N - 1]
        df[column_name] = df[column_name].astype(str).str.upper()
    
    # Generate output filename
    base_name = os.path.splitext(save_file_name)[0]
    output_file_name = f"{base_name}_processed.xlsx"
    
    # Write the modified data back to Excel
    result = self.write_excel(df, output_file_name)
    
    return (result, output_file_name)