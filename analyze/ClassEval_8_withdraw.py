def withdraw(self, amount):
    """
        खाते से एक निश्चित राशि निकालता है, खाते के संतुलन को कम करता है, वर्तमान खाते का संतुलन लौटाता है।
        यदि राशि नकारात्मक है, तो ValueError("अमान्य राशि") उठाएं।
        यदि निकासी राशि खाते के संतुलन से अधिक है, तो ValueError("पर्याप्त संतुलन नहीं है।") उठाएं।
        :param amount: int
        """
    if amount < 0:
        raise ValueError('Invalid amount')
    if amount > self.balance:
        raise ValueError('Insufficient balance.')
    self.balance -= amount
    return self.balance