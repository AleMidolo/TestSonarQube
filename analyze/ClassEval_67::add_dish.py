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
    for item in self.menu:
        if item['dish'] == dish['dish'] and item['count'] >= dish['count']:
            self.selected_dishes.append(dish)
            item['count'] -= dish['count']
            return True
    return False