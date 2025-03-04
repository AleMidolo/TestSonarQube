def xml_children_as_dict(node):
    """
    将 <xml> 节点的子节点转换为一个字典，以标签名称作为键。
    
    这只是一个浅层转换——子节点不会被递归处理。
    """
    result = {}
    for child in node:
        # 跳过注释等非元素节点
        if not hasattr(child, 'tag'):
            continue
        # 使用标签名作为键,节点对象作为值
        result[child.tag] = child
    return result