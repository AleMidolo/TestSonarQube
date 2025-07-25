def _include_groups(self, parser_dict):
    """
    解析规范文件中的 include dict 指令。
    """
    if 'include' in parser_dict:
        include_dict = parser_dict['include']
        for key, value in include_dict.items():
            if key in parser_dict:
                if isinstance(parser_dict[key], list) and isinstance(value, list):
                    parser_dict[key].extend(value)
                elif isinstance(parser_dict[key], dict) and isinstance(value, dict):
                    parser_dict[key].update(value)
                else:
                    parser_dict[key] = value
            else:
                parser_dict[key] = value
    return parser_dict