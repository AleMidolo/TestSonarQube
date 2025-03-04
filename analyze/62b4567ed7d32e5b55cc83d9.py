def deep_merge_nodes(nodes):
    result = {}
    
    # Iterate through all nodes and merge them
    for key_node, value_node in nodes:
        key = key_node.value
        
        # If key doesn't exist yet, just add it
        if key not in result:
            result[key] = (key_node, value_node)
            continue
            
        # If key exists, merge the values
        existing_value = result[key][1]
        
        # If both nodes are mapping nodes, merge them recursively
        if (isinstance(existing_value, type(value_node)) and 
            hasattr(existing_value, 'tag') and
            existing_value.tag == 'tag:yaml.org,2002:map' and
            value_node.tag == 'tag:yaml.org,2002:map'):
            
            # Convert mapping node values to dict for easier merging
            existing_dict = {k.value: v for k,v in existing_value.value}
            new_dict = {k.value: v for k,v in value_node.value}
            
            # Merge the dictionaries
            for k, v in new_dict.items():
                existing_dict[k] = v
                
            # Convert back to list of tuples format
            merged_value = [(k_node, v) for k_node, v in value_node.value 
                          if k_node.value in existing_dict]
            
            result[key] = (key_node, type(value_node)(
                tag=value_node.tag,
                value=merged_value
            ))
            
        # For non-mapping nodes, take the latest value
        else:
            result[key] = (key_node, value_node)
            
    return list(result.values())