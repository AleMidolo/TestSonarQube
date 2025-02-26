def xml_children_as_dict(node):
    """
    将 <xml> 节点的子节点转换为一个字典，以标签名称作为键。

    这只是一个浅层转换——子节点不会被递归处理。
    """
    return {child.tag: child for child in node}