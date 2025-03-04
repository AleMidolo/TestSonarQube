def deep_merge_nodes(nodes):
    # Create dict to store merged nodes by key
    merged = {}
    
    # Iterate through all nodes
    for key_node, value_node in nodes:
        key = key_node.value
        
        # If key doesn't exist yet, just add it
        if key not in merged:
            merged[key] = (key_node, value_node)
            continue
            
        # Get existing value node for this key
        existing_value_node = merged[key][1]
        
        # If both nodes are mapping nodes, merge them recursively
        if (isinstance(value_node, type(existing_value_node)) and 
            hasattr(value_node, 'value') and 
            hasattr(existing_value_node, 'value')):
            
            # Create dict of existing key-value pairs
            existing_dict = {k.value: (k,v) for k,v in existing_value_node.value}
            
            # Update with new values
            for k, v in value_node.value:
                existing_dict[k.value] = (k,v)
                
            # Create new merged mapping node
            merged_value = type(value_node)(
                tag=value_node.tag,
                value=list(existing_dict.values())
            )
            merged[key] = (key_node, merged_value)
            
        # Otherwise just take the latest value
        else:
            merged[key] = (key_node, value_node)
            
    return list(merged.values())