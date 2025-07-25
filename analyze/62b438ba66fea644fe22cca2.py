def deep_merge_nodes(nodes):
    from ruamel.yaml.nodes import ScalarNode, MappingNode

    merged = {}
    
    for key_node, value_node in nodes:
        key = key_node.value
        
        if isinstance(value_node, MappingNode):
            if key not in merged:
                merged[key] = {}
            for sub_key_node, sub_value_node in value_node.value:
                sub_key = sub_key_node.value
                merged[key][sub_key] = sub_value_node
        else:
            merged[key] = value_node

    result = []
    for key, value in merged.items():
        if isinstance(value, dict):
            mapping_node = MappingNode(tag='tag:yaml.org,2002:map', value=[
                (ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in value.items()
            ])
            result.append((ScalarNode(tag='tag:yaml.org,2002:str', value=key), mapping_node))
        else:
            result.append((ScalarNode(tag='tag:yaml.org,2002:str', value=key), value))

    return result