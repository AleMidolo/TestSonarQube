def _include_groups(self, parser_dict):
    """
    Risolve la direttiva "include dict" nei file di specifica
    """
    if 'include' in parser_dict:
        include_files = parser_dict['include']
        for include_file in include_files:
            with open(include_file, 'r') as f:
                included_dict = self._parse_file(f)
                parser_dict.update(included_dict)
    return parser_dict

def _parse_file(self, file):
    # Dummy implementation for parsing a file into a dictionary
    # Replace with actual parsing logic
    return {}  # Return an empty dictionary for now