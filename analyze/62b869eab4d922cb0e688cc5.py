def update_last_applied_manifest_dict_from_resp(last_applied_manifest, observer_schema, response):
    # Iterate through all fields in observer schema
    for field_name, field_schema in observer_schema.items():
        # If field not initialized in last_applied_manifest, initialize it
        if field_name not in last_applied_manifest:
            last_applied_manifest[field_name] = {}

        # If field not in response, raise KeyError
        if field_name not in response:
            raise KeyError(f"Field {field_name} not found in Kubernetes response")

        # If field schema is a dict, recursively update nested fields
        if isinstance(field_schema, dict):
            update_last_applied_manifest_dict_from_resp(
                last_applied_manifest[field_name],
                field_schema,
                response[field_name]
            )
        # Otherwise copy value directly from response
        else:
            last_applied_manifest[field_name] = response[field_name]

    return last_applied_manifest