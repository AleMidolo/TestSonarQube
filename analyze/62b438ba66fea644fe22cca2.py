from ruamel.yaml.nodes import ScalarNode, MappingNode

def deep_merge_nodes(nodes):
    """
    Dado un conjunto de datos de configuración anidada de borgmatic como una lista de tuplas en la forma de:

        (
            ruamel.yaml.nodes.ScalarNode como clave,
            ruamel.yaml.nodes.MappingNode u otro tipo de nodo como valor,
        ),

    ... fusionar profundamente cualquier valor de nodo correspondiente a claves duplicadas y devolver el resultado. Si hay claves en conflicto con valores que no son de tipo `MappingNode` (por ejemplo, enteros o cadenas de texto), el último de los valores prevalece.
    """
    merged_nodes = {}

    for key, value in nodes:
        if key.value in merged_nodes:
            existing_value = merged_nodes[key.value]
            if isinstance(existing_value, MappingNode) and isinstance(value, MappingNode):
                # Merge the MappingNodes
                existing_items = {item[0].value: item[1] for item in existing_value.value}
                for item_key, item_value in value.value:
                    if item_key.value in existing_items:
                        if isinstance(existing_items[item_key.value], MappingNode) and isinstance(item_value, MappingNode):
                            # Recursively merge nested MappingNodes
                            merged_items = deep_merge_nodes([
                                (item_key, existing_items[item_key.value]),
                                (item_key, item_value),
                            ])
                            existing_items[item_key.value] = merged_items[0][1]
                        else:
                            # Overwrite non-MappingNode values
                            existing_items[item_key.value] = item_value
                    else:
                        existing_items[item_key.value] = item_value
                # Convert the merged items back to a list of tuples
                merged_value = MappingNode(
                    tag=existing_value.tag,
                    value=[(ScalarNode(tag=item_key.tag, value=item_key.value), item_value) for item_key, item_value in existing_items.items()],
                )
                merged_nodes[key.value] = merged_value
            else:
                # Overwrite non-MappingNode values
                merged_nodes[key.value] = value
        else:
            merged_nodes[key.value] = value

    # Convert the merged dictionary back to a list of tuples
    return [(ScalarNode(tag='tag:yaml.org,2002:str', value=key), value) for key, value in merged_nodes.items()]