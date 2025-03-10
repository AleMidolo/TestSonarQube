import argparse

def parse_arguments(*unparsed_arguments):
    """
    इस स्क्रिप्ट को जिन कमांड-लाइन आर्ग्युमेंट्स के साथ चलाया गया है, उन आर्ग्युमेंट्स को पार्स करें और उन्हें एक डिक्ट (dict) के रूप में लौटाएं। यह डिक्ट सबपार्सर के नाम (या "global") को `argparse.Namespace` इंस्टेंस के साथ मैप करता है।
    """
    parser = argparse.ArgumentParser(description="Parse command-line arguments.")
    subparsers = parser.add_subparsers(dest="subparser_name", help="Sub-command help")

    # Add a global argument example
    parser.add_argument('--global-arg', type=str, help="A global argument")

    # Example subparser
    subparser_example = subparsers.add_parser('example', help="Example subcommand")
    subparser_example.add_argument('--sub-arg', type=int, help="An argument for the example subcommand")

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)

    # Convert the Namespace object to a dictionary
    args_dict = vars(args)

    # If a subparser was used, map the subparser name to its arguments
    if args.subparser_name:
        result = {args.subparser_name: args_dict}
    else:
        result = {"global": args_dict}

    return result