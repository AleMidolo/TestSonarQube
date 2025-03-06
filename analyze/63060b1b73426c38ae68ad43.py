def extend_cli(self, root_subparsers):
    """
    मुख्य एंट्री पॉइंट में स्पेक CLI विकल्प जोड़ता है।

    :param subparser: वह सबपार्सर ऑब्जेक्ट जिसे विस्तारित करना है।
    """
    spec_parser = root_subparsers.add_parser('spec', help='स्पेक संबंधित कमांड')
    spec_parser.add_argument('--option1', help='स्पेक विकल्प 1')
    spec_parser.add_argument('--option2', help='स्पेक विकल्प 2')