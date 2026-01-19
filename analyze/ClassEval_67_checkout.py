def checkout(self):
    """
        Controlla i piatti ordinati. SE self.selected_dishes non è vuoto, invoca il metodo calculate_total
        per procedere al checkout.
        :return False se self.selected_dishes è vuoto, o il totale (valore di ritorno di calculate_total) altrimenti.
        >>> order = Order()
        >>> order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        >>> order.sales = {"dish1": 0.8}
        >>> order.add_dish({"dish": "dish1", "price": 10, "count": 4})
        True
        >>> order.checkout()
        32.0
        """
    if not self.selected_dishes:
        return False
    return self.calculate_total()