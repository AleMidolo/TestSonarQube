import argparse

def parse_arguments(*unparsed_arguments):
    """
    इस स्क्रिप्ट को जिन कमांड-लाइन आर्ग्युमेंट्स के साथ चलाया गया है, उन आर्ग्युमेंट्स को पार्स करें और उन्हें एक डिक्ट (dict) के रूप में लौटाएं। यह डिक्ट सबपार्सर के नाम (या "global") को `argparse.Namespace` इंस्टेंस के साथ मैप करता है।
    """
    parser = argparse.ArgumentParser()
    # Add global arguments here if needed
    # Example: parser.add_argument('--global_arg', type=str, help='A global argument')

    # Parse the unparsed arguments
    args = parser.parse_args(unparsed_arguments)
    
    # Convert Namespace to dict
    return vars(args)