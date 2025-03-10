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
                merged_mapping = {**existing_mapping, **new_mapping}
                merged_nodes[key] = MappingNode(
                    tag=existing_value_node.tag,
                    value=[(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in merged_mapping.items()]
                )
            else:
                # If not both MappingNodes, the last value prevails
                merged_nodes[key] = value_node
        else:
            merged_nodes[key] = value_node

    return [(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in merged_nodes.items()]