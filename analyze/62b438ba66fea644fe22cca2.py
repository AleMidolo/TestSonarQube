def deep_merge_nodes(nodes):
    # Create dict to store merged results
    merged = {}
    
    # Iterate through all nodes
    for key_node, value_node in nodes:
        key = key_node.value
        
        # If key doesn't exist yet, just add it
        if key not in merged:
            merged[key] = (key_node, value_node)
            continue
            
        # If key exists, need to merge
        existing_value = merged[key][1]
        
        # If both are mapping nodes, merge recursively
        if (hasattr(existing_value, 'tag') and 
            hasattr(value_node, 'tag') and
            existing_value.tag == 'tag:yaml.org,2002:map' and 
            value_node.tag == 'tag:yaml.org,2002:map'):
            
            # Convert mapping node values to dict for easier merging
            existing_dict = {k.value: (k,v) for k,v in existing_value.value}
            new_dict = {k.value: (k,v) for k,v in value_node.value}
            
            # Merge the dicts
            for k, v in new_dict.items():
                existing_dict[k] = v
                
            # Convert back to list of tuples
            merged_value = list(existing_dict.values())
            
            # Create new mapping node with merged values
            merged[key] = (key_node, type(value_node)(
                tag='tag:yaml.org,2002:map',
                value=merged_value
            ))
            
        # For non-mapping nodes, take the latest value
        else:
            merged[key] = (key_node, value_node)
            
    # Return list of merged tuples
    return list(merged.values())