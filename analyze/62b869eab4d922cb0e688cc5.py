def update_last_applied_manifest_dict_from_resp(
    last_applied_manifest, observer_schema, response
):
    # Iterate through all fields in observer schema
    for field, value in observer_schema.items():
        # If field not in response, raise KeyError
        if field not in response:
            raise KeyError(f"Field {field} not found in Kubernetes response")

        # If field not in last_applied_manifest, initialize it
        if field not in last_applied_manifest:
            if isinstance(value, dict):
                # For nested dict fields, initialize empty dict
                last_applied_manifest[field] = {}
                # Recursively update nested dict
                update_last_applied_manifest_dict_from_resp(
                    last_applied_manifest[field], value, response[field]
                )
            elif isinstance(value, list):
                # For list fields, initialize empty list
                last_applied_manifest[field] = []
                # Update list field
                update_last_applied_manifest_list_from_resp(
                    last_applied_manifest[field], value[0], response[field]
                )
            else:
                # For simple fields, copy value from response
                last_applied_manifest[field] = response[field]