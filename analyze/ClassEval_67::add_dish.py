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
                existing_selected = None
                for selected in self.selected_dishes:
                    if selected['dish'] == dish_name and selected['price'] == price:
                        existing_selected = selected
                        break
                if existing_selected:
                    existing_selected['count'] += requested_count
                else:
                    self.selected_dishes.append({'dish': dish_name, 'count': requested_count, 'price': price})
                return True
            else:
                return False
    return False