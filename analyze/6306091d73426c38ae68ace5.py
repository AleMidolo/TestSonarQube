def _include_groups(self, parser_dict):
    """
    解析规范文件中的 include dict 指令。
    """
    include_dict = parser_dict.get('include', {})
    for group_name, group_content in include_dict.items():
        if isinstance(group_content, dict):
            self._process_group(group_name, group_content)
        else:
            raise ValueError(f"Group content for '{group_name}' must be a dictionary.")