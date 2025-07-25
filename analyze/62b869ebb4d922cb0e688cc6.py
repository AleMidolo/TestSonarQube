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

    # Iterate through response items
    for i, resp_item in enumerate(response):
        if i >= len(observer_schema):
            break

        # Get corresponding schema for this item
        schema = observer_schema[i]

        # If schema is a dict, recursively update nested dict
        if isinstance(schema, dict):
            if not isinstance(last_applied_manifest[i], dict):
                last_applied_manifest[i] = {}
            from .utils import update_last_applied_manifest_dict_from_resp
            update_last_applied_manifest_dict_from_resp(
                last_applied_manifest[i], 
                schema,
                resp_item
            )
        # If schema is a list, recursively update nested list  
        elif isinstance(schema, list):
            if not isinstance(last_applied_manifest[i], list):
                last_applied_manifest[i] = []
            update_last_applied_manifest_list_from_resp(
                last_applied_manifest[i],
                schema,
                resp_item
            )
        # For primitive values, copy directly from response
        else:
            last_applied_manifest[i] = resp_item

    return last_applied_manifest