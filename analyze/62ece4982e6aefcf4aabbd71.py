import re

def regex_dict(item):
    """
    将 *.cpp 键转换为正则表达式键

    给定一个字典，其中的键是带有通配符的文件名，仅将这些键转换为等效的正则表达式，同时保持值不变。

    参数：
        item：需要转换的字典
    返回值：
        一个键已转换为正则表达式的字典

    示例：
    ules = {
        '*.cpp':
            {'a': 'arf', 'b': 'bark', 'c': 'coo'},
        '*.h':
            {'h': 'help'}
    }
    regex_keys = regex_dict(rules)
    """
    regex_item = {}
    for key, value in item.items():
        # Convert wildcard to regex
        regex_key = re.escape(key).replace(r'\*', '.*')
        regex_item[regex_key] = value
    return regex_item