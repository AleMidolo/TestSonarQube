def make_parsers():
    """
    शीर्ष-स्तरीय पार्सर और इसके उप-पार्सर बनाएं और उन्हें एक ट्यूपल के रूप में लौटाएं।
    """
    import argparse

    # मुख्य पार्सर बनाएँ
    main_parser = argparse.ArgumentParser(description='मुख्य पार्सर')
    
    # उप-पार्सर बनाएँ
    subparsers = main_parser.add_subparsers(dest='command', help='उप-पार्सर मदद')

    # एक उप-पार्सर जोड़ें
    sub_parser_a = subparsers.add_parser('command_a', help='कमांड A के लिए मदद')
    sub_parser_a.add_argument('--option', type=str, help='कमांड A के लिए विकल्प')

    # एक और उप-पार्सर जोड़ें
    sub_parser_b = subparsers.add_parser('command_b', help='कमांड B के लिए मदद')
    sub_parser_b.add_argument('--flag', action='store_true', help='कमांड B के लिए फ्लैग')

    return main_parser, subparsers