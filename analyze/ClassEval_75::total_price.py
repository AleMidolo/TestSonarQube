def total_price(self) -> float:
    """
        Calcola il prezzo totale di tutti gli articoli nella lista della spesa, che è la quantità di ciascun articolo moltiplicata per il prezzo
        :return: float, il prezzo totale di tutti gli articoli nella lista della spesa
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