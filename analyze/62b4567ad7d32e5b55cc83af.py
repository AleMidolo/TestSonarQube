import argparse

def parse_arguments(*arguments):
    """
    इस फ़ंक्शन का उद्देश्य दिए गए कमांड-लाइन आर्ग्युमेंट्स को पार्स करना है और उन्हें एक 
    ArgumentParser इंस्टेंस के रूप में लौटाना है।
    """
    parser = argparse.ArgumentParser(description="Parse command-line arguments.")
    
    # Add arguments to the parser
    for arg in arguments:
        parser.add_argument(arg)
    
    # Parse the arguments
    args = parser.parse_args()
    
    return args