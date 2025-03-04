def update_last_applied_manifest_list_from_resp(last_applied_manifest, observer_schema, response):
    # Handle empty cases
    if not observer_schema or not response:
        return last_applied_manifest

    # Ensure last_applied_manifest is initialized as a list
    if last_applied_manifest is None:
        last_applied_manifest = []

    # Extend last_applied_manifest if needed to match response length
    while len(last_applied_manifest) < len(response):
        last_applied_manifest.append({})

    # Update each item in the list
    for i, (schema_item, resp_item) in enumerate(zip(observer_schema, response)):
        if i >= len(last_applied_manifest):
            break
            
        # Handle dict type schema items
        if isinstance(schema_item, dict):
            if not isinstance(last_applied_manifest[i], dict):
                last_applied_manifest[i] = {}
            for key, value in schema_item.items():
                if key in resp_item:
                    if isinstance(value, list):
                        if key not in last_applied_manifest[i]:
                            last_applied_manifest[i][key] = []
                        update_last_applied_manifest_list_from_resp(
                            last_applied_manifest[i][key],
                            value,
                            resp_item[key]
                        )
                    elif isinstance(value, dict):
                        if key not in last_applied_manifest[i]:
                            last_applied_manifest[i][key] = {}
                        update_last_applied_manifest_dict_from_resp(
                            last_applied_manifest[i][key],
                            value,
                            resp_item[key]
                        )
                    else:
                        last_applied_manifest[i][key] = resp_item[key]
                        
        # Handle non-dict schema items
        else:
            last_applied_manifest[i] = resp_item

    return last_applied_manifest