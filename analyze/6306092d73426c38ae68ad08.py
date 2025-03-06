def _get_conditionally_required_args(self, command_name, options_spec, args):
    """
    उन तर्कों (arguments) की सूची बनाएं जिनके लिए ``required_when`` शर्त लागू होती है।

    :param command_name: कमांड का नाम।
    :param options_spec: कमांड स्पेसिफिकेशन विकल्पों की सूची।
    :param args: प्राप्त इनपुट तर्क (arguments)।
    :return: list, उन तर्क नामों की सूची जिन पर ``required_when`` शर्त लागू होती है।
    """
    conditionally_required_args = []
    
    for option in options_spec:
        if 'required_when' in option:
            condition = option['required_when']
            if condition in args:
                conditionally_required_args.append(option['name'])
    
    return conditionally_required_args