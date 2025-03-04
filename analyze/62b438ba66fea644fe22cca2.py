def deep_merge_nodes(nodes):
    merged = {}
    
    # Iterate through nodes in reverse so later values take precedence
    for key_node, value_node in reversed(nodes):
        key = key_node.value
        
        if key not in merged:
            # First time seeing this key, just store the nodes
            merged[key] = (key_node, value_node)
            continue
            
        # Key exists, need to merge
        existing_value_node = merged[key][1]
        
        # If both are mapping nodes, merge them recursively
        if (hasattr(value_node, 'tag') and 'map' in value_node.tag and 
            hasattr(existing_value_node, 'tag') and 'map' in existing_value_node.tag):
            
            # Convert mapping node values to dict for easier lookup
            existing_dict = {k.value: (k,v) for k,v in existing_value_node.value}
            new_dict = {k.value: (k,v) for k,v in value_node.value}
            
            # Merge the mapping values
            for new_key, new_value in new_dict.items():
                if new_key not in existing_dict:
                    existing_dict[new_key] = new_value
            
            # Convert back to list of tuples
            merged_value = list(existing_dict.values())
            
            # Create new mapping node with merged values
            merged[key] = (key_node, type(value_node)(tag=value_node.tag, value=merged_value))
            
        else:
            # For non-mapping nodes, just keep the existing value
            merged[key] = merged[key]
            
    # Convert merged dict back to list of tuples
    return list(merged.values())