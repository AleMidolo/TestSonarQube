def update_last_applied_manifest_list_from_resp(
    last_applied_manifest, observer_schema, response
):
    # If response is None, nothing to update
    if response is None:
        return

    # Ensure last_applied_manifest is a list
    if not isinstance(last_applied_manifest, list):
        last_applied_manifest.clear()
        last_applied_manifest.extend([])

    # Extend last_applied_manifest to match response length
    while len(last_applied_manifest) < len(response):
        last_applied_manifest.append({})

    # Update each item in the list
    for i, (schema_item, resp_item) in enumerate(zip(observer_schema, response)):
        # Skip if response item is None
        if resp_item is None:
            continue

        # Get or create dict at index i
        if i >= len(last_applied_manifest):
            last_applied_manifest.append({})
        
        # If schema item is a dict, recursively update
        if isinstance(schema_item, dict):
            from_dict = update_last_applied_manifest_dict_from_resp(
                last_applied_manifest[i], schema_item, resp_item
            )
            last_applied_manifest[i].update(from_dict)
        # If schema item is a list, recursively update
        elif isinstance(schema_item, list):
            update_last_applied_manifest_list_from_resp(
                last_applied_manifest[i], schema_item, resp_item
            )
        # Otherwise directly update value
        else:
            last_applied_manifest[i] = resp_item