def validate_as_prior_version(self, prior):
    """
    Verifica che "prior" sia una versione precedente valida dell'oggetto inventario corrente.

    La variabile di input "prior" deve essere un oggetto di tipo InventoryValidator
    e si presume che sia l'inventario corrente (self) sia l'inventario "prior" siano stati
    verificati per coerenza interna.
    """
    # Verifica che prior sia dello stesso tipo
    if not isinstance(prior, type(self)):
        raise TypeError("L'oggetto prior deve essere dello stesso tipo dell'inventario corrente")
        
    # Verifica che la data di prior sia precedente
    if prior.date >= self.date:
        raise ValueError("La data dell'inventario prior deve essere precedente a quella corrente")
        
    # Verifica che gli articoli in prior esistano anche nell'inventario corrente
    for item_id in prior.items:
        if item_id not in self.items:
            raise ValueError(f"L'articolo {item_id} presente in prior non esiste nell'inventario corrente")
            
    # Verifica che le quantità in prior non siano maggiori di quelle correnti
    for item_id in prior.items:
        if prior.items[item_id].quantity > self.items[item_id].quantity:
            raise ValueError(f"La quantità dell'articolo {item_id} in prior non può essere maggiore di quella corrente")
            
    return True