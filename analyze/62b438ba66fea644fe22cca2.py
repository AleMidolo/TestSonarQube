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
            for new_key, new_pair in new_dict.items():
                if new_key not in existing_dict:
                    existing_dict[new_key] = new_pair
                else:
                    # Recursively merge if both are mapping nodes
                    if ('map' in new_pair[1].tag and 
                        'map' in existing_dict[new_key][1].tag):
                        merged_value = deep_merge_nodes([
                            (existing_dict[new_key][0], existing_dict[new_key][1]),
                            (new_pair[0], new_pair[1])
                        ])
                        existing_dict[new_key] = merged_value[0]
                    else:
                        # For non-mapping nodes, take the newer value
                        existing_dict[new_key] = new_pair
                        
            # Convert back to list of tuples
            merged_value = list(existing_dict.values())
            
            # Create new mapping node with merged values
            merged[key] = (key_node, type(value_node)(tag=value_node.tag, value=merged_value))
            
        else:
            # For non-mapping nodes, take the newer value
            merged[key] = (key_node, value_node)
            
    return list(merged.values())