def view_items(self) -> dict:
    """
    Restituisce gli  Restituisce gli articoli attualmente presenti nella lista della spesa.
    :return: dict, gli attuali articoli della lista della spesa
    >>> shoppingcart.add_item("apple", 1, 5)
    >>> shoppingcart.remove_item("apple", 3)
    >>> shoppingcart.view_items()
    {"apple":{"price":1, "quantity":2}}
    """
    return self.items