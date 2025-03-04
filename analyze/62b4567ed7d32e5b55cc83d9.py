def deep_merge_nodes(nodes):
    merged = {}
    
    # Iterate through nodes in reverse order so last value wins for non-mapping collisions
    for key_node, value_node in reversed(nodes):
        key = key_node.value
        
        if key not in merged:
            # First time seeing this key, just store the value
            merged[key] = (key_node, value_node)
            continue
            
        # Key exists, need to merge
        existing_value_node = merged[key][1]
        
        # If both are mapping nodes, do a deep merge
        if (hasattr(value_node, 'tag') and 'map' in value_node.tag and 
            hasattr(existing_value_node, 'tag') and 'map' in existing_value_node.tag):
            
            # Convert mapping node values to dict for easier merging
            existing_dict = {k.value: v for k,v in existing_value_node.value}
            new_dict = {k.value: v for k,v in value_node.value}
            
            # Update existing with new values
            existing_dict.update(new_dict)
            
            # Convert back to list of tuples
            merged_value = [
                (k_node, v_node) 
                for k_node, v_node in existing_value_node.value
                if k_node.value not in new_dict
            ]
            merged_value.extend([
                (k_node, v_node)
                for k_node, v_node in value_node.value 
            ])
            
            # Create new mapping node with merged values
            merged[key] = (
                key_node,
                type(value_node)(tag=value_node.tag, value=merged_value)
            )
            
        else:
            # For non-mapping nodes, just use the latest value
            merged[key] = (key_node, value_node)
            
    # Return list of merged tuples
    return list(merged.values())