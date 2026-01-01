@staticmethod
def FidelityPromo(order):
    """
        Calcola lo sconto basato sui punti fedeltà del cliente. I clienti con oltre 1000 punti possono godere di uno sconto del 5% sull'intero ordine.
        :param order: oggetto, l'ordine a cui applicare lo sconto
        :return: float, importo dello sconto
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        >>> order = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
        >>> DiscountStrategy.FidelityPromo(order)
        16.45

        """
    return order.total() * 0.05 if order.customer['fidelity'] > 1000 else 0