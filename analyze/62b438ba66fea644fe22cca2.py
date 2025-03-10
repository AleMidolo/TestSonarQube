def deep_merge_nodes(nodes):
    from ruamel.yaml.nodes import ScalarNode, MappingNode

    merged_nodes = {}

    for key, value in nodes:
        if isinstance(key, ScalarNode):
            key_value = key.value
            if key_value in merged_nodes:
                existing_value = merged_nodes[key_value]
                if isinstance(existing_value, MappingNode) and isinstance(value, MappingNode):
                    # Merge the MappingNodes
                    existing_mapping = {k.value: v for k, v in existing_value.value}
                    new_mapping = {k.value: v for k, v in value.value}
                    merged_mapping = {**existing_mapping, **new_mapping}
                    merged_nodes[key_value] = MappingNode(
                        tag=existing_value.tag,
                        value=[(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in merged_mapping.items()]
                    )
                else:
                    # If not both MappingNodes, the last value prevails
                    merged_nodes[key_value] = value
            else:
                merged_nodes[key_value] = value

    return [(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in merged_nodes.items()]