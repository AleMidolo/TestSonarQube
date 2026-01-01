def add_dish(self, dish):
    """
        Controlla il self.menu e aggiungi in self.selected_dish se il conteggio del piatto è valido.
        E se il piatto è stato aggiunto con successo, cambia il conteggio in self.menu.
        :param dish: dict, le informazioni del piatto. dish = {"dish": nome del piatto, "count": conteggio, price: prezzo}
        :return: True se aggiunto con successo, altrimenti False.
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