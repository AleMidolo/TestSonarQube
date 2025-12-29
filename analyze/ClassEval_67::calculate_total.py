def calculate_total(self):
    """
        Calcola il prezzo totale dei piatti che sono stati ordinati. Moltiplica il conteggio, il prezzo e le vendite.
        :return total: float, il prezzo totale finale.
        >>> order = Order()
        >>> order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        >>> order.sales = {"dish1": 0.8}
        >>> order.add_dish({"dish": "dish1", "price": 10, "count": 4})
        True
        >>> order.calculate_total()
        32.0
        """
    total = 0.0
    for selected in self.selected_dishes:
        dish_name = selected['dish']
        count = selected['count']
        price = selected['price']
        sales_multiplier = self.sales.get(dish_name, 1)
        total += count * price * sales_multiplier
    return total