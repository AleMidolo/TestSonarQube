from ruamel.yaml.nodes import ScalarNode, MappingNode

def deep_merge_nodes(nodes):
    merged_nodes = {}
    
    for key, value in nodes:
        if key.value in merged_nodes:
            existing_value = merged_nodes[key.value]
            if isinstance(existing_value, MappingNode) and isinstance(value, MappingNode):
                # Merge the MappingNodes
                merged_mapping = {}
                for sub_key, sub_value in existing_value.value:
                    merged_mapping[sub_key.value] = sub_value
                for sub_key, sub_value in value.value:
                    merged_mapping[sub_key.value] = sub_value
                # Convert back to list of tuples
                merged_value = [(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v] for k, v in merged_mapping.items()]
                merged_nodes[key.value] = MappingNode(tag='tag:yaml.org,2002:map', value=merged_value)
            else:
                # If not both MappingNodes, the last value prevails
                merged_nodes[key.value] = value
        else:
            merged_nodes[key.value] = value
    
    # Convert the merged_nodes dictionary back to a list of tuples
    result = [(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in merged_nodes.items()]
    return result