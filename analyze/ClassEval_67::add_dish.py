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
    dish_name = dish['dish']
    requested_count = dish['count']
    for menu_item in self.menu:
        if menu_item['dish'] == dish_name:
            if menu_item['count'] >= requested_count:
                menu_item['count'] -= requested_count
                found = False
                for selected_dish in self.selected_dishes:
                    if selected_dish['dish'] == dish_name:
                        selected_dish['count'] += requested_count
                        found = True
                        break
                if not found:
                    self.selected_dishes.append({'dish': dish_name, 'count': requested_count, 'price': dish['price']})
                return True
            else:
                return False
    return False