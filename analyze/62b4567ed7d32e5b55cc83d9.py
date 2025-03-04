def deep_merge_nodes(nodes):
    # Dictionary to store merged nodes by key
    merged = {}
    
    # Iterate through all nodes
    for key_node, value_node in nodes:
        key = key_node.value
        
        # If key not seen before, add it directly
        if key not in merged:
            merged[key] = (key_node, value_node)
            continue
            
        # Get existing value node for this key
        existing_value_node = merged[key][1]
        
        # If both nodes are mapping nodes, merge them recursively
        if (isinstance(value_node, type(existing_value_node)) and 
            hasattr(value_node, 'value') and 
            hasattr(existing_value_node, 'value')):
            
            # Convert inner nodes to dict for easier merging
            existing_dict = {k.value: v for k,v in existing_value_node.value}
            new_dict = {k.value: v for k,v in value_node.value}
            
            # Update existing dict with new values
            for k, v in new_dict.items():
                existing_dict[k] = v
                
            # Convert back to list of tuples
            merged_value = [(k_node, v) for k_node, v in value_node.value 
                          if k_node.value in existing_dict]
            
            # Create new MappingNode with merged values
            merged_node = type(value_node)(
                tag=value_node.tag,
                value=merged_value
            )
            
            merged[key] = (key_node, merged_node)
            
        # For non-mapping nodes, latest value wins
        else:
            merged[key] = (key_node, value_node)
            
    # Convert merged dict back to list of tuples
    return list(merged.values())