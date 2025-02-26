def names(self, all=False): # pylint:disable=redefined-builtin
    """
    इंटरफेस द्वारा परिभाषित एट्रिब्यूट नाम लौटाएं।
        if not all:
    
    इंटरफेस द्वारा परिभाषित एट्रिब्यूट नाम लौटाएं।
    """
    if all:
        return [attr for attr in dir(self) if not attr.startswith('_')]
    else:
        return [attr for attr in dir(self) if not attr.startswith('_') and not callable(getattr(self, attr))]