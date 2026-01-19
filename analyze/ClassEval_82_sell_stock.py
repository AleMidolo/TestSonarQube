def sell_stock(self, stock):
    """
    Vender una acción y eliminarla del portafolio y agregar el efectivo al saldo de efectivo.
    :param stock: un diccionario con las claves "name", "price" y "quantity"
    :param quantity: la cantidad de la acción a vender, int.
    :return: True si la acción se vendió con éxito, False si la cantidad de la acción no es suficiente.
    >>> tracker = StockPortfolioTracker(10000.0)
    >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
    >>> tracker.sell_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
    True
    >>> tracker.portfolio
    []

    """
    stock_name = stock["name"]
    quantity_to_sell = stock["quantity"]
    price = stock["price"]
    
    # Buscar la acción en el portafolio
    for portfolio_stock in self.portfolio:
        if portfolio_stock["name"] == stock_name:
            # Verificar si hay suficiente cantidad
            if portfolio_stock["quantity"] >= quantity_to_sell:
                # Calcular el efectivo a agregar
                cash_to_add = price * quantity_to_sell
                self.cash_balance += cash_to_add
                
                # Reducir la cantidad o eliminar la acción
                portfolio_stock["quantity"] -= quantity_to_sell
                
                # Si la cantidad llega a 0, eliminar del portafolio
                if portfolio_stock["quantity"] == 0:
                    self.portfolio.remove(portfolio_stock)
                
                return True
            else:
                return False
    
    # Si la acción no se encuentra en el portafolio
    return False