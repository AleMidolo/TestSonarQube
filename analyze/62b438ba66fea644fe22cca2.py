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
                # Merge the two MappingNodes
                for sub_key_node, sub_value_node in value_node.value:
                    existing_value.value.append((sub_key_node, sub_value_node))
            else:
                # If there's a conflict, take the last value
                merged[key] = value_node

    return [(ScalarNode(tag='tag:yaml.org,2002:str', value=key), value) for key, value in merged.items()]