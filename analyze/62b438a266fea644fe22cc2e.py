import argparse

def parse_arguments(*unparsed_arguments):
    """
    इस स्क्रिप्ट को जिन कमांड-लाइन आर्ग्युमेंट्स के साथ चलाया गया है, उन आर्ग्युमेंट्स को पार्स (parse) करें और उन्हें एक डिक्शनरी (dict) के रूप में लौटाएं। यह डिक्शनरी सबपार्सर (subparser) के नाम (या "global") को `argparse.Namespace` इंस्टेंस से मैप करती है।
    """
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subparser_name')

    # Example subparser
    subparser_example = subparsers.add_parser('example')
    subparser_example.add_argument('--option', type=str, help='An example option')

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)

    # Convert Namespace to dict
    return {args.subparser_name: vars(args)}