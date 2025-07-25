import argparse

def make_parsers():
    """
    शीर्ष-स्तरीय पार्सर और इसके उप-पार्सर बनाएं और उन्हें एक ट्यूपल के रूप में लौटाएं।
    """
    # शीर्ष-स्तरीय पार्सर बनाएं
    parser = argparse.ArgumentParser(description="शीर्ष-स्तरीय पार्सर")
    
    # उप-पार्सर बनाएं
    subparsers = parser.add_subparsers(dest="command", help="उप-पार्सर कमांड")
    
    # पहला उप-पार्सर
    parser_a = subparsers.add_parser('command_a', help='कमांड A के लिए उप-पार्सर')
    parser_a.add_argument('--option_a', type=int, help='कमांड A के लिए विकल्प')
    
    # दूसरा उप-पार्सर
    parser_b = subparsers.add_parser('command_b', help='कमांड B के लिए उप-पार्सर')
    parser_b.add_argument('--option_b', type=str, help='कमांड B के लिए विकल्प')
    
    return parser, subparsers