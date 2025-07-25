def deep_merge_nodes(nodes):
    from ruamel.yaml.nodes import MappingNode, ScalarNode

    merged_nodes = {}

    for key, value in nodes:
        if key.value in merged_nodes:
            existing_value = merged_nodes[key.value]
            if isinstance(existing_value, MappingNode) and isinstance(value, MappingNode):
                # Merge the MappingNodes
                existing_mapping = {k.value: v for k, v in existing_value.value}
                new_mapping = {k.value: v for k, v in value.value}
                # Deep merge the mappings
                for k, v in new_mapping.items():
                    if k in existing_mapping and isinstance(existing_mapping[k], MappingNode) and isinstance(v, MappingNode):
                        # Recursively merge nested MappingNodes
                        merged_mapping = deep_merge_nodes([(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v)])
                        existing_mapping[k] = merged_mapping[0][1]
                    else:
                        # Overwrite or add new key-value pair
                        existing_mapping[k] = v
                # Convert back to list of tuples
                merged_nodes[key.value] = MappingNode(
                    tag=existing_value.tag,
                    value=[(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in existing_mapping.items()]
                )
            else:
                # If either value is not a MappingNode, the last value prevails
                merged_nodes[key.value] = value
        else:
            # Add new key-value pair
            merged_nodes[key.value] = value

    # Convert the merged dictionary back to a list of tuples
    return [(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in merged_nodes.items()]