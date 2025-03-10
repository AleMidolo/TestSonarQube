import argparse

def make_parsers():
    """
    शीर्ष-स्तरीय पार्सर और इसके उप-पार्सर बनाएं और उन्हें एक ट्यूपल के रूप में लौटाएं।
    """
    # शीर्ष-स्तरीय पार्सर बनाएं
    parser = argparse.ArgumentParser(description="शीर्ष-स्तरीय पार्सर")
    
    # उप-पार्सर बनाएं
    subparsers = parser.add_subparsers(dest="command", help="उप-कमांड")
    
    # पहला उप-पार्सर
    parser_a = subparsers.add_parser("command_a", help="कमांड A के लिए मदद")
    parser_a.add_argument("arg1", type=int, help="कमांड A के लिए पहला तर्क")
    
    # दूसरा उप-पार्सर
    parser_b = subparsers.add_parser("command_b", help="कमांड B के लिए मदद")
    parser_b.add_argument("arg2", type=str, help="कमांड B के लिए पहला तर्क")
    
    return parser, subparsers