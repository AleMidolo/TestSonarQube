def checkout(self):
    """
    Realiza el pago de los platos pedidos. Si self.selected_dishes no está vacío, invoca el método calculate_total
    para realizar el pago.
    :return False si self.selected_dishes está vacío, o total (valor de retorno de calculate_total) en caso contrario.
    >>> order = Order()
    >>> order.menu.append({"dish": "dish1", "price": 10, "count": 5})
    >>> order.sales = {"dish1": 0.8}
    >>> order.add_dish({"dish": "dish1", "price": 10, "count": 4})
    True
    >>> order.checkout()
    32.0
    """
    if not self.selected_dishes:
        return False
    return self.calculate_total()