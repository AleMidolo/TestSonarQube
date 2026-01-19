def add_dish(self, dish):
    """
        Check the self.menu and add into self.selected_dish if the dish count is valid.
        And if the dish has successfully been added, change the count in self.menu.
        :param dish: dict, the information of dish. dish = {"dish": dish name, "count": count, price: price}
        :return: True if successfully added, or False otherwise.
        >>> order = Order()
        >>> order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        >>> order.add_dish({"dish": "dish1", "price": 10, "count": 3})
        True
        """
    for menu_item in self.menu:
        if menu_item['dish'] == dish['dish']:
            if menu_item['count'] >= dish['count']:
                self.selected_dishes.append(dish)
                menu_item['count'] -= dish['count']
                return True
    return False