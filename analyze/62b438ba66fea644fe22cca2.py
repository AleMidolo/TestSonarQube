def deep_merge_nodes(nodes):
    from ruamel.yaml.nodes import MappingNode, ScalarNode

    merged_nodes = {}

    for key_node, value_node in nodes:
        key = key_node.value
        if key in merged_nodes:
            existing_value_node = merged_nodes[key]
            if isinstance(existing_value_node, MappingNode) and isinstance(value_node, MappingNode):
                # Deep merge the MappingNodes
                existing_value = existing_value_node.value
                new_value = value_node.value
                merged_value = deep_merge_nodes(existing_value + new_value)
                merged_nodes[key] = MappingNode(
                    tag=existing_value_node.tag,
                    value=merged_value,
                    start_mark=existing_value_node.start_mark,
                    end_mark=existing_value_node.end_mark,
                    flow_style=existing_value_node.flow_style,
                )
            else:
                # If either value is not a MappingNode, the last value wins
                merged_nodes[key] = value_node
        else:
            merged_nodes[key] = value_node

    # Convert the merged dictionary back to a list of tuples
    return [(ScalarNode(tag='tag:yaml.org,2002:str', value=key), value_node) for key, value_node in merged_nodes.items()]