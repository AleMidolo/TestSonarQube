import argparse

def parse_arguments(*unparsed_arguments):
    """
    इस स्क्रिप्ट को जिन कमांड-लाइन आर्ग्युमेंट्स के साथ चलाया गया है, उन आर्ग्युमेंट्स को पार्स करें और उन्हें एक डिक्ट (dict) के रूप में लौटाएं। यह डिक्ट सबपार्सर के नाम (या "global") को `argparse.Namespace` इंस्टेंस के साथ मैप करता है।
    """
    parser = argparse.ArgumentParser()
    # Add subparsers if needed
    subparsers = parser.add_subparsers(dest='subparser_name')

    # Example of adding a subparser
    # subparser = subparsers.add_parser('example')
    # subparser.add_argument('--option', type=str, help='An example option')

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)
    
    # Convert Namespace to dict
    return vars(args)