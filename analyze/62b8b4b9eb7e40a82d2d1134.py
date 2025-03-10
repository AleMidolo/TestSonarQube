def namesAndDescriptions(self, all=False):  # pylint:disable=redefined-builtin
    """
    इंटरफेस द्वारा परिभाषित एट्रिब्यूट नाम और विवरण लौटाएं।
    
    Args:
        all (bool): यदि True, तो सभी एट्रिब्यूट्स के नाम और विवरण लौटाएं। अन्यथा, केवल कुछ विशिष्ट एट्रिब्यूट्स के नाम और विवरण लौटाएं।
    
    Returns:
        dict: एट्रिब्यूट नाम और उनके विवरण का डिक्शनरी।
    """
    attributes = {
        "name": "इंटरफेस का नाम",
        "description": "इंटरफेस का विवरण",
        "version": "इंटरफेस का संस्करण"
    }
    
    if not all:
        return {key: attributes[key] for key in ["name", "description"]}
    else:
        return attributes