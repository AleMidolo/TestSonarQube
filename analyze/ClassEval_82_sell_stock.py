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
    # Buscar la acción en el portafolio
    for i, portfolio_stock in enumerate(self.portfolio):
        if portfolio_stock['name'] == stock['name']:
            # Verificar si hay suficiente cantidad para vender
            if portfolio_stock['quantity'] >= stock['quantity']:
                # Calcular el efectivo a agregar
                cash_to_add = stock['price'] * stock['quantity']
                self.cash_balance += cash_to_add
                
                # Reducir la cantidad de la acción
                portfolio_stock['quantity'] -= stock['quantity']
                
                # Si la cantidad llega a 0, eliminar la acción del portafolio
                if portfolio_stock['quantity'] == 0:
                    self.portfolio.pop(i)
                
                return True
            else:
                # No hay suficiente cantidad para vender
                return False
    
    # Si la acción no se encuentra en el portafolio
    return False