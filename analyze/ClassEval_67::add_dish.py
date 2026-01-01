def add_dish(self, dish):
    """
        Verifica el self.menu y añade a self.selected_dish si el conteo del plato es válido.
        Y si el plato ha sido añadido con éxito, cambia el conteo en self.menu.
        :param dish: dict, la información del plato. dish = {"dish": nombre del plato, "count": conteo, price: precio}
        :return: True si se añadió con éxito, o False en caso contrario.
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