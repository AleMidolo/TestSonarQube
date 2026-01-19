def add_table(self, data):
    """
    निर्दिष्ट डेटा के साथ Word दस्तावेज़ में एक तालिका जोड़ता है।
    :param data: सूचियों की सूची, तालिका को भरने के लिए डेटा।
    :return: bool, यदि तालिका सफलतापूर्वक जोड़ी गई है तो True, अन्यथा False।
    """
    try:
        if not data or len(data) == 0:
            return False
        
        # Get number of rows and columns
        rows = len(data)
        cols = len(data[0]) if data[0] else 0
        
        if cols == 0:
            return False
        
        # Add table to document
        table = self.document.add_table(rows=rows, cols=cols)
        table.style = 'Table Grid'
        
        # Populate table with data
        for i, row_data in enumerate(data):
            row_cells = table.rows[i].cells
            for j, cell_data in enumerate(row_data):
                if j < cols:
                    row_cells[j].text = str(cell_data) if cell_data is not None else ''
        
        return True
    except Exception as e:
        return False