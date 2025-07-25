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
            
        # Get existing value node for this key
        existing_value_node = merged[key][1]
        
        # If both nodes are mapping nodes, merge them
        if (isinstance(value_node, type(existing_value_node)) and 
            hasattr(value_node, 'value') and 
            hasattr(existing_value_node, 'value')):
            
            # Convert inner nodes to dict for merging
            existing_dict = {k.value: v for k,v in existing_value_node.value}
            new_dict = {k.value: v for k,v in value_node.value}
            
            # Update existing dict with new values
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
            merged_mapping = type(value_node)(
                tag=value_node.tag,
                value=merged_value
            )
            
            merged[key] = (key_node, merged_mapping)
            
        # If not both mapping nodes, take the latest value
        else:
            merged[key] = (key_node, value_node)
            
    # Return list of merged tuples
    return list(merged.values())