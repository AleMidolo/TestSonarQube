def xml_children_as_dict(node):
    # Create empty dictionary to store children
    children_dict = {}
    
    # Iterate through all child nodes
    for child in node:
        # Skip non-element nodes like text/comments
        if not isinstance(child.tag, str):
            continue
            
        # Use tag name as key and store node as value
        tag_name = child.tag
        children_dict[tag_name] = child
        
    return children_dict