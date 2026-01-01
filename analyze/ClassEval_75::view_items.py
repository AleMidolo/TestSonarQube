def view_items(self) -> dict:
    """
        Devuelve los elementos actuales de la lista de compras
        :return: dict, los elementos actuales de la lista de compras
        >>> shoppingcart.add_item("apple", 1, 5)
        >>> shoppingcart.remove_item("apple", 3)
        >>> shoppingcart.view_items()
        {"apple":{"price":1, "quantity":2}}
        """
    return self.items.copy()