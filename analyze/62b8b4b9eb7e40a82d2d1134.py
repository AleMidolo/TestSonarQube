def namesAndDescriptions(self, all=False): # pylint:disable=redefined-builtin
    """
    इंटरफेस द्वारा परिभाषित एट्रिब्यूट नाम और विवरण लौटाएं।
    
    Args:
        all (bool): यदि True, तो सभी एट्रिब्यूट्स के नाम और विवरण लौटाएं। 
                   यदि False, तो केवल उन एट्रिब्यूट्स के नाम और विवरण लौटाएं जो इंटरफेस द्वारा परिभाषित हैं।
    
    Returns:
        dict: एट्रिब्यूट नाम और उनके विवरण का डिक्शनरी।
    """
    if not all:
        # केवल इंटरफेस द्वारा परिभाषित एट्रिब्यूट्स लौटाएं
        return {attr: desc for attr, desc in self._attributes.items() if desc.get('defined_by_interface', False)}
    else:
        # सभी एट्रिब्यूट्स लौटाएं
        return self._attributes