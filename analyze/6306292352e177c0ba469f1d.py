from typing import Tuple, Set
import re

def find_tags(text: str, replacer: callable = None) -> Tuple[Set, str]:
    """
    在文本中查找标签。

    尽量忽略代码块中的标签。

    可选地，如果传入了一个 “replacer”，则会使用调用该 replacer 函数（参数为标签单词）的返回值来替换该标签单词。

    返回一个包含标签的集合以及原始文本或替换后的文本。
    """
    # 正则表达式匹配标签，忽略代码块
    tag_pattern = r'(?<!`)(#\w+)(?!`)'
    code_block_pattern = r'`.*?`'
    
    # 找到所有代码块并替换为占位符
    code_blocks = re.findall(code_block_pattern, text)
    text_without_code = re.sub(code_block_pattern, '', text)
    
    # 查找标签
    tags = set(re.findall(tag_pattern, text_without_code))
    
    # 替换标签
    if replacer:
        for tag in tags:
            text_without_code = text_without_code.replace(tag, replacer(tag))
    
    return tags, text_without_code