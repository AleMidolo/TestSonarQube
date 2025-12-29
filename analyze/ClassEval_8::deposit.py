def deposit(self, amount):
    """
        Deposita un certo importo nel conto, aumentando il saldo del conto, restituisce il saldo attuale del conto.
        Se l'importo è negativo, solleva un ValueError("Importo non valido").
        :param amount: int
        """
    if amount < 0:
        raise ValueError('Importo non valido')
    self.balance += amount
    return self.balance