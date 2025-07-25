def deep_merge_nodes(nodes):
    # Create a dictionary to store merged nodes by key
    merged = {}
    
    # Iterate through all nodes
    for key_node, value_node in nodes:
        key = key_node.value
        
        # If key doesn't exist yet, just add it
        if key not in merged:
            merged[key] = (key_node, value_node)
            continue
            
        # If key exists, we need to merge
        existing_value = merged[key][1]
        
        # If both nodes are MappingNodes, do a deep merge
        if (isinstance(existing_value, type(value_node)) and 
            hasattr(existing_value, 'value') and 
            hasattr(value_node, 'value')):
            
            # Convert existing mapping to dict for easier lookup
            existing_dict = {k.value: (k,v) for k,v in existing_value.value}
            
            # Merge in new values
            for k, v in value_node.value:
                existing_dict[k.value] = (k,v)
                
            # Convert back to list of tuples
            merged_value = list(existing_dict.values())
            
            # Create new MappingNode with merged values
            merged[key] = (key_node, type(value_node)(
                tag=value_node.tag,
                value=merged_value
            ))
            
        # If not both MappingNodes, keep the latest value
        else:
            merged[key] = (key_node, value_node)
    
    # Return list of merged tuples
    return list(merged.values())