def validate_arg_deprecation(self, cli_args, answer_file_args):
    """
    अप्रचलित तर्कों को मान्य करता है और उन्हें प्रिंट करता है।

    :param cli_args: CLI (कमांड लाइन इंटरफ़ेस) से प्राप्त तर्कों की डिक्शनरी 
    :param answer_file_args: फ़ाइलों से प्राप्त तर्कों की डिक्शनरी
    """
    deprecated_args = {
        'force': 'use --yes instead',
        'quiet': 'use --silent instead',
        'verbose': 'use --debug instead'
    }

    # Check CLI args for deprecated options
    for arg in cli_args:
        if arg in deprecated_args:
            print(f"Warning: The argument '--{arg}' is deprecated. {deprecated_args[arg]}")

    # Check answer file args for deprecated options 
    for arg in answer_file_args:
        if arg in deprecated_args:
            print(f"Warning: The argument '{arg}' in answer file is deprecated. {deprecated_args[arg]}")