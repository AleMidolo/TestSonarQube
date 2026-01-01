def insert_coin(self, amount):
    """
        Inserta monedas en la máquina expendedora.
        :param amount: La cantidad de monedas a insertar, float.
        :return: El saldo de la máquina expendedora después de insertar las monedas, float.
        >>> vendingMachine = VendingMachine()
        >>> vendingMachine.insert_coin(1.25)
        1.25
        """
    self.balance += amount
    return self.balance