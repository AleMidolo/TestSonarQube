def regex_dict(item):
    """
    将 *.cpp 键转换为正则表达式键

    给定一个字典，其中的键是带有通配符的文件名，仅将这些键转换为等效的正则表达式，同时保持值不变。

    参数：
        item：需要转换的字典
    返回值：
        一个键已转换为正则表达式的字典
    """
    import re
    
    # 创建新字典存储结果
    result = {}
    
    # 遍历原字典的键值对
    for key, value in item.items():
        # 转换通配符为正则表达式
        # 将 * 替换为 .*
        # 将 . 替换为 \.
        # 在开头和结尾添加 ^ 和 $
        regex_key = '^' + re.escape(key).replace('\\*', '.*') + '$'
        
        # 将转换后的正则表达式键和原值添加到结果字典
        result[regex_key] = value
        
    return result