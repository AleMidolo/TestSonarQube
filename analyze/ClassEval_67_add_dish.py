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
    # Cerca il piatto nel menu
    for menu_item in self.menu:
        if menu_item["dish"] == dish["dish"]:
            # Controlla se il conteggio richiesto è valido (disponibile nel menu)
            if menu_item["count"] >= dish["count"]:
                # Aggiungi il piatto a selected_dish
                self.selected_dish.append(dish)
                # Decrementa il conteggio nel menu
                menu_item["count"] -= dish["count"]
                return True
            else:
                # Conteggio non valido (non abbastanza disponibile)
                return False
    
    # Piatto non trovato nel menu
    return False