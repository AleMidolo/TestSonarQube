import argparse

def parse_arguments(*unparsed_arguments):
    """
    इस स्क्रिप्ट को जिन कमांड-लाइन आर्ग्युमेंट्स के साथ चलाया गया है, उन आर्ग्युमेंट्स को पार्स (parse) करें और उन्हें एक डिक्शनरी (dict) के रूप में लौटाएं। यह डिक्शनरी सबपार्सर (subparser) के नाम (या "global") को `argparse.Namespace` इंस्टेंस से मैप करती है।
    """
    parser = argparse.ArgumentParser(description="Parse command-line arguments.")
    subparsers = parser.add_subparsers(dest="command", help="Sub-command help")

    # Add subparsers here as needed
    # Example:
    # subparser1 = subparsers.add_parser('command1', help='command1 help')
    # subparser1.add_argument('--arg1', type=int, help='arg1 help')

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)

    # Convert the Namespace object to a dictionary
    args_dict = vars(args)

    # If no subcommand was provided, map to 'global'
    if args_dict.get('command') is None:
        args_dict['command'] = 'global'

    return args_dict