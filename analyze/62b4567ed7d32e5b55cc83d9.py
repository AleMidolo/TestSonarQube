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
        existing_value = merged[key][1]
        
        if (hasattr(existing_value, 'tag') and existing_value.tag == 'tag:yaml.org,2002:map' and
            hasattr(value_node, 'tag') and value_node.tag == 'tag:yaml.org,2002:map'):
            # Both are mapping nodes - do a deep merge
            existing_dict = {k.value: v for k,v in existing_value.value}
            new_dict = {k.value: v for k,v in value_node.value}
            
            # Recursively merge the mapping node values
            merged_value = deep_merge_nodes([
                (k, v) for k,v in existing_value.value
            ] + [
                (k, v) for k,v in value_node.value
            ])
            
            # Create new mapping node with merged values
            merged[key] = (key_node, type(value_node)(
                tag='tag:yaml.org,2002:map',
                value=merged_value
            ))
        else:
            # For non-mapping nodes, just take the latest value
            merged[key] = (key_node, value_node)
            
    # Convert merged dict back to list of tuples
    return [(k_node, v_node) for k_node, v_node in merged.values()]