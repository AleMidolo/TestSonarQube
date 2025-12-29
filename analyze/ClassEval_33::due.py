def due(self):
    """
        छूट लागू करने के बाद भुगतान करने के लिए अंतिम राशि की गणना करें।
        :return: float, भुगतान करने के लिए अंतिम राशि
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        >>> ds = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
        >>> ds.due()
        312.55

        """
    total = self.total()
    discount = self.promotion(self) if self.promotion else 0
    return total - discount