def xml_children_as_dict(node):
    """
    将 <xml> 节点的子节点转换为一个字典，以标签名称作为键。

    这只是一个浅层转换——子节点不会被递归处理。
    """
    result = {}
    for child in node:
        if child.tag not in result:
            result[child.tag] = child.text
        else:
            if not isinstance(result[child.tag], list):
                result[child.tag] = [result[child.tag]]
            result[child.tag].append(child.text)
    return result