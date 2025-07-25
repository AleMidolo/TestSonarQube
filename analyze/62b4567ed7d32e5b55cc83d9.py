def deep_merge_nodes(nodes):
    from ruamel.yaml.nodes import MappingNode, ScalarNode

    merged_nodes = {}

    for key, value in nodes:
        if isinstance(key, ScalarNode):
            key_value = key.value
            if key_value in merged_nodes:
                existing_value = merged_nodes[key_value]
                if isinstance(existing_value, MappingNode) and isinstance(value, MappingNode):
                    # Deep merge the MappingNodes
                    existing_mapping = {k.value: v for k, v in existing_value.value}
                    new_mapping = {k.value: v for k, v in value.value}
                    for k, v in new_mapping.items():
                        if k in existing_mapping and isinstance(existing_mapping[k], MappingNode) and isinstance(v, MappingNode):
                            # Recursively merge nested MappingNodes
                            existing_mapping[k] = deep_merge_nodes([(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v])
                        else:
                            # Overwrite or add new key-value pair
                            existing_mapping[k] = v
                    merged_nodes[key_value] = MappingNode(
                        tag='tag:yaml.org,2002:map',
                        value=[(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in existing_mapping.items()]
                    )
                else:
                    # If either value is not a MappingNode, the last value prevails
                    merged_nodes[key_value] = value
            else:
                # Add new key-value pair
                merged_nodes[key_value] = value
        else:
            # If the key is not a ScalarNode, treat it as a unique key
            merged_nodes[key] = value

    # Convert the merged dictionary back to a list of tuples
    return [(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v] if isinstance(k, str) else (k, v) for k, v in merged_nodes.items()]