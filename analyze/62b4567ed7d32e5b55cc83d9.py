from ruamel.yaml.nodes import ScalarNode, MappingNode

def deep_merge_nodes(nodes):
    """
    Dato una struttura configuratione di struttura data annidata di borgmatic sotto forma di una lista di tuple nel formato:

        (
            ruamel.yaml.nodes.ScalarNode come chiave,
            ruamel.yaml.nodes.MappingNode o un altro tipo di Node come valore,
        ),

    ... esegui una fusione profonda (deep merge) dei valori dei nodi corrispondenti a chiavi duplicate e restituisci il risultato. Se ci sono chiavi in conflitto con valori non di tipo `MappingNode` (ad esempio, interi o stringhe), l'ultimo dei valori prevale.

    Ad esempio, dati i seguenti valori dei nodi:

        [
            (
                ScalarNode(tag='tag:yaml.org,2002:str', value='retention'),
                MappingNode(tag='tag:yaml.org,2002:map', value=[
                    (
                        ScalarNode(tag='tag:yaml.org,2002:str', value='keep_hourly'),
                        ScalarNode(tag='tag:yaml.org,2002:int', value='24')
                    ),
                    (
                        ScalarNode(tag='tag:yaml.org,2002:str', value='keep_daily'),
                        ScalarNode(tag='tag:yaml.org,2002:int', value='7')
                    ),
                ]),
            ),
            (
                ScalarNode(tag='tag:yaml.org,2002:str', value='retention'),
                MappingNode(tag='tag:yaml.org,2002:map', value=[
                    (
                        ScalarNode(tag='tag:yaml.org,2002:str', value='keep_daily'),
                        ScalarNode(tag='tag:yaml.org,2002:int', value='5')
                    ),
                ]),
            ),
        ]

    ... il risultato restituito sarebbe:

        [
            (
                ScalarNode(tag='tag:yaml.org,2002:str', value='retention'),
                MappingNode(tag='tag:yaml.org,2002:map', value=[
                    (
                        ScalarNode(tag='tag:yaml.org,2002:str', value='keep_hourly'),
                        ScalarNode(tag='tag:yaml.org,2002:int', value='24')
                    ),
                    (
                        ScalarNode(tag='tag:yaml.org,2002:str', value='keep_daily'),
                        ScalarNode(tag='tag:yaml.org,2002:int', value='5')
                    ),
                ]),
            ),
        ]

    Lo scopo di una fusione profonda come questa è supportare, ad esempio, la fusione di un file di configurazione borgmatic in un altro per il riutilizzo, in modo che una sezione di configurazione ("retention", ecc.) non sostituisca completamente la sezione corrispondente in un file unito.
    """
    merged = {}
    
    for key_node, value_node in nodes:
        key = key_node.value
        
        if key not in merged:
            merged[key] = value_node
        else:
            if isinstance(merged[key], MappingNode) and isinstance(value_node, MappingNode):
                # Deep merge the mapping nodes
                for sub_key_node, sub_value_node in value_node.value:
                    merged_value = merged[key].value
                    merged_value_dict = {k.value: v for k, v in merged_value}
                    merged_value_dict[sub_key_node.value] = sub_value_node
                    merged[key] = MappingNode(tag='tag:yaml.org,2002:map', value=[
                        (ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in merged_value_dict.items()
                    ])
            else:
                # If there's a conflict, take the last value
                merged[key] = value_node

    return [(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in merged.items()]