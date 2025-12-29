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
    dish_name = dish['dish']
    requested_count = dish['count']
    price = dish['price']
    for menu_item in self.menu:
        if menu_item['dish'] == dish_name and menu_item['price'] == price:
            if menu_item['count'] >= requested_count:
                menu_item['count'] -= requested_count
                found = False
                for selected in self.selected_dishes:
                    if selected['dish'] == dish_name and selected['price'] == price:
                        selected['count'] += requested_count
                        found = True
                        break
                if not found:
                    self.selected_dishes.append({'dish': dish_name, 'count': requested_count, 'price': price})
                return True
            else:
                return False
    return False