def namesAndDescriptions(self, all=False): # pylint:disable=redefined-builtin
    """
    इंटरफेस द्वारा परिभाषित एट्रिब्यूट नाम और विवरण लौटाएं।
    if not all:
    इंटरफेस द्वारा परिभाषित एट्रिब्यूट नाम और विवरण लौटाएं।
    """
    attrs = {}
    for name, desc in self.getDescriptionFor(all):
        attrs[name] = desc
    return attrs