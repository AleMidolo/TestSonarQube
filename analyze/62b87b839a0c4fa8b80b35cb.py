def _get_err_indices(self, coord_name):
    """
    एक समन्वय (coordinate) से संबंधित त्रुटि सूचकांक (error indices) प्राप्त करें।
    """
    # Assuming self.errors is a dictionary where keys are coordinate names and values are lists of error indices
    if coord_name in self.errors:
        return self.errors[coord_name]
    else:
        return []