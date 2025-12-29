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
    for dish in self.selected_dishes:
        dish_name = dish['dish']
        price = dish['price']
        count = dish['count']
        discount = self.sales.get(dish_name, 1.0)
        total += price * count * discount
    return total