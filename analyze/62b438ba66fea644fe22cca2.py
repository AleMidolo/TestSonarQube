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
            
            # Recursively merge the nested mapping nodes
            merged_value = deep_merge_nodes(existing_value_node.value + value_node.value)
            
            # Create new mapping node with merged values
            new_value_node = type(value_node)(
                tag='tag:yaml.org,2002:map',
                value=merged_value
            )
            merged[key] = (key_node, new_value_node)
            
        # For non-mapping nodes, latest value wins
        else:
            merged[key] = (key_node, value_node)
            
    # Convert merged dict back to list of tuples
    return list(merged.values())