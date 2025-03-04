def names(self, all=False): # pylint:disable=redefined-builtin
    """
    इंटरफेस द्वारा परिभाषित एट्रिब्यूट नाम लौटाएं।
    if not all:
    
    
    इंटरफेस द्वारा परिभाषित एट्रिब्यूट नाम लौटाएं।
    """
    if not all:
        return [name for name in self._names if not name.startswith('_')]
    return list(self._names)