def due(self):
    """
        计算应用折扣后的最终支付金额。
        :return: float，最终支付金额
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        >>> ds = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
        >>> ds.due()
        312.55

        """
    total = self.total()
    discount = self.promotion(self) if self.promotion else 0
    return total - discount