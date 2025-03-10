import argparse

def parse_arguments(*unparsed_arguments):
    """
    इस स्क्रिप्ट को जिन कमांड-लाइन आर्ग्युमेंट्स के साथ चलाया गया है, उन आर्ग्युमेंट्स को पार्स (parse) करें और उन्हें एक डिक्शनरी (dict) के रूप में लौटाएं। यह डिक्शनरी सबपार्सर (subparser) के नाम (या "global") को `argparse.Namespace` इंस्टेंस से मैप करती है।
    """
    parser = argparse.ArgumentParser(description="Parse command-line arguments.")
    subparsers = parser.add_subparsers(dest="subparser_name", help="Sub-command help")

    # Add subparsers here as needed
    # Example:
    # subparser1 = subparsers.add_parser('subparser1', help='subparser1 help')
    # subparser1.add_argument('--arg1', type=int, help='arg1 help')

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)

    # Create a dictionary to map subparser names to their respective Namespace objects
    parsed_arguments = {}
    if hasattr(args, 'subparser_name'):
        parsed_arguments[args.subparser_name] = args
    else:
        parsed_arguments["global"] = args

    return parsed_arguments