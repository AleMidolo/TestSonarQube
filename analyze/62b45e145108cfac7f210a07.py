def validate(self, inventory, extract_spec_version=False):
    """
    दिए गए इन्वेंटरी को सत्यापित करें।

    यदि `extract_spec_version` का मान `True` है, तो यह `type` मान को देखकर 
    स्पेसिफिकेशन वर्जन निर्धारित करेगा। यदि `type` मान मौजूद नहीं है या यह 
    मान्य नहीं है, तो अन्य परीक्षण `self.spec_version` में दिए गए वर्जन के 
    आधार पर किए जाएंगे।
    """
    if extract_spec_version:
        if 'type' in inventory:
            spec_version = inventory['type']
            if self.is_valid_spec_version(spec_version):
                self.spec_version = spec_version
            else:
                raise ValueError("Invalid specification version in 'type' field.")
        else:
            raise ValueError("'type' field is missing in inventory.")
    
    # Perform validation based on the determined or default spec_version
    if self.spec_version == 'v1':
        self.validate_v1(inventory)
    elif self.spec_version == 'v2':
        self.validate_v2(inventory)
    else:
        raise ValueError(f"Unsupported specification version: {self.spec_version}")

def is_valid_spec_version(self, spec_version):
    """
    Check if the given specification version is valid.
    """
    return spec_version in ['v1', 'v2']

def validate_v1(self, inventory):
    """
    Validate inventory against specification version v1.
    """
    # Add validation logic for v1
    pass

def validate_v2(self, inventory):
    """
    Validate inventory against specification version v2.
    """
    # Add validation logic for v2
    pass