def fix_namespace_prefix_w(content):
    """
    将内容中的 "w:st=" 替换为 "w-st="。
    将默认的文本 'w:st="' 转换为 'w-st="'。
    """
    return content.replace('w:st="', 'w-st="')