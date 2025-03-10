import argparse

def parse_arguments(*unparsed_arguments):
    """
    इस स्क्रिप्ट को जिन कमांड-लाइन आर्ग्युमेंट्स के साथ चलाया गया है, उन आर्ग्युमेंट्स को पार्स करें और उन्हें एक डिक्ट (dict) के रूप में लौटाएं। यह डिक्ट सबपार्सर के नाम (या "global") को `argparse.Namespace` इंस्टेंस के साथ मैप करता है।
    """
    parser = argparse.ArgumentParser(description="Parse command-line arguments.")
    subparsers = parser.add_subparsers(dest="subparser_name", help="Sub-command help")

    # Add subparsers here if needed
    # Example:
    # subparser1 = subparsers.add_parser('subparser1', help='subparser1 help')
    # subparser1.add_argument('--arg1', type=int, help='arg1 help')

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)

    # Create a dictionary to map subparser names to their arguments
    parsed_args = {}
    if hasattr(args, 'subparser_name'):
        parsed_args[args.subparser_name] = args
    else:
        parsed_args["global"] = args

    return parsed_args