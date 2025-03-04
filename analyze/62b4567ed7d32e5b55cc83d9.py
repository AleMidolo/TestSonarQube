def deep_merge_nodes(nodes):
    result = {}
    
    # Iterate through all nodes and merge them
    for key_node, value_node in nodes:
        key = key_node.value
        
        # If key doesn't exist yet, just add it
        if key not in result:
            result[key] = (key_node, value_node)
            continue
            
        # If key exists, need to merge values
        existing_value = result[key][1]
        
        # If both nodes are mapping nodes, merge them recursively
        if (isinstance(existing_value, type(value_node)) and 
            hasattr(existing_value, 'value') and 
            hasattr(value_node, 'value')):
            
            # Create dict of existing key-value pairs
            existing_dict = {k.value: (k,v) for k,v in existing_value.value}
            
            # Merge in new key-value pairs
            for k, v in value_node.value:
                existing_dict[k.value] = (k,v)
                
            # Create new MappingNode with merged values
            merged_value = type(value_node)(
                tag=value_node.tag,
                value=list(existing_dict.values())
            )
            result[key] = (key_node, merged_value)
            
        # If not both mapping nodes, take the latest value
        else:
            result[key] = (key_node, value_node)
            
    return list(result.values())