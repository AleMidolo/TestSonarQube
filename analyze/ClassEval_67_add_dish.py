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
    dish_name = dish['dish']
    requested_count = dish['count']
    price = dish['price']
    for menu_item in self.menu:
        if menu_item['dish'] == dish_name and menu_item['price'] == price:
            if menu_item['count'] >= requested_count:
                menu_item['count'] -= requested_count
                existing_dish = None
                for selected_dish in self.selected_dishes:
                    if selected_dish['dish'] == dish_name and selected_dish['price'] == price:
                        existing_dish = selected_dish
                        break
                if existing_dish:
                    existing_dish['count'] += requested_count
                else:
                    self.selected_dishes.append({'dish': dish_name, 'count': requested_count, 'price': price})
                return True
            else:
                return False
    return False