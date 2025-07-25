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
            if 'CycloneDX' in inventory_type:
                version_match = re.search(r'(\d+\.\d+)', inventory_type)
                if version_match:
                    self.spec_version = version_match.group(1)
        except (AttributeError, TypeError):
            pass

    required_fields = ['bomFormat', 'specVersion', 'version', 'components']
    
    for field in required_fields:
        if field not in inventory:
            raise ValueError(f"Campo obbligatorio mancante: {field}")
            
    if inventory['bomFormat'] != 'CycloneDX':
        raise ValueError("Il formato BOM deve essere 'CycloneDX'")
        
    if not isinstance(inventory['components'], list):
        raise ValueError("Il campo 'components' deve essere una lista")
        
    try:
        version = float(inventory['specVersion'])
        if version < 1.0:
            raise ValueError("La versione della specifica deve essere >= 1.0")
    except ValueError:
        raise ValueError("Versione della specifica non valida")
        
    return True