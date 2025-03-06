def deep_merge_nodes(nodes):
    merged = {}
    for key_node, value_node in nodes:
        key = key_node.value
        if key in merged:
            if isinstance(merged[key], ruamel.yaml.nodes.MappingNode) and isinstance(value_node, ruamel.yaml.nodes.MappingNode):
                # Deep merge the MappingNodes
                existing_value = merged[key]
                new_value = value_node
                merged_value = []
                existing_dict = {k.value: v for k, v in existing_value.value}
                new_dict = {k.value: v for k, v in new_value.value}
                for k, v in existing_dict.items():
                    if k in new_dict:
                        if isinstance(v, ruamel.yaml.nodes.MappingNode) and isinstance(new_dict[k], ruamel.yaml.nodes.MappingNode):
                            # Recursively merge nested MappingNodes
                            merged_value.append((ruamel.yaml.nodes.ScalarNode(tag='tag:yaml.org,2002:str', value=k), deep_merge_nodes([(ruamel.yaml.nodes.ScalarNode(tag='tag:yaml.org,2002:str', value=k), v), (ruamel.yaml.nodes.ScalarNode(tag='tag:yaml.org,2002:str', value=k), new_dict[k])])[0][1])
                        else:
                            # Overwrite with new value
                            merged_value.append((ruamel.yaml.nodes.ScalarNode(tag='tag:yaml.org,2002:str', value=k), new_dict[k]))
                    else:
                        merged_value.append((ruamel.yaml.nodes.ScalarNode(tag='tag:yaml.org,2002:str', value=k), v))
                for k, v in new_dict.items():
                    if k not in existing_dict:
                        merged_value.append((ruamel.yaml.nodes.ScalarNode(tag='tag:yaml.org,2002:str', value=k), v))
                merged[key] = ruamel.yaml.nodes.MappingNode(tag='tag:yaml.org,2002:map', value=merged_value)
            else:
                # Overwrite with new value
                merged[key] = value_node
        else:
            merged[key] = value_node
    return [(ruamel.yaml.nodes.ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in merged.items()]