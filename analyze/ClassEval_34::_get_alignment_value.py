def _get_alignment_value(self, alignment):
    """
        दिए गए संरेखण स्ट्रिंग के अनुसार संरेखण मान लौटाता है।
        :param alignment: str, संरेखण स्ट्रिंग ('left', 'center', या 'right')।
        :return: int, संरेखण मान।
        """
    alignment_mapping = {'left': WD_PARAGRAPH_ALIGNMENT.LEFT, 'center': WD_PARAGRAPH_ALIGNMENT.CENTER, 'right': WD_PARAGRAPH_ALIGNMENT.RIGHT}
    return alignment_mapping.get(alignment.lower(), WD_PARAGRAPH_ALIGNMENT.LEFT)