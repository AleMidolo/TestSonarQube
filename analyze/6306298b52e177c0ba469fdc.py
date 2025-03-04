def xml_children_as_dict(node):
    # Create empty dictionary to store children
    children_dict = {}
    
    # Iterate through all child nodes
    for child in node:
        # Skip text nodes and comments
        if not isinstance(child.tag, str):
            continue
            
        # Get tag name
        tag = child.tag
        
        # If tag already exists in dict, make it a list
        if tag in children_dict:
            if not isinstance(children_dict[tag], list):
                children_dict[tag] = [children_dict[tag]]
            children_dict[tag].append(child)
        else:
            children_dict[tag] = child
            
    return children_dict