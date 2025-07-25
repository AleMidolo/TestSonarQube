def deep_merge_nodes(nodes):
    from ruamel.yaml.nodes import ScalarNode, MappingNode

    merged = {}

    for key_node, value_node in nodes:
        key = key_node.value
        if key not in merged:
            merged[key] = value_node
        else:
            existing_value = merged[key]
            if isinstance(existing_value, MappingNode) and isinstance(value_node, MappingNode):
                for sub_key_node, sub_value_node in value_node.value:
                    sub_key = sub_key_node.value
                    merged_value = existing_value.value.get(sub_key)
                    if merged_value is not None:
                        existing_value.value[sub_key] = sub_value_node
                    else:
                        existing_value.value[sub_key] = sub_value_node
            else:
                merged[key] = value_node

    result = []
    for key, value in merged.items():
        result.append((ScalarNode(tag='tag:yaml.org,2002:str', value=key), value))

    return result