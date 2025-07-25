def _get_err_indices(self, coord_name):
    """
    एक समन्वय (coordinate) से संबंधित त्रुटि सूचकांक (error indices) प्राप्त करें।
    """
    # Get error indices for the given coordinate
    if coord_name in self.error_indices:
        return self.error_indices[coord_name]
    else:
        return []  # Return empty list if no errors found for coordinate