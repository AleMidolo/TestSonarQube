def update_last_applied_manifest_list_from_resp(
    last_applied_manifest, observer_schema, response
):
    # Handle empty cases
    if not observer_schema or not response:
        return last_applied_manifest

    # Ensure last_applied_manifest has enough elements
    while len(last_applied_manifest) < len(response):
        last_applied_manifest.append({})

    # Iterate through response items
    for i, resp_item in enumerate(response):
        if i >= len(observer_schema):
            break
            
        schema_item = observer_schema[i]
        
        # Handle dict case recursively
        if isinstance(resp_item, dict) and isinstance(schema_item, dict):
            from .utils import update_last_applied_manifest_dict_from_resp
            last_applied_manifest[i] = update_last_applied_manifest_dict_from_resp(
                last_applied_manifest[i], schema_item, resp_item
            )
            
        # Handle list case recursively    
        elif isinstance(resp_item, list) and isinstance(schema_item, list):
            last_applied_manifest[i] = update_last_applied_manifest_list_from_resp(
                last_applied_manifest[i] if isinstance(last_applied_manifest[i], list) else [],
                schema_item,
                resp_item
            )
            
        # Handle primitive values
        else:
            last_applied_manifest[i] = resp_item

    return last_applied_manifest