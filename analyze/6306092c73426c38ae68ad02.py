def validate_arg_deprecation(self, cli_args, answer_file_args):
    """
    अप्रचलित तर्कों को मान्य करता है और उन्हें प्रिंट करता है।

    :param cli_args: CLI (कमांड लाइन इंटरफ़ेस) से प्राप्त तर्कों की डिक्शनरी
    :param answer_file_args: फ़ाइलों से प्राप्त तर्कों की डिक्शनरी
    """
    deprecated_args = set(cli_args.keys()).intersection(set(answer_file_args.keys()))
    
    if deprecated_args:
        print("अप्रचलित तर्क पाए गए:")
        for arg in deprecated_args:
            print(f" - {arg}")
    else:
        print("कोई अप्रचलित तर्क नहीं पाए गए।")