def update_last_applied_manifest_list_from_resp(last_applied_manifest, observer_schema, response):
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
        
        # Skip if schema item is not a dict
        if not isinstance(schema_item, dict):
            continue
            
        # Initialize empty dict if needed
        if not isinstance(last_applied_manifest[i], dict):
            last_applied_manifest[i] = {}
            
        # Update fields based on schema
        for field, value in resp_item.items():
            if field in schema_item:
                if isinstance(value, dict) and isinstance(schema_item[field], dict):
                    # Recursively handle nested dicts
                    if field not in last_applied_manifest[i]:
                        last_applied_manifest[i][field] = {}
                    update_last_applied_manifest_dict_from_resp(
                        last_applied_manifest[i][field],
                        schema_item[field],
                        value
                    )
                elif isinstance(value, list) and isinstance(schema_item[field], list):
                    # Recursively handle nested lists
                    if field not in last_applied_manifest[i]:
                        last_applied_manifest[i][field] = []
                    update_last_applied_manifest_list_from_resp(
                        last_applied_manifest[i][field],
                        schema_item[field],
                        value
                    )
                else:
                    # Direct value assignment
                    last_applied_manifest[i][field] = value