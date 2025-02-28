def namesAndDescriptions(self, all=False):  # pylint:disable=redefined-builtin
    """
    इंटरफेस द्वारा परिभाषित एट्रिब्यूट नाम और विवरण लौटाएं।
    if not all:
        return self._get_attributes()
    else:
        return self._get_all_attributes()