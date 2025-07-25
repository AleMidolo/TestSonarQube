def _get_err_indices(self, coord_name):
    """
    एक समन्वय (coordinate) से संबंधित त्रुटि सूचकांक (error indices) प्राप्त करें।
    """
    # मान लें कि self.errors एक डिक्शनरी है जिसमें समन्वय नाम कुंजी के रूप में हैं
    # और त्रुटि सूचकांक मान के रूप में हैं।
    if coord_name in self.errors:
        return self.errors[coord_name]
    else:
        return []