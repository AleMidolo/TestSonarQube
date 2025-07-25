def validate(self, inventory, extract_spec_version=False):
    """
    Validar un inventario dado.

    Si `extract_spec_version` es True, entonces se verificará el valor de `type` para determinar
    la versión de la especificación. En el caso de que no exista un valor para `type` o no sea
    válido, se realizarán otras pruebas basadas en la versión proporcionada en `self.spec_version`.
    """
    if extract_spec_version:
        if 'type' in inventory:
            spec_type = inventory['type']
            if spec_type in self.supported_spec_versions:
                self.spec_version = spec_type
            else:
                # Fallback to default spec version if type is not valid
                self.spec_version = self.default_spec_version
        else:
            # Use the instance's spec version if type is not provided
            self.spec_version = self.spec_version
    else:
        # Use the instance's spec version if extract_spec_version is False
        self.spec_version = self.spec_version

    # Perform validation based on the determined spec version
    if self.spec_version == 'v1':
        return self._validate_v1(inventory)
    elif self.spec_version == 'v2':
        return self._validate_v2(inventory)
    else:
        raise ValueError(f"Unsupported spec version: {self.spec_version}")