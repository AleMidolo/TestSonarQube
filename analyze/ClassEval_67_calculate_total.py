def calculate_total(self):
    """
    Calculate the total price of dishes that have been ordered. Multiply the count, price and sales.
    :return total: float, the final total price.
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
        
        # Get the sales discount for this dish, default to 1.0 (no discount) if not found
        discount = self.sales.get(dish_name, 1.0)
        
        # Calculate: count * price * discount
        total += count * price * discount
    
    return total