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
    for item in self.menu:
        dish_name = item["dish"]
        price = item["price"]
        count = item["count"]
        
        # Get the sales multiplier for this dish (default to 1.0 if not in sales)
        sales_multiplier = self.sales.get(dish_name, 1.0)
        
        # Calculate: count * price * sales_multiplier
        total += count * price * sales_multiplier
    
    return total