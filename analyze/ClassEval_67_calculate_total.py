def calculate_total(self):
    """
    उन व्यंजनों की कुल कीमत की गणना करें जो ऑर्डर किए गए हैं। गिनती, कीमत और बिक्री को गुणा करें।
    :return total: float, अंतिम कुल कीमत।
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
        
        # Get the sale multiplier for this dish (default to 1.0 if not in sales)
        sale_multiplier = self.sales.get(dish_name, 1.0)
        
        # Calculate: count * price * sale
        total += count * price * sale_multiplier
    
    return total