def get_silent_args(self, args):
    """
    मौन (साइलेंट) तर्कों की सूची प्राप्त करें।

    :param args: प्राप्त तर्क (arguments)।
    :return: list, मौन (साइलेंट) तर्कों के नाम।
    """
    silent_args = [arg for arg in args if arg.startswith('_')]
    return silent_args