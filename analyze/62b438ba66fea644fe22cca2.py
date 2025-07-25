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

                # Create a dictionary to hold the merged key-value pairs
                merged_dict = {}
                for k_node, v_node in existing_value:
                    merged_dict[k_node.value] = (k_node, v_node)

                for k_node, v_node in new_value:
                    k = k_node.value
                    if k in merged_dict:
                        existing_k_node, existing_v_node = merged_dict[k]
                        if isinstance(existing_v_node, MappingNode) and isinstance(v_node, MappingNode):
                            # Recursively merge nested MappingNodes
                            merged_dict[k] = (existing_k_node, deep_merge_nodes([(existing_k_node, existing_v_node), (k_node, v_node)])[0][1])
                        else:
                            # Overwrite with the new value if not a MappingNode
                            merged_dict[k] = (k_node, v_node)
                    else:
                        merged_dict[k] = (k_node, v_node)

                # Convert the merged dictionary back to a list of tuples
                merged_value = list(merged_dict.values())
                merged_nodes[key] = MappingNode(existing_value_node.tag, merged_value)
            else:
                # If either value is not a MappingNode, the last value wins
                merged_nodes[key] = value_node
        else:
            merged_nodes[key] = value_node

    # Convert the merged dictionary back to a list of tuples
    result = [(ScalarNode(key_node.tag, key), value_node) for key, value_node in merged_nodes.items()]
    return result