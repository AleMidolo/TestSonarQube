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
            if isinstance(type_value, str) and type_value.startswith("stix"):
                spec_version = type_value.split("-")[-1]
                if spec_version in ["2.0", "2.1"]:
                    self.spec_version = spec_version
                else:
                    print("Invalid type value for spec version extraction.")
            else:
                print("Type value is not valid for spec version extraction.")
        else:
            print("No type value found in inventory for spec version extraction.")
    
    # Perform validation based on self.spec_version
    if self.spec_version == "2.0":
        # Validation logic for STIX 2.0
        pass
    elif self.spec_version == "2.1":
        # Validation logic for STIX 2.1
        pass
    else:
        print("Unsupported specification version.")