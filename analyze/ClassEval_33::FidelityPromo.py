@staticmethod
def FidelityPromo(order):
    """
        ग्राहक के निष्ठा अंकों के आधार पर छूट की गणना करें। 1000 अंकों से अधिक वाले ग्राहकों को पूरे आदेश पर 5% छूट का आनंद मिल सकता है।
        :param order: object, वह आदेश जिस पर छूट लागू करनी है
        :return: float, छूट की राशि
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        >>> order = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
        >>> DiscountStrategy.FidelityPromo(order)
        16.45

        """
    if order.customer.get('fidelity', 0) > 1000:
        return order.total() * 0.05
    return 0