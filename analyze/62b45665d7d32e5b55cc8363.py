def make_parsers():
    """
    Crea un analizador de nivel superior y sus subanalizadores, y devuélvalos como una tupla.
    """
    class HighLevelParser:
        def parse(self, data):
            # Implementación del análisis de nivel superior
            return f"HighLevelParser: {data}"

    class SubParserA:
        def parse(self, data):
            # Implementación del subanálisis A
            return f"SubParserA: {data}"

    class SubParserB:
        def parse(self, data):
            # Implementación del subanálisis B
            return f"SubParserB: {data}"

    high_level_parser = HighLevelParser()
    sub_parser_a = SubParserA()
    sub_parser_b = SubParserB()

    return (high_level_parser, sub_parser_a, sub_parser_b)