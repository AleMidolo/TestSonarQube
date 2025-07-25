import argparse

def parse_subparser_arguments(unparsed_arguments, subparsers):
    """
    दिए गए तर्कों (arguments) की एक श्रृंखला और एक डिक्शनरी जो सबपार्सर (subparser) के नाम को 
    argparse.ArgumentParser इंस्टेंस से मैप करती है, के आधार पर, प्रत्येक अनुरोधित क्रिया के 
    सबपार्सर को सभी तर्कों को पार्स (parse) करने का मौका दें। 

    यह प्रक्रिया सामान्य तर्कों जैसे "--repository" को कई सबपार्सरों के बीच साझा करने की अनुमति देती है।

    परिणाम को एक ट्यूपल (tuple) के रूप में लौटाएं, जिसमें शामिल हैं:
    1. एक डिक्शनरी जो सबपार्सर के नाम को पार्स किए गए तर्कों के नेमस्पेस (namespace) से मैप करती है।
    2. उन तर्कों की एक सूची जो किसी भी सबपार्सर द्वारा दावा नहीं किए गए हैं।
    """
    parsed_args = {}
    remaining_args = unparsed_arguments.copy()
    
    for subparser_name, parser in subparsers.items():
        try:
            args, remaining = parser.parse_known_args(remaining_args)
            parsed_args[subparser_name] = args
            remaining_args = remaining
        except argparse.ArgumentError:
            continue
    
    return parsed_args, remaining_args