def validate(self, inventory, extract_spec_version=False):
    """
    Validar un inventario dado.

    Si `extract_spec_version` es True, entonces se verificará el valor de `type` para determinar
    la versión de la especificación. En el caso de que no exista un valor para `type` o no sea
    válido, se realizarán otras pruebas basadas en la versión proporcionada en `self.spec_version`.
    """
    if not isinstance(inventory, dict):
        raise ValueError("El inventario debe ser un diccionario")

    if extract_spec_version:
        try:
            inventory_type = inventory.get('type', '')
            if inventory_type.startswith('inventory/'):
                self.spec_version = inventory_type.split('/')[1]
            else:
                # Si no hay un tipo válido, usar la versión por defecto
                pass
        except (AttributeError, IndexError):
            # Si hay algún error al extraer la versión, usar la versión por defecto
            pass

    # Validar campos requeridos básicos
    required_fields = ['id', 'items']
    for field in required_fields:
        if field not in inventory:
            raise ValueError(f"Campo requerido '{field}' no encontrado en el inventario")

    # Validar que items sea una lista
    if not isinstance(inventory['items'], list):
        raise ValueError("El campo 'items' debe ser una lista")

    # Validar cada item en el inventario
    for item in inventory['items']:
        if not isinstance(item, dict):
            raise ValueError("Cada item debe ser un diccionario")
        
        # Validar campos requeridos para cada item
        item_required_fields = ['id', 'quantity']
        for field in item_required_fields:
            if field not in item:
                raise ValueError(f"Campo requerido '{field}' no encontrado en un item")

        # Validar tipos de datos
        if not isinstance(item['id'], str):
            raise ValueError("El campo 'id' del item debe ser una cadena de texto")
        if not isinstance(item['quantity'], (int, float)):
            raise ValueError("El campo 'quantity' del item debe ser un número")

    return True