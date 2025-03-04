def make_parsers():
    """Crea un parser di livello superiore e i suoi sottoparser e restituiscili come una tupla."""
    import argparse

    # Create main parser
    parser = argparse.ArgumentParser(description='Command line tool')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Create encode subparser
    encode_parser = subparsers.add_parser('encode', help='Encode a message')
    encode_parser.add_argument('message', help='Message to encode')
    encode_parser.add_argument('-k', '--key', help='Encryption key', required=True)
    encode_parser.add_argument('-o', '--output', help='Output file')

    # Create decode subparser 
    decode_parser = subparsers.add_parser('decode', help='Decode a message')
    decode_parser.add_argument('message', help='Message to decode')
    decode_parser.add_argument('-k', '--key', help='Decryption key', required=True)
    decode_parser.add_argument('-o', '--output', help='Output file')

    # Create generate subparser
    generate_parser = subparsers.add_parser('generate', help='Generate encryption key')
    generate_parser.add_argument('-l', '--length', type=int, default=32, help='Key length')
    generate_parser.add_argument('-o', '--output', help='Output file')

    return parser, encode_parser, decode_parser, generate_parser