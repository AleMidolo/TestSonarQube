import argparse

def make_parsers():
    """
    शीर्ष-स्तरीय पार्सर और इसके उप-पार्सर बनाएं और उन्हें एक ट्यूपल के रूप में लौटाएं।
    """
    # शीर्ष-स्तरीय पार्सर बनाएं
    parser = argparse.ArgumentParser(description="शीर्षक स्तर का पार्सर")
    
    # उप-पार्सर बनाएं
    subparsers = parser.add_subparsers(dest="command", help="उप-कमांड")
    
    # उप-पार्सर 1
    parser_a = subparsers.add_parser('command_a', help='कमांड ए के लिए मदद')
    parser_a.add_argument('--option_a', type=str, help='कमांड ए के लिए विकल्प')
    
    # उप-पार्सर 2
    parser_b = subparsers.add_parser('command_b', help='कमांड बी के लिए मदद')
    parser_b.add_argument('--option_b', type=int, help='कमांड बी के लिए विकल्प')
    
    return parser, subparsers