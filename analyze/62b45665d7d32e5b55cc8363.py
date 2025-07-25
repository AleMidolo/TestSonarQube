def make_parsers():
    """
    एक शीर्ष-स्तरीय (top-level) पार्सर और उसके सबपार्सर बनाएं और उन्हें एक ट्यूपल के रूप में लौटाएं।
    """
    import argparse

    # शीर्ष-स्तरीय पार्सर बनाना
    top_parser = argparse.ArgumentParser(description='Top-level parser')
    
    # सबपार्सर बनाना
    subparsers = top_parser.add_subparsers(dest='command', help='Sub-command help')

    # एक सबपार्सर जोड़ना
    sub_parser_a = subparsers.add_parser('command_a', help='Command A help')
    sub_parser_a.add_argument('--option', type=str, help='Option for command A')

    # एक और सबपार्सर जोड़ना
    sub_parser_b = subparsers.add_parser('command_b', help='Command B help')
    sub_parser_b.add_argument('--flag', action='store_true', help='Flag for command B')

    return top_parser, subparsers