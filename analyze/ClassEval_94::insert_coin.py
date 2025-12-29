def insert_coin(self, amount):
    """
    Inserisce monete nel distributore automatico.
    :param amount: L'importo delle monete da inserire, float.
    :return: Il saldo del distributore automatico dopo che le monete sono state inserite, float.
    >>> vendingMachine = VendingMachine()
    >>> vendingMachine.insert_coin(1.25)
    1.25

    """
    self.balance += amount
    return self.balance