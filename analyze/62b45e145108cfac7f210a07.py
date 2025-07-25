def validate(self, inventory, extract_spec_version=False):
    """
    Convalida un inventario specificato.

    Se `extract_spec_version` è impostato su `True`, verrà esaminato il valore del tipo (`type`) 
    per determinare la versione della specifica. Nel caso in cui non sia presente un valore per 
    il tipo o questo non sia valido, verranno eseguiti altri test basati sulla versione specificata 
    in `self.spec_version`.
    """
    if not isinstance(inventory, dict):
        raise ValueError("L'inventario deve essere un dizionario")

    if extract_spec_version:
        try:
            inventory_type = inventory.get('type', '')
            if 'bom-1.0' in inventory_type:
                self.spec_version = '1.0'
            elif 'bom-1.1' in inventory_type:
                self.spec_version = '1.1'
            elif 'bom-1.2' in inventory_type:
                self.spec_version = '1.2'
            elif 'bom-1.3' in inventory_type:
                self.spec_version = '1.3'
            elif 'bom-1.4' in inventory_type:
                self.spec_version = '1.4'
        except (AttributeError, TypeError):
            pass

    required_fields = ['bomFormat', 'specVersion', 'version']
    for field in required_fields:
        if field not in inventory:
            raise ValueError(f"Campo obbligatorio mancante: {field}")

    if inventory['specVersion'] != self.spec_version:
        raise ValueError(f"Versione della specifica non valida. Attesa: {self.spec_version}, Trovata: {inventory['specVersion']}")

    if 'components' in inventory:
        if not isinstance(inventory['components'], list):
            raise ValueError("Il campo 'components' deve essere una lista")
        
        for component in inventory['components']:
            if not isinstance(component, dict):
                raise ValueError("Ogni componente deve essere un dizionario")
            if 'name' not in component or 'version' not in component:
                raise ValueError("I componenti devono avere i campi 'name' e 'version'")

    return True