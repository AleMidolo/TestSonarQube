def add_dish(self, dish):
    """
        检查 self.menu 并在 dish 数量有效时添加到 self.selected_dish 中。
        如果菜品成功添加，则更改 self.menu 中的数量。
        :param dish: dict，菜品的信息。 dish = {"dish": 菜品名称, "count": 数量, price: 价格}
        :return: 如果成功添加则返回 True，否则返回 False。
        >>> order = Order()
        >>> order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        >>> order.add_dish({"dish": "dish1", "price": 10, "count": 3})
        True
        """
    for menu_item in self.menu:
        if menu_item['dish'] == dish['dish'] and menu_item['count'] >= dish['count']:
            self.selected_dishes.append(dish)
            menu_item['count'] -= dish['count']
            return True
    return False