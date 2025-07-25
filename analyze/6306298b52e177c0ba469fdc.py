def xml_children_as_dict(node):
    # Create empty dictionary to store children
    children_dict = {}
    
    # Iterate through all child nodes
    for child in node:
        # Skip non-element nodes like text/comments
        if not isinstance(child.tag, str):
            continue
            
        # Use the tag name as key and store the child node as value
        tag_name = child.tag
        
        # If tag already exists, convert value to list
        if tag_name in children_dict:
            if not isinstance(children_dict[tag_name], list):
                children_dict[tag_name] = [children_dict[tag_name]]
            children_dict[tag_name].append(child)
        else:
            children_dict[tag_name] = child
            
    return children_dict