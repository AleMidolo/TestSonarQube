def update_last_applied_manifest_list_from_resp(
    last_applied_manifest, observer_schema, response
):
    # Handle empty cases
    if not observer_schema or not response:
        return
        
    # Ensure last_applied_manifest has enough elements
    while len(last_applied_manifest) < len(response):
        last_applied_manifest.append({})
        
    # Update each element in the list
    for i in range(len(response)):
        if i < len(observer_schema):
            # If schema element is a dict, recursively update
            if isinstance(observer_schema[i], dict):
                if not isinstance(last_applied_manifest[i], dict):
                    last_applied_manifest[i] = {}
                update_last_applied_manifest_dict_from_resp(
                    last_applied_manifest[i],
                    observer_schema[i], 
                    response[i]
                )
            # If schema element is a list, recursively update
            elif isinstance(observer_schema[i], list):
                if not isinstance(last_applied_manifest[i], list):
                    last_applied_manifest[i] = []
                update_last_applied_manifest_list_from_resp(
                    last_applied_manifest[i],
                    observer_schema[i],
                    response[i]
                )
            # For primitive types, copy value directly
            else:
                last_applied_manifest[i] = response[i]