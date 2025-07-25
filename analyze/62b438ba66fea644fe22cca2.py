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
        
        # If both nodes are mapping nodes, merge them recursively
        if (value_node.tag == 'tag:yaml.org,2002:map' and 
            existing_value_node.tag == 'tag:yaml.org,2002:map'):
            
            # Convert mapping node values to dict for easier lookup
            existing_dict = {k.value: v for k,v in existing_value_node.value}
            new_dict = {k.value: v for k,v in value_node.value}
            
            # Merge the two dicts, with new values taking precedence
            merged_dict = existing_dict.copy()
            for k, v in new_dict.items():
                merged_dict[k] = v
                
            # Convert back to list of tuples
            merged_value = []
            for k, v in merged_dict.items():
                # Find original key node with this value
                key_node = next(kn for kn,_ in existing_value_node.value + value_node.value 
                              if kn.value == k)
                merged_value.append((key_node, v))
                
            # Create new mapping node with merged values
            merged_mapping = type(value_node)(
                tag='tag:yaml.org,2002:map',
                value=merged_value
            )
            merged[key] = (key_node, merged_mapping)
            
        # For non-mapping nodes, keep the latest value
        else:
            merged[key] = (key_node, value_node)
            
    # Convert merged dict back to list of tuples
    return list(merged.values())