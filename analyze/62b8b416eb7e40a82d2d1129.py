def names(self, all=False): # pylint:disable=redefined-builtin
    """
    इंटरफेस द्वारा परिभाषित एट्रिब्यूट नाम लौटाएं।
    यदि `all` पैरामीटर `True` है, तो सभी एट्रिब्यूट नाम लौटाएं।
    अन्यथा, केवल इंटरफेस द्वारा परिभाषित एट्रिब्यूट नाम लौटाएं।
    """
    if not all:
        return [attr for attr in dir(self) if not attr.startswith('_')]
    else:
        return dir(self)