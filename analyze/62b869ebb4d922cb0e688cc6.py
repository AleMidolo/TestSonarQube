def update_last_applied_manifest_list_from_resp(
    last_applied_manifest, observer_schema, response
):
    # Handle empty cases
    if not observer_schema or not response:
        return
    
    # Ensure last_applied_manifest has enough elements
    while len(last_applied_manifest) < len(response):
        last_applied_manifest.append({})

    # Iterate through response items and update manifest
    for i, resp_item in enumerate(response):
        if i < len(observer_schema):
            # If schema item is a dict, recursively update
            if isinstance(observer_schema[i], dict):
                if not isinstance(last_applied_manifest[i], dict):
                    last_applied_manifest[i] = {}
                update_last_applied_manifest_dict_from_resp(
                    last_applied_manifest[i],
                    observer_schema[i],
                    resp_item
                )
            # If schema item is a list, recursively update
            elif isinstance(observer_schema[i], list):
                if not isinstance(last_applied_manifest[i], list):
                    last_applied_manifest[i] = []
                update_last_applied_manifest_list_from_resp(
                    last_applied_manifest[i],
                    observer_schema[i],
                    resp_item
                )
            # For primitive types, directly copy value
            else:
                last_applied_manifest[i] = resp_item