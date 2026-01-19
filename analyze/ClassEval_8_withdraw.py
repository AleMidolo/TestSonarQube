def withdraw(self, amount):
    """
    Retira una cierta cantidad de la cuenta, disminuyendo el saldo de la cuenta, y devuelve el saldo actual de la cuenta.
    Si la cantidad es negativa, se genera un ValueError("Cantidad inválida").
    Si la cantidad de retiro es mayor que el saldo de la cuenta, se genera un ValueError("Saldo insuficiente.").
    :param amount: int
    """
    if amount < 0:
        raise ValueError("Cantidad inválida")
    if amount > self.balance:
        raise ValueError("Saldo insuficiente.")
    self.balance -= amount
    return self.balance