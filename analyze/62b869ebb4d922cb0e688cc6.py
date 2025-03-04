def update_last_applied_manifest_list_from_resp(
    last_applied_manifest, observer_schema, response
):
    # Handle empty cases
    if not observer_schema or not response:
        return
        
    # Ensure last_applied_manifest has enough elements
    while len(last_applied_manifest) < len(response):
        last_applied_manifest.append({})
        
    # Process each element in the response list
    for i, resp_item in enumerate(response):
        if i >= len(observer_schema):
            break
            
        schema_item = observer_schema[i]
        
        # Skip if schema item is not a dict/list
        if not isinstance(schema_item, (dict, list)):
            continue
            
        # Handle nested dict
        if isinstance(schema_item, dict):
            if not isinstance(resp_item, dict):
                continue
            if not isinstance(last_applied_manifest[i], dict):
                last_applied_manifest[i] = {}
            update_last_applied_manifest_dict_from_resp(
                last_applied_manifest[i],
                schema_item,
                resp_item
            )
            
        # Handle nested list    
        elif isinstance(schema_item, list):
            if not isinstance(resp_item, list):
                continue
            if not isinstance(last_applied_manifest[i], list):
                last_applied_manifest[i] = []
            update_last_applied_manifest_list_from_resp(
                last_applied_manifest[i],
                schema_item,
                resp_item
            )