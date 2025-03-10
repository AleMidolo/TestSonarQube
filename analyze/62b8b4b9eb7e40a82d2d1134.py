def namesAndDescriptions(self, all=False):  # pylint:disable=redefined-builtin
    """
    इंटरफेस द्वारा परिभाषित एट्रिब्यूट नाम और विवरण लौटाएं।
    
    Args:
        all (bool): यदि True है, तो सभी एट्रिब्यूट्स को लौटाएं। अन्यथा केवल डिफ़ॉल्ट एट्रिब्यूट्स को लौटाएं।
    
    Returns:
        dict: एट्रिब्यूट नाम और उनके विवरण का डिक्शनरी।
    """
    attributes = {
        'name': 'इंटरफेस का नाम',
        'description': 'इंटरफेस का विवरण',
        'version': 'इंटरफेस का संस्करण',
    }
    
    if not all:
        return {k: v for k, v in attributes.items() if k in ['name', 'description']}
    return attributes