def xml_children_as_dict(node):
    # Create empty dictionary to store children
    children_dict = {}
    
    # Iterate through all child nodes
    for child in node:
        # Skip non-element nodes like text/comments
        if not isinstance(child.tag, str):
            continue
            
        # Use the tag name as key and store the child node as value
        children_dict[child.tag] = child
        
    return children_dict