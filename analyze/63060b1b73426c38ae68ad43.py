def extend_cli(self, root_subparsers):
    """
    मुख्य एंट्री पॉइंट में स्पेक CLI विकल्प जोड़ता है।

    :param subparser: वह सबपार्सर ऑब्जेक्ट जिसे विस्तारित करना है।
    """
    # उदाहरण के लिए, एक नया सबपार्सर जोड़ें
    parser = root_subparsers.add_parser('example', help='यह एक उदाहरण है।')
    
    # विकल्प जोड़ें
    parser.add_argument('--option', type=str, help='एक वैकल्पिक तर्क।')
    
    # अन्य आवश्यकताएँ या तर्क जोड़ें
    parser.add_argument('required_arg', type=int, help='एक आवश्यक तर्क।')