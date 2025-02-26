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
    sub_parser1 = subparsers.add_parser('command1', help='Help for command1')
    sub_parser1.add_argument('--option1', type=str, help='Option 1 for command1')

    # दूसरे सबपार्सर को जोड़ना
    sub_parser2 = subparsers.add_parser('command2', help='Help for command2')
    sub_parser2.add_argument('--option2', type=int, help='Option 2 for command2')

    return top_parser, subparsers