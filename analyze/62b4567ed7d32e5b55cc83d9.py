def deep_merge_nodes(nodes):
    from ruamel.yaml.nodes import ScalarNode, MappingNode

    def merge_dicts(dict1, dict2):
        for key, value in dict2.items():
            if key in dict1:
                if isinstance(dict1[key], MappingNode) and isinstance(value, MappingNode):
                    dict1[key] = merge_dicts(dict1[key], value)
                else:
                    dict1[key] = value
            else:
                dict1[key] = value
        return dict1

    merged = {}
    for key_node, value_node in nodes:
        key = key_node.value
        if isinstance(value_node, MappingNode):
            if key in merged:
                merged[key] = merge_dicts(merged[key], value_node)
            else:
                merged[key] = value_node
        else:
            merged[key] = value_node

    result = []
    for key, value in merged.items():
        result.append((ScalarNode(tag='tag:yaml.org,2002:str', value=key), value))
    
    return result