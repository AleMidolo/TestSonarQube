def withdraw(self, amount):
    """
    Preleva un certo importo dal conto, diminuendo il saldo del conto, restituisce il saldo attuale del conto.
    Se l'importo è negativo, solleva un ValueError("Importo non valido").
    Se l'importo del prelievo è maggiore del saldo del conto, solleva un ValueError("Saldo insufficiente.").
    :param amount: int
    """
    if amount < 0:
        raise ValueError("Importo non valido")
    
    if amount > self.saldo:
        raise ValueError("Saldo insufficiente.")
    
    self.saldo -= amount
    return self.saldo