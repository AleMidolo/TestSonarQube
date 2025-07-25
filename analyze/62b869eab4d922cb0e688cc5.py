def update_last_applied_manifest_dict_from_resp(
    last_applied_manifest, observer_schema, response
):
    # Iterate through all fields in observer schema
    for field, value in observer_schema.items():
        # Skip if field doesn't exist in response
        if field not in response:
            continue
            
        # Initialize field in last_applied_manifest if it doesn't exist
        if field not in last_applied_manifest:
            if isinstance(response[field], dict):
                last_applied_manifest[field] = {}
            elif isinstance(response[field], list):
                last_applied_manifest[field] = []
            else:
                last_applied_manifest[field] = response[field]
                continue

        # Recursively update nested dictionaries
        if isinstance(value, dict) and isinstance(response[field], dict):
            update_last_applied_manifest_dict_from_resp(
                last_applied_manifest[field], value, response[field]
            )
        # Handle lists
        elif isinstance(value, list) and isinstance(response[field], list):
            if len(value) > 0 and isinstance(value[0], dict):
                # List contains dictionaries - handle recursively
                if len(last_applied_manifest[field]) < len(response[field]):
                    last_applied_manifest[field].extend(
                        [{}] * (len(response[field]) - len(last_applied_manifest[field]))
                    )
                for i in range(len(response[field])):
                    update_last_applied_manifest_dict_from_resp(
                        last_applied_manifest[field][i], value[0], response[field][i]
                    )
            else:
                # List contains simple values - copy directly
                last_applied_manifest[field] = response[field]
        # Handle simple values
        else:
            last_applied_manifest[field] = response[field]