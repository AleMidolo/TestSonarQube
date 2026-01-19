def due(self):
    """
        Calcola l'importo finale da pagare dopo aver applicato lo sconto.
        :return: float, importo finale da pagare
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        >>> ds = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
        >>> ds.due()
        312.55

        """
    if self.promotion:
        discount = self.promotion(self)
        return self.total() - discount
    return self.total()