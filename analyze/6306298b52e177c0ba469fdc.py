def xml_children_as_dict(node):
    """
    将 <xml> 节点的子节点转换为一个字典，以标签名称作为键。

    这只是一个浅层转换——子节点不会被递归处理。
    """
    result = {}
    for child in node:
        tag = child.tag
        if tag in result:
            if isinstance(result[tag], list):
                result[tag].append(child.text)
            else:
                result[tag] = [result[tag], child.text]
        else:
            result[tag] = child.text
    return result