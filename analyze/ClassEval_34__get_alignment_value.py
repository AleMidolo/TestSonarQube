def _get_alignment_value(self, alignment):
    """
    दिए गए संरेखण स्ट्रिंग के अनुसार संरेखण मान लौटाता है।
    :param alignment: str, संरेखण स्ट्रिंग ('left', 'center', या 'right')।
    :return: int, संरेखण मान।
    """
    alignment_map = {
        'left': 0,
        'center': 1,
        'right': 2
    }
    return alignment_map.get(alignment.lower(), 0)