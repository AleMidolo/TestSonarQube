import argparse

def parse_arguments(*unparsed_arguments):
    """
    इस स्क्रिप्ट को जिन कमांड-लाइन आर्ग्युमेंट्स के साथ चलाया गया है, उन आर्ग्युमेंट्स को पार्स करें और उन्हें एक डिक्ट (dict) के रूप में लौटाएं। यह डिक्ट सबपार्सर के नाम (या "global") को `argparse.Namespace` इंस्टेंस के साथ मैप करता है।
    """
    parser = argparse.ArgumentParser(description="Parse command-line arguments.")
    parser.add_argument('--global-arg', type=str, help='Global argument')
    
    subparsers = parser.add_subparsers(dest='subparser_name', help='Sub-commands')
    
    # Example subparser
    subparser1 = subparsers.add_parser('subcommand1', help='First subcommand')
    subparser1.add_argument('--arg1', type=str, help='Argument for subcommand1')
    
    # Another example subparser
    subparser2 = subparsers.add_parser('subcommand2', help='Second subcommand')
    subparser2.add_argument('--arg2', type=int, help='Argument for subcommand2')
    
    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)
    
    # Convert the Namespace object to a dictionary
    args_dict = vars(args)
    
    # Map the subparser name to the parsed arguments
    result = {}
    if args.subparser_name:
        result[args.subparser_name] = args_dict
    else:
        result['global'] = args_dict
    
    return result