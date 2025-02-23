def deep_merge_nodes(nodes):
    from ruamel.yaml.nodes import ScalarNode, MappingNode

    merged = {}

    for key_node, value_node in nodes:
        key = key_node.value
        if key not in merged:
            merged[key] = value_node
        else:
            existing_value = merged[key]
            if isinstance(existing_value, MappingNode) and isinstance(value_node, MappingNode):
                for sub_key_node, sub_value_node in value_node.value:
                    sub_key = sub_key_node.value
                    existing_value_dict = {k.value: v for k, v in existing_value.value}
                    existing_value_dict[sub_key] = sub_value_node
                    merged[key] = MappingNode(tag='tag:yaml.org,2002:map', value=[
                        (ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in existing_value_dict.items()
                    ])
            else:
                merged[key] = value_node

    return [(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in merged.items()]