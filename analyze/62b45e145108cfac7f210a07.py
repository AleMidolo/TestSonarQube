def validate(self, inventory, extract_spec_version=False):
    """
    Convalida un inventario specificato.

    Se `extract_spec_version` è impostato su `True`, verrà esaminato il valore del tipo (`type`) 
    per determinare la versione della specifica. Nel caso in cui non sia presente un valore per 
    il tipo o questo non sia valido, verranno eseguiti altri test basati sulla versione specificata 
    in `self.spec_version`.
    """
    if extract_spec_version:
        if 'type' in inventory and inventory['type'] in self.valid_types:
            return self.extract_version(inventory['type'])
        else:
            return self.spec_version

    # Esegui altri test di convalida basati su self.spec_version
    if self.spec_version == '1.0':
        return self.validate_v1(inventory)
    elif self.spec_version == '2.0':
        return self.validate_v2(inventory)
    else:
        raise ValueError("Versione della specifica non supportata.")