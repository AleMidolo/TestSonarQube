def xml_children_as_dict(node):
    # Create empty dictionary to store child nodes
    children_dict = {}
    
    # Iterate through all child nodes
    for child in node:
        # Get the tag name of the child node
        tag = child.tag
        
        # If tag already exists in dictionary, make it a list
        if tag in children_dict:
            # Convert existing value to list if not already
            if not isinstance(children_dict[tag], list):
                children_dict[tag] = [children_dict[tag]]
            # Append new child node to list    
            children_dict[tag].append(child)
        else:
            # Add new tag:child pair to dictionary
            children_dict[tag] = child
            
    return children_dict