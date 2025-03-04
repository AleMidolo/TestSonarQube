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
            
        schema_item = observer_schema[i]
        
        # Skip if schema item is not a dict
        if not isinstance(schema_item, dict):
            continue
            
        # Get or create manifest item
        manifest_item = last_applied_manifest[i]
        if not isinstance(manifest_item, dict):
            manifest_item = {}
            last_applied_manifest[i] = manifest_item
            
        # Update fields based on schema
        for field, value in resp_item.items():
            if field in schema_item:
                if isinstance(value, dict) and isinstance(schema_item[field], dict):
                    # Recursively handle nested dicts
                    if field not in manifest_item:
                        manifest_item[field] = {}
                    update_last_applied_manifest_dict_from_resp(
                        manifest_item[field],
                        schema_item[field], 
                        value
                    )
                elif isinstance(value, list) and isinstance(schema_item[field], list):
                    # Recursively handle nested lists
                    if field not in manifest_item:
                        manifest_item[field] = []
                    update_last_applied_manifest_list_from_resp(
                        manifest_item[field],
                        schema_item[field],
                        value
                    )
                else:
                    # Directly update primitive values
                    manifest_item[field] = value