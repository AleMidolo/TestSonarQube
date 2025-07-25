def get_silent_args(self, args):
    """
    मौन (साइलेंट) तर्कों की सूची प्राप्त करें।

    :param args: प्राप्त तर्क (arguments)।
    :return: list, मौन (साइलेंट) तर्कों के नाम।
    """
    silent_args = []
    
    # Check if args is a dictionary
    if isinstance(args, dict):
        # Iterate through args and find ones marked as silent
        for arg_name, arg_value in args.items():
            if isinstance(arg_value, dict) and arg_value.get('silent', False):
                silent_args.append(arg_name)
                
    return silent_args