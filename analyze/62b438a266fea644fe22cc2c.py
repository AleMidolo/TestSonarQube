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
    sub_parser1 = subparsers.add_parser('command1', help='कमांड 1 मदद')
    sub_parser1.add_argument('--option1', type=str, help='विकल्प 1')

    # दूसरे उप-पार्सर जोड़ें
    sub_parser2 = subparsers.add_parser('command2', help='कमांड 2 मदद')
    sub_parser2.add_argument('--option2', type=int, help='विकल्प 2')

    return main_parser, subparsers