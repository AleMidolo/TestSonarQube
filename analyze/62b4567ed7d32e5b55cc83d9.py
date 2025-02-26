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
                # Deep merge the MappingNodes
                for sub_key, sub_value in value.value:
                    existing_value.value.append((sub_key, sub_value))
                # Remove duplicates in the merged MappingNode
                unique_mapping = {}
                for sub_key, sub_value in existing_value.value:
                    unique_mapping[sub_key.value] = sub_value
                existing_value.value = list(unique_mapping.items())
            else:
                # If they are not both MappingNodes, the last one wins
                merged[key_value] = value

    return [(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in merged.items()]