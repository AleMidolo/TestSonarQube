def names(self, all=False):  # pylint:disable=redefined-builtin
    """
    इंटरफेस द्वारा परिभाषित एट्रिब्यूट नाम लौटाएं।
    if not all:
        return [attr for attr in self.__dict__ if not attr.startswith('_')]
    else:
        return list(self.__dict__.keys())