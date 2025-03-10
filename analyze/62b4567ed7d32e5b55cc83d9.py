from ruamel.yaml.nodes import ScalarNode, MappingNode

def deep_merge_nodes(nodes):
    """
    Dato una struttura configuratione di struttura data annidata di borgmatic sotto forma di una lista di tuple nel formato:

        (
            ruamel.yaml.nodes.ScalarNode come chiave,
            ruamel.yaml.nodes.MappingNode o un altro tipo di Node come valore,
        ),

    ... esegui una fusione profonda (deep merge) dei valori dei nodi corrispondenti a chiavi duplicate e restituisci il risultato. Se ci sono chiavi in conflitto con valori non di tipo `MappingNode` (ad esempio, interi o stringhe), l'ultimo dei valori prevale.
    """
    merged_nodes = {}
    
    for key, value in nodes:
        if key.value in merged_nodes:
            existing_value = merged_nodes[key.value]
            if isinstance(existing_value, MappingNode) and isinstance(value, MappingNode):
                # Deep merge the MappingNodes
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