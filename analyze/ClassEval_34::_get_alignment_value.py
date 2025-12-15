def _get_alignment_value(self, alignment):
        """
        दिए गए संरेखण स्ट्रिंग के अनुसार संरेखण मान लौटाता है।
        :param alignment: str, संरेखण स्ट्रिंग ('left', 'center', या 'right')।
        :return: int, संरेखण मान।
        """
        if alignment == 'left':
            return WD_PARAGRAPH_ALIGNMENT.LEFT
        elif alignment == 'center':
            return WD_PARAGRAPH_ALIGNMENT.CENTER
        elif alignment == 'right':
            return WD_PARAGRAPH_ALIGNMENT.RIGHT
        else:
            raise ValueError("Invalid alignment value. Use 'left', 'center', or 'right'.")