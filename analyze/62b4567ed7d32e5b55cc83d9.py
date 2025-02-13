def deep_merge_nodes(nodes):
    from ruamel.yaml.nodes import ScalarNode, MappingNode

    merged = {}

    for key_node, value_node in nodes:
        key = key_node.value
        if key not in merged:
            merged[key] = value_node
        else:
            if isinstance(merged[key], MappingNode) and isinstance(value_node, MappingNode):
                for sub_key_node, sub_value_node in value_node.value:
                    merged[key].value.append((sub_key_node, sub_value_node))
            else:
                merged[key] = value_node

    result = []
    for key, value in merged.items():
        result.append((ScalarNode(tag='tag:yaml.org,2002:str', value=key), value))

    return result