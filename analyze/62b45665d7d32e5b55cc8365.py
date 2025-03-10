import argparse

def parse_arguments(*unparsed_arguments):
    """
    इस स्क्रिप्ट को जिन कमांड-लाइन आर्ग्युमेंट्स के साथ चलाया गया है, उन आर्ग्युमेंट्स को पार्स करें और उन्हें एक डिक्ट (dict) के रूप में लौटाएं। यह डिक्ट सबपार्सर के नाम (या "global") को `argparse.Namespace` इंस्टेंस के साथ मैप करता है।
    """
    parser = argparse.ArgumentParser(description="Parse command-line arguments.")
    subparsers = parser.add_subparsers(dest="subparser_name", help="Sub-command help")
    
    # Add subparsers or global arguments here as needed
    # Example:
    # subparser1 = subparsers.add_parser('sub1', help='sub1 help')
    # subparser1.add_argument('--foo', type=int, help='foo help')
    
    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)
    
    # Convert the Namespace to a dictionary
    args_dict = vars(args)
    
    # If no subparser was used, map to 'global'
    if args.subparser_name is None:
        args_dict = {'global': args_dict}
    else:
        args_dict = {args.subparser_name: args_dict}
    
    return args_dict