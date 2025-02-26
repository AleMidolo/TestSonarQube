def make_parsers():
    """
    एक शीर्ष-स्तरीय (top-level) पार्सर और उसके सबपार्सर बनाएं और उन्हें एक ट्यूपल के रूप में लौटाएं।
    """
    import argparse

    # शीर्ष-स्तरीय पार्सर बनाना
    top_parser = argparse.ArgumentParser(description='Top-level parser')
    
    # सबपार्सर बनाना
    subparsers = top_parser.add_subparsers(dest='command', required=True)

    # एक सबपार्सर जोड़ना
    subparser_a = subparsers.add_parser('command_a', help='Help for command_a')
    subparser_a.add_argument('--option', type=str, help='An option for command_a')

    # एक और सबपार्सर जोड़ना
    subparser_b = subparsers.add_parser('command_b', help='Help for command_b')
    subparser_b.add_argument('--flag', action='store_true', help='A flag for command_b')

    return top_parser, subparsers