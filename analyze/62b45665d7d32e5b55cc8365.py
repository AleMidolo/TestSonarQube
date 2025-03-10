import argparse

def parse_arguments(*unparsed_arguments):
    """
    इस स्क्रिप्ट को जिन कमांड-लाइन आर्ग्युमेंट्स के साथ चलाया गया है, उन आर्ग्युमेंट्स को पार्स करें और उन्हें एक डिक्ट (dict) के रूप में लौटाएं। यह डिक्ट सबपार्सर के नाम (या "global") को `argparse.Namespace` इंस्टेंस के साथ मैप करता है।
    """
    parser = argparse.ArgumentParser(description="Parse command-line arguments.")
    subparsers = parser.add_subparsers(dest="subparser_name", help="Sub-command help")

    # Example subparser
    subparser_example = subparsers.add_parser("example", help="Example subcommand")
    subparser_example.add_argument("--example_arg", type=str, help="Example argument")

    # Parse the arguments
    parsed_args = parser.parse_args(unparsed_arguments)

    # Convert the Namespace object to a dictionary
    args_dict = {}
    if parsed_args.subparser_name:
        args_dict[parsed_args.subparser_name] = parsed_args
    else:
        args_dict["global"] = parsed_args

    return args_dict