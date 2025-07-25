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
    remaining_args = list(unparsed_arguments)
    
    # Try parsing with each subparser
    for name, subparser in subparsers.items():
        try:
            # Parse known args, allowing unknown
            namespace, unknown = subparser.parse_known_args(remaining_args)
            parsed_args[name] = namespace
            
            # Update remaining args to only those that weren't recognized
            remaining_args = unknown
            
        except Exception:
            # If parsing fails, skip this subparser
            continue
            
    return parsed_args, remaining_args