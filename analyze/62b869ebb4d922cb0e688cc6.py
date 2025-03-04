def update_last_applied_manifest_list_from_resp(
    last_applied_manifest, observer_schema, response
):
    # Handle empty response
    if not response:
        return
    
    # Ensure last_applied_manifest has enough elements
    while len(last_applied_manifest) < len(response):
        last_applied_manifest.append({})

    # Iterate through response items
    for i, resp_item in enumerate(response):
        # Get corresponding schema for this index
        if i < len(observer_schema):
            schema_item = observer_schema[i]
        else:
            schema_item = observer_schema[-1] # Use last schema for additional items
            
        # Update manifest item based on schema type
        if isinstance(schema_item, dict):
            from .manifest import update_last_applied_manifest_dict_from_resp
            update_last_applied_manifest_dict_from_resp(
                last_applied_manifest[i], 
                schema_item,
                resp_item
            )
        elif isinstance(schema_item, list):
            update_last_applied_manifest_list_from_resp(
                last_applied_manifest[i],
                schema_item,
                resp_item
            )
        else:
            # For primitive types, directly copy the value
            last_applied_manifest[i] = resp_item