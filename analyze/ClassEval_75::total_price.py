def total_price(self) -> float:
    """
        Calcula el precio total de todos los artículos en la lista de compras, que es la cantidad de cada artículo multiplicada por el precio
        :return: float, el precio total de todos los artículos en la lista de compras
        >>> shoppingcart = ShoppingCart()
        >>> shoppingcart.add_item("apple", 1, 5)
        >>> shoppingcart.add_item("banana", 2, 3)
        >>> shoppingcart.total_price()
        11.0
        """
    total = 0.0
    for item in self.items.values():
        total += item['price'] * item['quantity']
    return total