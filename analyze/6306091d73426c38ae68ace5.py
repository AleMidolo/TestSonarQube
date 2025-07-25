def _include_groups(self, parser_dict):
    """
    解析规范文件中的 include dict 指令。
    """
    if 'include' in parser_dict:
        for group in parser_dict['include']:
            if group in self.groups:
                self.groups[group].update(parser_dict['include'][group])
            else:
                self.groups[group] = parser_dict['include'][group]