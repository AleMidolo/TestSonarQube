import re
from typing import Set, Tuple, Callable

def find_tags(text: str, replacer: Callable[[str], str] = None) -> Tuple[Set[str], str]:
    """
    在文本中查找标签。

    尽量忽略代码块中的标签。

    可选地，如果传入了一个 “replacer”，则会使用调用该 replacer 函数（参数为标签单词）的返回值来替换该标签单词。

    返回一个包含标签的集合以及原始文本或替换后的文本。
    """
    # 正则表达式匹配标签，假设标签以#开头，且不包含空格
    tag_pattern = re.compile(r'(?<!\S)#\w+')
    
    # 忽略代码块中的标签
    code_block_pattern = re.compile(r'