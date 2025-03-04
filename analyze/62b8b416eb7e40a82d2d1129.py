def names(self, all=False): # pylint:disable=redefined-builtin
    """
    इंटरफेस द्वारा परिभाषित एट्रिब्यूट नाम लौटाएं।
    if not all:
    
    
    इंटरफेस द्वारा परिभाषित एट्रिब्यूट नाम लौटाएं।
    """
    result = []
    for attr in dir(self):
        if not attr.startswith('_'):  # Skip private/protected attributes
            if all or not callable(getattr(self, attr)):  # Skip methods if all=False
                result.append(attr)
    return sorted(result)