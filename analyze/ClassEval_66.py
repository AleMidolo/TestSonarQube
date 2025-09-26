class NumericEntityUnescaper:
    def __init__(self):
        pass

    def replace(self, string):
        out = []
        pos = 0
        length = len(string)

        while pos < length - 2:
            if self.is_numeric_entity(string, pos, length):
                entity_value, end = self.extract_entity_value(string, pos, length)
                if entity_value is not None:
                    out.append(chr(entity_value))
                    pos = end + 1
                    continue

            out.append(string[pos])
            pos += 1

        return ''.join(out)

    def is_numeric_entity(self, string, pos, length):
        return string[pos] == '&' and string[pos + 1] == '#' and pos + 2 < length

    def extract_entity_value(self, string, pos, length):
        start = pos + 2
        is_hex = False
        first_char = string[start]

        if first_char in ('x', 'X'):
            start += 1
            is_hex = True

        if start == length:
            return None, pos

        end = start
        while end < length and self.is_hex_char(string[end]):
            end += 1

        if end < length and string[end] == ';':
            try:
                entity_value = int(string[start:end], 16 if is_hex else 10)
                return entity_value, end
            except ValueError:
                return None, pos

        return None, pos

    @staticmethod
    def is_hex_char(char):
        return char.isdigit() or ('a' <= char.lower() <= 'f')