import argparse

def make_parsers():
    """
    शीर्ष-स्तरीय पार्सर और इसके उप-पार्सर बनाएं और उन्हें एक ट्यूपल के रूप में लौटाएं।
    """
    # शीर्ष-स्तरीय पार्सर बनाएं
    top_parser = argparse.ArgumentParser(description="शीर्ष-स्तरीय पार्सर")
    
    # उप-पार्सर बनाएं
    subparsers = top_parser.add_subparsers(title="उप-पार्सर", dest="subcommand")
    
    # पहला उप-पार्सर
    parser_a = subparsers.add_parser('command_a', help='कमांड ए के लिए मदद')
    parser_a.add_argument('--option_a', type=int, help='कमांड ए के लिए विकल्प')
    
    # दूसरा उप-पार्सर
    parser_b = subparsers.add_parser('command_b', help='कमांड बी के लिए मदद')
    parser_b.add_argument('--option_b', type=str, help='कमांड बी के लिए विकल्प')
    
    return top_parser, subparsers