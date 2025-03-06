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
                merged_value = deep_merge_nodes(existing_value.value + value.value)
                merged_nodes[key.value] = MappingNode(existing_value.tag, merged_value)
            else:
                # If not both MappingNodes, the last value prevails
                merged_nodes[key.value] = value
        else:
            merged_nodes[key.value] = value

    # Convert the merged dictionary back to a list of tuples
    result = [(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in merged_nodes.items()]
    return result