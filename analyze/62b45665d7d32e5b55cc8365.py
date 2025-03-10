import argparse

def parse_arguments(*unparsed_arguments):
    """
    इस स्क्रिप्ट को जिन कमांड-लाइन आर्ग्युमेंट्स के साथ चलाया गया है, उन आर्ग्युमेंट्स को पार्स करें और उन्हें एक डिक्ट (dict) के रूप में लौटाएं। यह डिक्ट सबपार्सर के नाम (या "global") को `argparse.Namespace` इंस्टेंस के साथ मैप करता है।
    """
    parser = argparse.ArgumentParser(description="Parse command-line arguments.")
    subparsers = parser.add_subparsers(dest="subparser_name", help="Sub-command help")

    # Add a global parser (no subcommand)
    global_parser = subparsers.add_parser("global", help="Global arguments")

    # Example of adding arguments to the global parser
    global_parser.add_argument("--global_arg", type=str, help="A global argument")

    # Example of adding a subcommand parser
    subcommand_parser = subparsers.add_parser("subcommand", help="Subcommand help")
    subcommand_parser.add_argument("--sub_arg", type=str, help="A subcommand argument")

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)

    # Convert the Namespace to a dictionary
    args_dict = vars(args)

    # Map the subparser name to the parsed arguments
    result = {args.subparser_name: args_dict} if args.subparser_name else {"global": args_dict}

    return result