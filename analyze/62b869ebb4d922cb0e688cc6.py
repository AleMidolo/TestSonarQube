def update_last_applied_manifest_list_from_resp(last_applied_manifest, observer_schema, response):
    # Handle empty cases
    if not observer_schema or not response:
        return
        
    # Ensure last_applied_manifest has enough elements
    while len(last_applied_manifest) < len(response):
        last_applied_manifest.append({})
        
    # Iterate through response items
    for i, resp_item in enumerate(response):
        if i >= len(observer_schema):
            break
            
        # Get schema for this item
        schema = observer_schema[i]
        
        # Skip if schema is None
        if not schema:
            continue
            
        # Handle dict items
        if isinstance(resp_item, dict):
            if not isinstance(last_applied_manifest[i], dict):
                last_applied_manifest[i] = {}
            from .utils import update_last_applied_manifest_dict_from_resp
            update_last_applied_manifest_dict_from_resp(
                last_applied_manifest[i],
                schema,
                resp_item
            )
            
        # Handle list items 
        elif isinstance(resp_item, list):
            if not isinstance(last_applied_manifest[i], list):
                last_applied_manifest[i] = []
            update_last_applied_manifest_list_from_resp(
                last_applied_manifest[i],
                schema,
                resp_item
            )
            
        # Handle primitive values
        else:
            last_applied_manifest[i] = resp_item