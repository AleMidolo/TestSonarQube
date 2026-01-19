def checkout(self):
    """
        结账所点的菜品。如果 self.selected_dishes 不为空，调用 calculate_total 方法进行结账。
        :return 如果 self.selected_dishes 为空则返回 False，否则返回总金额（calculate_total 的返回值）。
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