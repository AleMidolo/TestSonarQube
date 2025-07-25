def deep_merge_nodes(nodes):
    merged = {}
    
    for key_node, value_node in nodes:
        key = key_node.value
        
        if key in merged:
            existing_value_node = merged[key]
            
            if isinstance(existing_value_node, ruamel.yaml.nodes.MappingNode) and isinstance(value_node, ruamel.yaml.nodes.MappingNode):
                # Merge the two MappingNodes
                existing_items = {item[0].value: item[1] for item in existing_value_node.value}
                new_items = {item[0].value: item[1] for item in value_node.value}
                
                # Deep merge the items
                for new_key, new_value in new_items.items():
                    if new_key in existing_items and isinstance(existing_items[new_key], ruamel.yaml.nodes.MappingNode) and isinstance(new_value, ruamel.yaml.nodes.MappingNode):
                        # Recursively merge nested MappingNodes
                        merged_items = deep_merge_nodes([(ruamel.yaml.nodes.ScalarNode(tag='tag:yaml.org,2002:str', value=new_key), existing_items[new_key]),
                                                       (ruamel.yaml.nodes.ScalarNode(tag='tag:yaml.org,2002:str', value=new_key), new_value)])
                        existing_items[new_key] = merged_items[0][1]
                    else:
                        # Overwrite with the new value
                        existing_items[new_key] = new_value
                
                # Convert back to a list of tuples
                merged[key] = ruamel.yaml.nodes.MappingNode(
                    tag='tag:yaml.org,2002:map',
                    value=[(ruamel.yaml.nodes.ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in existing_items.items()]
                )
            else:
                # Overwrite with the new value if not both are MappingNodes
                merged[key] = value_node
        else:
            # Add the new key-value pair
            merged[key] = value_node
    
    # Convert the merged dictionary back to a list of tuples
    return [(ruamel.yaml.nodes.ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in merged.items()]