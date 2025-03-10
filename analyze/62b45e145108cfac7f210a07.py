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
        else:
            print("No type value found. Falling back to default spec version.")
    
    # Perform validation based on the determined spec version
    if self.spec_version in self.supported_spec_versions:
        self._validate_inventory(inventory)
    else:
        raise ValueError("Unsupported specification version.")