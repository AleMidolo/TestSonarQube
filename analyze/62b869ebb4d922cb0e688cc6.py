def update_last_applied_manifest_list_from_resp(
    last_applied_manifest, observer_schema, response
):
    # Handle empty cases
    if not observer_schema or not response:
        return last_applied_manifest

    # Ensure last_applied_manifest is a list
    if not isinstance(last_applied_manifest, list):
        last_applied_manifest = []

    # Extend last_applied_manifest if needed
    while len(last_applied_manifest) < len(response):
        last_applied_manifest.append({})

    # Update each element in the list
    for i, (schema_item, resp_item) in enumerate(zip(observer_schema, response)):
        if isinstance(schema_item, dict):
            # If schema item is a dict, recursively update the dict
            from .utils import update_last_applied_manifest_dict_from_resp
            last_applied_manifest[i] = update_last_applied_manifest_dict_from_resp(
                last_applied_manifest[i], schema_item, resp_item
            )
        elif isinstance(schema_item, list):
            # If schema item is a list, recursively update the list
            last_applied_manifest[i] = update_last_applied_manifest_list_from_resp(
                last_applied_manifest[i], schema_item, resp_item
            )
        else:
            # For primitive types, directly update the value
            last_applied_manifest[i] = resp_item

    return last_applied_manifest