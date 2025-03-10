import argparse

def parse_arguments(*unparsed_arguments):
    """
    इस स्क्रिप्ट को जिन कमांड-लाइन आर्ग्युमेंट्स के साथ चलाया गया है, उन आर्ग्युमेंट्स को पार्स (parse) करें और उन्हें एक डिक्शनरी (dict) के रूप में लौटाएं। यह डिक्शनरी सबपार्सर (subparser) के नाम (या "global") को `argparse.Namespace` इंस्टेंस से मैप करती है।
    """
    parser = argparse.ArgumentParser(description="Parse command-line arguments.")
    subparsers = parser.add_subparsers(dest="command", help="Sub-command help")

    # Add subparsers here as needed
    # Example:
    # subparser_example = subparsers.add_parser('example', help='Example subparser')
    # subparser_example.add_argument('--example_arg', type=str, help='Example argument')

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)

    # Create a dictionary to map subparser names to their arguments
    parsed_arguments = {}
    if hasattr(args, 'command'):
        parsed_arguments[args.command] = args
    else:
        parsed_arguments["global"] = args

    return parsed_arguments