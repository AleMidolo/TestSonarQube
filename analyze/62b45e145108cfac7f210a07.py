def validate(self, inventory, extract_spec_version=False):
    """
    Validate a given inventory.

    If extract_spec_version is True then will look at the type value to determine
    the specification version. In the case that there is no type value or it isn't
    valid, then other tests will be based on the version given in self.spec_version.
    """
    if extract_spec_version:
        if 'type' in inventory:
            type_value = inventory['type']
            # Assuming type_value contains the version information
            if isinstance(type_value, str) and type_value.startswith("spec_v"):
                spec_version = type_value.split("_")[-1]
                try:
                    spec_version = float(spec_version)
                    self.spec_version = spec_version
                except ValueError:
                    # If the version cannot be extracted, use the default
                    pass
        else:
            # If no type value, use the default spec_version
            pass
    
    # Perform validation based on self.spec_version
    # Example validation logic (this is a placeholder)
    if self.spec_version == 1.0:
        # Validate for version 1.0
        if 'items' not in inventory:
            raise ValueError("Inventory must contain 'items' for version 1.0")
    elif self.spec_version == 2.0:
        # Validate for version 2.0
        if 'products' not in inventory:
            raise ValueError("Inventory must contain 'products' for version 2.0")
    else:
        # Default validation logic
        if 'items' not in inventory and 'products' not in inventory:
            raise ValueError("Inventory must contain either 'items' or 'products'")
    
    return True