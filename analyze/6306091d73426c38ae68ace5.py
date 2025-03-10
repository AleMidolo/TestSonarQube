def _include_groups(self, parser_dict):
    """
    解析规范文件中的 include dict 指令。
    """
    if 'include' not in parser_dict:
        return parser_dict
    
    include_dict = parser_dict['include']
    if not isinstance(include_dict, dict):
        raise ValueError("'include' must be a dictionary")
    
    for key, value in include_dict.items():
        if key in parser_dict:
            if isinstance(parser_dict[key], dict) and isinstance(value, dict):
                parser_dict[key].update(value)
            else:
                parser_dict[key] = value
        else:
            parser_dict[key] = value
    
    del parser_dict['include']
    return parser_dict