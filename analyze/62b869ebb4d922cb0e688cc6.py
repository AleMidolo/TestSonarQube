def update_last_applied_manifest_list_from_resp(
    last_applied_manifest, observer_schema, response
):
    # If response is None, return empty list
    if response is None:
        return []
    
    # If last_applied_manifest is None, initialize as empty list
    if last_applied_manifest is None:
        last_applied_manifest = []
        
    # Extend last_applied_manifest if shorter than response
    while len(last_applied_manifest) < len(response):
        last_applied_manifest.append({})
        
    # Update each item in the list recursively
    for i, (schema_item, resp_item) in enumerate(zip(observer_schema, response)):
        # Skip if index out of range
        if i >= len(last_applied_manifest):
            continue
            
        # Handle dict items
        if isinstance(schema_item, dict) and isinstance(resp_item, dict):
            from .utils import update_last_applied_manifest_dict_from_resp
            update_last_applied_manifest_dict_from_resp(
                last_applied_manifest[i], 
                schema_item,
                resp_item
            )
        # Handle list items    
        elif isinstance(schema_item, list) and isinstance(resp_item, list):
            update_last_applied_manifest_list_from_resp(
                last_applied_manifest[i],
                schema_item,
                resp_item
            )
        # Handle primitive values
        else:
            last_applied_manifest[i] = resp_item
            
    return last_applied_manifest