def make_parsers():
    """
    Crea un analizador de nivel superior y sus subanalizadores, y devuélvalos como una tupla.
    """
    class HighLevelParser:
        def parse(self, data):
            # Lógica para analizar datos a un nivel alto
            return f"High-level parsing of {data}"

    class SubParserA:
        def parse(self, data):
            # Lógica para analizar datos en un subnivel A
            return f"SubParserA parsing of {data}"

    class SubParserB:
        def parse(self, data):
            # Lógica para analizar datos en un subnivel B
            return f"SubParserB parsing of {data}"

    high_level_parser = HighLevelParser()
    sub_parser_a = SubParserA()
    sub_parser_b = SubParserB()

    return (high_level_parser, sub_parser_a, sub_parser_b)