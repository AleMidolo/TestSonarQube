def deep_merge_nodes(nodes):
    from collections import defaultdict
    from ruamel.yaml.nodes import ScalarNode, MappingNode

    merged_nodes = defaultdict(list)

    # Group nodes by their key
    for key, value in nodes:
        merged_nodes[key].append(value)

    result = []
    for key, values in merged_nodes.items():
        if len(values) == 1:
            result.append((key, values[0]))
        else:
            # Merge MappingNodes deeply
            merged_value = values[0]
            for value in values[1:]:
                if isinstance(merged_value, MappingNode) and isinstance(value, MappingNode):
                    # Create a dictionary to hold the merged content
                    merged_dict = {}
                    for k, v in merged_value.value:
                        merged_dict[k.value] = v
                    for k, v in value.value:
                        if k.value in merged_dict:
                            if isinstance(merged_dict[k.value], MappingNode) and isinstance(v, MappingNode):
                                # Recursively merge nested MappingNodes
                                merged_dict[k.value] = deep_merge_nodes([(k, merged_dict[k.value]), (k, v)])[0][1]
                            else:
                                # Overwrite with the new value
                                merged_dict[k.value] = v
                        else:
                            merged_dict[k.value] = v
                    # Convert the dictionary back to a list of tuples
                    merged_value = MappingNode(
                        tag=merged_value.tag,
                        value=[(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in merged_dict.items()]
                    )
                else:
                    # If not both MappingNodes, the last value prevails
                    merged_value = value
            result.append((key, merged_value))

    return result