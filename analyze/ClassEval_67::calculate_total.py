def calculate_total(self):
    """
        计算已点菜品的总价格。将数量、价格和销售额相乘。
        :return total: float, 最终总价格。
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
        dish_price = dish['price']
        dish_count = dish['count']
        discount = self.sales.get(dish_name, 1.0)
        total += dish_price * dish_count * discount
    return total