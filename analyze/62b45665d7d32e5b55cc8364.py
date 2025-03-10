def parse_subparser_arguments(unparsed_arguments, subparsers):
    """
    दिए गए तर्कों (arguments) की एक श्रृंखला और एक डिक्शनरी जो सबपार्सर (subparser) के नाम को 
    argparse.ArgumentParser इंस्टेंस से मैप करती है, के आधार पर, प्रत्येक अनुरोधित क्रिया के 
    सबपार्सर को सभी तर्कों को पार्स (parse) करने का मौका दें। 

    यह प्रक्रिया सामान्य तर्कों जैसे "--repository" को कई सबपार्सरों के बीच साझा करने की अनुमति देती है।

    परिणाम को एक ट्यूपल (tuple) के रूप में लौटाएं, जिसमें शामिल हैं:
    1. एक डिक्शनरी जो सबपार्सर के नाम को पार्स किए गए तर्कों के नेमस्पेस (namespace) से मैप करती है।
    2. उन तर्कों की सूची जो किसी भी सबपार्सर द्वारा दावा नहीं किए गए हैं।
    """
    import argparse

    # Initialize the main parser
    main_parser = argparse.ArgumentParser()
    subparsers_dict = {}

    # Add subparsers to the main parser
    for name, parser in subparsers.items():
        subparser = main_parser.add_subparsers().add_parser(name)
        subparsers_dict[name] = subparser

    # Parse the arguments using the main parser
    parsed_args, remaining_args = main_parser.parse_known_args(unparsed_arguments)

    # Create a dictionary to store the parsed arguments for each subparser
    parsed_subparser_args = {}

    # Iterate through the subparsers and parse the arguments
    for name, subparser in subparsers_dict.items():
        subparser_args, remaining_args = subparser.parse_known_args(remaining_args)
        parsed_subparser_args[name] = subparser_args

    return parsed_subparser_args, remaining_args