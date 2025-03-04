def deep_merge_nodes(nodes):
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
            
            # Create dict of existing key/value pairs
            existing_dict = {k.value: v for k,v in existing_value_node.value}
            
            # Update with new values
            for k, v in value_node.value:
                existing_dict[k.value] = v
                
            # Convert back to list of tuples
            merged_value = [(k, existing_dict[k.value]) 
                          for k in sorted(existing_dict.keys(), key=lambda x: x)]
            
            # Create new mapping node with merged values
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