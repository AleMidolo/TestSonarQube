import argparse

def make_parsers():
    """
    एक शीर्ष-स्तरीय (top-level) पार्सर और उसके सबपार्सर बनाएं और उन्हें एक ट्यूपल के रूप में लौटाएं।
    """
    # शीर्ष-स्तरीय पार्सर बनाएं
    top_parser = argparse.ArgumentParser(description="शीर्ष-स्तरीय पार्सर")
    
    # सबपार्सर बनाएं
    subparsers = top_parser.add_subparsers(title="सबपार्सर", dest="command")
    
    # पहला सबपार्सर
    parser_a = subparsers.add_parser('command_a', help='कमांड ए के लिए सहायता')
    parser_a.add_argument('--option_a', type=int, help='कमांड ए के लिए विकल्प')
    
    # दूसरा सबपार्सर
    parser_b = subparsers.add_parser('command_b', help='कमांड बी के लिए सहायता')
    parser_b.add_argument('--option_b', type=str, help='कमांड बी के लिए विकल्प')
    
    return top_parser, subparsers