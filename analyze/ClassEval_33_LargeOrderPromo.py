@staticmethod
def LargeOrderPromo(order):
    """
    Calcola lo sconto basato sul numero di prodotti diversi nell'ordine. Se la quantità di prodotti diversi nell'ordine raggiunge 10 o più, l'intero ordine godrà di uno sconto del 7%.
    :param order: oggetto, l'ordine a cui applicare lo sconto
    :return: float, importo dello sconto
    >>> customer = {'name': 'John Doe', 'fidelity': 1200}
    >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
    >>> order = DiscountStrategy(customer, cart, DiscountStrategy.LargeOrderPromo)
    >>> DiscountStrategy.LargeOrderPromo(order)
    0.0

    """
    # Conta il numero di prodotti diversi nel carrello
    distinct_products = len(order.cart)
    
    # Se ci sono 10 o più prodotti diversi, applica uno sconto del 7%
    if distinct_products >= 10:
        # Calcola il totale dell'ordine
        total = sum(item['quantity'] * item['price'] for item in order.cart)
        # Restituisce il 7% del totale come sconto
        return total * 0.07
    
    # Nessuno sconto se ci sono meno di 10 prodotti diversi
    return 0.0