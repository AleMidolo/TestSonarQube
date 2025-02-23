def _include_groups(self, parser_dict):
    """
    解析规范文件中的 include dict 指令。
    """
    include_dict = parser_dict.get('include', {})
    for group_name, group_items in include_dict.items():
        if isinstance(group_items, list):
            for item in group_items:
                self._process_include_item(group_name, item)
        else:
            self._process_include_item(group_name, group_items)

def _process_include_item(self, group_name, item):
    # 处理每个包含项的逻辑
    pass