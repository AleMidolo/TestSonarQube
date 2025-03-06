def names(self, all=False):  # pylint:disable=redefined-builtin
    """
    इंटरफेस द्वारा परिभाषित एट्रिब्यूट नाम लौटाएं।
    if not all:
        return [name for name in dir(self) if not name.startswith('_')]
    else:
        return dir(self)