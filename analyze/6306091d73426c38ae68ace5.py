def _include_groups(self, parser_dict):
    if 'include' in parser_dict:
        for group in parser_dict['include']:
            if group in self.specs:
                parser_dict.update(self.specs[group])
            else:
                raise KeyError(f"Group '{group}' not found in specs.")
    return parser_dict