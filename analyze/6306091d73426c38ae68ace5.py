def _include_groups(self, parser_dict):
    """
    Risolve la direttiva "include dict" nei file di specifica
    """
    if not isinstance(parser_dict, dict):
        return parser_dict

    for key, value in parser_dict.items():
        if isinstance(value, dict):
            if "include" in value:
                include_key = value["include"]
                if include_key in parser_dict:
                    parser_dict[key] = parser_dict[include_key]
                else:
                    raise ValueError(f"Include key '{include_key}' not found in parser_dict")
            else:
                self._include_groups(value)
        elif isinstance(value, list):
            for i, item in enumerate(value):
                if isinstance(item, dict):
                    value[i] = self._include_groups(item)

    return parser_dict