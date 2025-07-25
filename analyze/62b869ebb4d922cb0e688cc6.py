def update_last_applied_manifest_list_from_resp(
    last_applied_manifest, observer_schema, response
):
    # Handle empty response
    if not response:
        return

    # Ensure last_applied_manifest has enough elements
    while len(last_applied_manifest) < len(response):
        last_applied_manifest.append({})

    # Update each element in the list
    for i, (schema_item, resp_item) in enumerate(zip(observer_schema, response)):
        # Handle dict type schema
        if isinstance(schema_item, dict):
            if not isinstance(last_applied_manifest[i], dict):
                last_applied_manifest[i] = {}
            update_last_applied_manifest_dict_from_resp(
                last_applied_manifest[i], schema_item, resp_item
            )
        # Handle list type schema
        elif isinstance(schema_item, list):
            if not isinstance(last_applied_manifest[i], list):
                last_applied_manifest[i] = []
            update_last_applied_manifest_list_from_resp(
                last_applied_manifest[i], schema_item, resp_item
            )
        # Handle primitive types
        else:
            last_applied_manifest[i] = resp_item