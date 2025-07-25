def deep_merge_nodes(nodes):
    merged = {}
    
    # Iterate through nodes in reverse order so last value wins for non-mapping collisions
    for key_node, value_node in reversed(nodes):
        key = key_node.value
        
        if key not in merged:
            # First time seeing this key, just store the value
            merged[key] = (key_node, value_node)
            continue
            
        # We've seen this key before - need to merge
        existing_value_node = merged[key][1]
        
        # If both nodes are mapping nodes, do a deep merge
        if (hasattr(value_node, 'tag') and 'map' in value_node.tag and
            hasattr(existing_value_node, 'tag') and 'map' in existing_value_node.tag):
            
            # Convert the mapping node values to dict for easier lookup
            existing_dict = {k.value: (k,v) for k,v in existing_value_node.value}
            new_dict = {k.value: (k,v) for k,v in value_node.value}
            
            # Merge the new mapping into existing
            for new_key, new_val in new_dict.items():
                if new_key not in existing_dict:
                    existing_dict[new_key] = new_val
            
            # Convert back to list of tuples
            merged_value = list(existing_dict.values())
            
            # Create new MappingNode with merged values
            merged[key] = (key_node, type(value_node)(tag=value_node.tag, value=merged_value))
            
        else:
            # For non-mapping nodes, keep the most recent value
            merged[key] = (key_node, value_node)
            
    # Convert merged dict back to list of tuples
    return list(merged.values())