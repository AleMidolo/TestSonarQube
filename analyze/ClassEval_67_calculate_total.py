def calculate_total(self):
    """
        Calcular el precio total de los platos que han sido pedidos. Multiplicar la cantidad, el precio y las ventas.
        :return total: float, el precio total final.
        >>> order = Order()
        >>> order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        >>> order.sales = {"dish1": 0.8}
        >>> order.add_dish({"dish": "dish1", "price": 10, "count": 4})
        True
        >>> order.calculate_total()
        32.0
        """
    total = 0.0
    for dish in self.selected_dishes:
        dish_name = dish['dish']
        count = dish['count']
        price = dish['price']
        discount = self.sales.get(dish_name, 1.0)
        total += count * price * discount
    return total