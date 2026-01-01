def add_product(self, product_id, name, quantity):
    """
    Aggiungi prodotto all'inventario e aumenta la quantità se esiste già nell'inventario.
    Altrimenti, aggiungi semplicemente un nuovo prodotto al dizionario.
    :param product_id: int
    :param name: str, nome del prodotto
    :param quantity: int, quantità del prodotto
    >>> warehouse.add_product(1, "product1", 3)
    >>> warehouse.inventory
    {1: {'name': 'product1', 'quantity': 3}}
    """
    if product_id in self.inventory:
        self.inventory[product_id]['quantity'] += quantity
    else:
        self.inventory[product_id] = {'name': name, 'quantity': quantity}