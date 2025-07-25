def update_last_applied_manifest_dict_from_resp(
    last_applied_manifest, observer_schema, response
):
    # Iterate through all fields in the observer schema
    for field, value in observer_schema.items():
        # If field doesn't exist in response, raise KeyError
        if field not in response:
            raise KeyError(f"Field {field} not found in Kubernetes response")

        # If field not in last_applied_manifest, initialize it
        if field not in last_applied_manifest:
            if isinstance(value, dict):
                last_applied_manifest[field] = {}
                update_last_applied_manifest_dict_from_resp(
                    last_applied_manifest[field], value, response[field]
                )
            elif isinstance(value, list):
                last_applied_manifest[field] = []
                update_last_applied_manifest_list_from_resp(
                    last_applied_manifest[field], value[0], response[field]
                )
            else:
                last_applied_manifest[field] = response[field]