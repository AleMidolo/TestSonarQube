def deposit(self, amount):
    """
        Deposita una cierta cantidad en la cuenta, aumentando el saldo de la cuenta, y devuelve el saldo actual de la cuenta.
        Si la cantidad es negativa, se genera un ValueError("Cantidad inválida").
        :param amount: int
        """
    if amount < 0:
        raise ValueError('Cantidad inválida')
    self.balance += amount
    return self.balance