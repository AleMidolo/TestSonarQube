def deep_merge_nodes(nodes):
    # Dictionary to store merged nodes by key
    merged = {}
    
    # Iterate through all node tuples
    for key_node, value_node in nodes:
        key = key_node.value
        
        # If key doesn't exist yet, just add it
        if key not in merged:
            merged[key] = (key_node, value_node)
            continue
            
        # Get existing value node for this key
        existing_value_node = merged[key][1]
        
        # If both nodes are mapping nodes, merge them recursively
        if (value_node.tag == 'tag:yaml.org,2002:map' and 
            existing_value_node.tag == 'tag:yaml.org,2002:map'):
            
            # Convert mapping node values to dict for easier merging
            existing_dict = {k.value: v for k,v in existing_value_node.value}
            new_dict = {k.value: v for k,v in value_node.value}
            
            # Update existing dict with new values
            for k, v in new_dict.items():
                existing_dict[k] = v
                
            # Convert back to list of tuples
            merged_value = [(k_node, existing_dict[k_node.value]) 
                          for k_node, _ in existing_value_node.value 
                          if k_node.value in existing_dict]
            
            # Add any new keys
            for k_node, v_node in value_node.value:
                if k_node.value not in [k.value for k,_ in merged_value]:
                    merged_value.append((k_node, v_node))
                    
            # Create new mapping node with merged values    
            merged_mapping = type(value_node)(
                tag='tag:yaml.org,2002:map',
                value=merged_value
            )
            merged[key] = (key_node, merged_mapping)
            
        # For non-mapping nodes, newer value overwrites
        else:
            merged[key] = (key_node, value_node)
            
    # Convert merged dict back to list of tuples
    return list(merged.values())