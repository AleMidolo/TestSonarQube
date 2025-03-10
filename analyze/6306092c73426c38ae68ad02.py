def validate_arg_deprecation(self, cli_args, answer_file_args):
    """
    अप्रचलित तर्कों को मान्य करता है और उन्हें प्रिंट करता है।

    :param cli_args: CLI (कमांड लाइन इंटरफ़ेस) से प्राप्त तर्कों की डिक्शनरी
    :param answer_file_args: फ़ाइलों से प्राप्त तर्कों की डिक्शनरी
    """
    deprecated_args = set(cli_args.keys()).intersection(answer_file_args.keys())
    
    for arg in deprecated_args:
        print(f"अप्रचलित तर्क: {arg}")
        print(f"CLI से मान: {cli_args[arg]}")
        print(f"फ़ाइल से मान: {answer_file_args[arg]}")
        print("यह तर्क अप्रचलित है और भविष्य के संस्करणों में हटाया जा सकता है।\n")