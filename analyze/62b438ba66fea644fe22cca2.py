def deep_merge_nodes(nodes):
    from ruamel.yaml.nodes import ScalarNode, MappingNode

    merged = {}

    for key, value in nodes:
        key_value = key.value
        if key_value not in merged:
            merged[key_value] = value
        else:
            existing_value = merged[key_value]
            if isinstance(existing_value, MappingNode) and isinstance(value, MappingNode):
                existing_mapping = {k.value: v for k, v in existing_value.value}
                new_mapping = {k.value: v for k, v in value.value}
                existing_mapping.update(new_mapping)
                merged[key_value] = MappingNode(tag='tag:yaml.org,2002:map', value=[
                    (ScalarNode(tag='tag:yaml.org,2002:str', value=k), ScalarNode(tag='tag:yaml.org,2002:int', value=str(v)))
                    for k, v in existing_mapping.items()
                ])
            else:
                merged[key_value] = value

    return [(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in merged.items()]