def validate(self, inventory, extract_spec_version=False):
    """
    Convalida un inventario specificato.

    Se `extract_spec_version` è impostato su `True`, verrà esaminato il valore del tipo (`type`) 
    per determinare la versione della specifica. Nel caso in cui non sia presente un valore per 
    il tipo o questo non sia valido, verranno eseguiti altri test basati sulla versione specificata 
    in `self.spec_version`.
    """
    if extract_spec_version:
        if 'type' in inventory:
            spec_type = inventory['type']
            if spec_type in self.supported_spec_versions:
                self.spec_version = spec_type
            else:
                print("Invalid type value. Falling back to default spec version.")
                self.spec_version = self.default_spec_version
        else:
            print("No type value found. Falling back to default spec version.")
            self.spec_version = self.default_spec_version
    
    # Perform validation based on the determined spec version
    if self.spec_version == "v1":
        self._validate_v1(inventory)
    elif self.spec_version == "v2":
        self._validate_v2(inventory)
    else:
        raise ValueError(f"Unsupported spec version: {self.spec_version}")

def _validate_v1(self, inventory):
    """
    Validate inventory against v1 specification.
    """
    # Example validation logic for v1
    if 'name' not in inventory:
        raise ValueError("Inventory must have a 'name' field for v1 specification.")
    # Add more validation rules as needed

def _validate_v2(self, inventory):
    """
    Validate inventory against v2 specification.
    """
    # Example validation logic for v2
    if 'id' not in inventory:
        raise ValueError("Inventory must have an 'id' field for v2 specification.")
    # Add more validation rules as needed