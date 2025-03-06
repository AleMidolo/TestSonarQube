import argparse

def make_parsers():
    """
    एक शीर्ष-स्तरीय (top-level) पार्सर और उसके सबपार्सर बनाएं और उन्हें एक ट्यूपल के रूप में लौटाएं।
    """
    # शीर्ष-स्तरीय पार्सर बनाएं
    top_parser = argparse.ArgumentParser(description="शीर्ष-स्तरीय पार्सर")
    
    # सबपार्सर बनाएं
    subparsers = top_parser.add_subparsers(title="कमांड", dest="command")
    
    # पहला सबपार्सर
    parser_a = subparsers.add_parser("command_a", help="कमांड A के लिए मदद")
    parser_a.add_argument("arg1", type=str, help="कमांड A के लिए पहला तर्क")
    
    # दूसरा सबपार्सर
    parser_b = subparsers.add_parser("command_b", help="कमांड B के लिए मदद")
    parser_b.add_argument("arg2", type=int, help="कमांड B के लिए पहला तर्क")
    
    return top_parser, subparsers