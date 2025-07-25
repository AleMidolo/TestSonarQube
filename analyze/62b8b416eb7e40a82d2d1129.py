def names(self, all=False):  # pylint:disable=redefined-builtin
    """
    इंटरफेस द्वारा परिभाषित एट्रिब्यूट नाम लौटाएं।
    
    :param all: यदि True है, तो सभी एट्रिब्यूट नाम लौटाएं। अन्यथा, केवल इंटरफेस द्वारा परिभाषित एट्रिब्यूट नाम लौटाएं।
    :return: एट्रिब्यूट नामों की सूची।
    """
    if not all:
        # केवल इंटरफेस द्वारा परिभाषित एट्रिब्यूट नाम लौटाएं
        return [attr for attr in dir(self) if not attr.startswith('_')]
    else:
        # सभी एट्रिब्यूट नाम लौटाएं
        return dir(self)