def deep_merge_nodes(nodes):
    from ruamel.yaml.nodes import ScalarNode, MappingNode

    merged = {}

    for key, value in nodes:
        key_value = key.value
        if key_value not in merged:
            merged[key_value] = value
        else:
            existing_value = merged[key_value]
            if isinstance(existing_value, MappingNode) and isinstance(value, MappingNode):
                # Merge the MappingNode values
                for sub_key, sub_value in value.value:
                    existing_value.value.append((sub_key, sub_value))
            else:
                # If they are not both MappingNodes, the last one wins
                merged[key_value] = value

    result = []
    for key, value in merged.items():
        result.append((ScalarNode(tag='tag:yaml.org,2002:str', value=key), value))

    return result