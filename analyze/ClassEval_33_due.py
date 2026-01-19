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
    # Calculate total before discount
    total = sum(item['quantity'] * item['price'] for item in self.cart)
    
    # Apply discount using the promotion strategy
    discount = self.promotion(self)
    
    # Return final amount after discount
    return total - discount