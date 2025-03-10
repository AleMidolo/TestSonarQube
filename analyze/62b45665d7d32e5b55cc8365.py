import argparse

def parse_arguments(*unparsed_arguments):
    """
    इस स्क्रिप्ट को जिन कमांड-लाइन आर्ग्युमेंट्स के साथ चलाया गया है, उन आर्ग्युमेंट्स को पार्स करें और उन्हें एक डिक्ट (dict) के रूप में लौटाएं। यह डिक्ट सबपार्सर के नाम (या "global") को `argparse.Namespace` इंस्टेंस के साथ मैप करता है।
    """
    parser = argparse.ArgumentParser(description="Parse command-line arguments.")
    subparsers = parser.add_subparsers(dest="command", help="Sub-command help")

    # Add subparsers here as needed
    # Example:
    # parser_foo = subparsers.add_parser('foo', help='foo help')
    # parser_foo.add_argument('bar', type=int, help='bar help')

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)

    # Return a dictionary mapping subparser names to their parsed arguments
    if args.command:
        return {args.command: args}
    else:
        return {"global": args}