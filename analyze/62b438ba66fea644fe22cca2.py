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
        if (hasattr(value_node, 'tag') and value_node.tag == 'tag:yaml.org,2002:map' and
            hasattr(existing_value_node, 'tag') and existing_value_node.tag == 'tag:yaml.org,2002:map'):
            
            # Convert mapping node values to dict for easier merging
            existing_dict = {k.value: (k,v) for k,v in existing_value_node.value}
            new_dict = {k.value: (k,v) for k,v in value_node.value}
            
            # Merge the dicts, with new values taking precedence
            merged_dict = existing_dict.copy()
            merged_dict.update(new_dict)
            
            # Convert back to list of tuples for MappingNode
            merged_value = [(k_v[0], k_v[1]) for k_v in merged_dict.values()]
            
            merged[key] = (key_node, type(value_node)(tag=value_node.tag, value=merged_value))
            
        else:
            # For non-mapping nodes, just keep the latest value
            merged[key] = (key_node, value_node)
            
    # Convert merged dict back to list of tuples
    return list(merged.values())