def deposit(self, amount):
    """
        खाते में एक निश्चित राशि जमा करता है, खाते के संतुलन को बढ़ाता है, वर्तमान खाते के संतुलन को लौटाता है।
        यदि राशि नकारात्मक है, तो ValueError("अमान्य राशि") उठाएं।
        :param amount: int
        """
    if amount < 0:
        raise ValueError('अमान्य राशि')
    self.balance += amount
    return self.balance