def _include_groups(self, parser_dict):
    """
    解析规范文件中的 include dict 指令。
    """
    if 'include' in parser_dict:
        for group in parser_dict['include']:
            if group in parser_dict:
                parser_dict.update(parser_dict[group])
            else:
                raise ValueError(f"Group '{group}' not found in parser_dict")
    return parser_dict