def deep_merge_nodes(nodes):
    from ruamel.yaml.nodes import MappingNode, ScalarNode

    merged_nodes = {}

    for key_node, value_node in nodes:
        key = key_node.value
        if key in merged_nodes:
            existing_value_node = merged_nodes[key]
            if isinstance(existing_value_node, MappingNode) and isinstance(value_node, MappingNode):
                # Deep merge the MappingNodes
                existing_mapping = {k.value: v for k, v in existing_value_node.value}
                new_mapping = {k.value: v for k, v in value_node.value}
                for k, v in new_mapping.items():
                    if k in existing_mapping and isinstance(existing_mapping[k], MappingNode) and isinstance(v, MappingNode):
                        # Recursively merge nested MappingNodes
                        merged_nodes[key] = MappingNode(
                            tag=existing_value_node.tag,
                            value=[
                                (ScalarNode(tag='tag:yaml.org,2002:str', value=k), deep_merge_nodes([(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v)]))
                                for k, v in existing_mapping.items()
                            ] + [
                                (ScalarNode(tag='tag:yaml.org,2002:str', value=k), v)
                                for k, v in new_mapping.items()
                                if k not in existing_mapping
                            ]
                        )
                    else:
                        # Overwrite or add new key-value pairs
                        existing_mapping[k] = v
                merged_nodes[key] = MappingNode(
                    tag=existing_value_node.tag,
                    value=[(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in existing_mapping.items()]
                )
            else:
                # If either value is not a MappingNode, the last value prevails
                merged_nodes[key] = value_node
        else:
            # Add new key-value pair
            merged_nodes[key] = value_node

    return [(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in merged_nodes.items()]