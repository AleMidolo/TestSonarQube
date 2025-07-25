def _get_err_indices(self, coord_name):
    """
    एक समन्वय (coordinate) से संबंधित त्रुटि सूचकांक (error indices) प्राप्त करें।
    """
    # Initialize empty list to store error indices
    err_indices = []
    
    # Get coordinate data
    coord_data = getattr(self, coord_name)
    
    # Check each value in coordinate data
    for i, val in enumerate(coord_data):
        # Add index to err_indices if value is invalid
        if val is None or pd.isna(val):
            err_indices.append(i)
            
    return err_indices