import math

def cos(self, x):
    """
    x-डिग्री कोण का कोस मान निकालें
    :param x:float
    :return:float
    >>> tricalculator = TriCalculator()
    >>> tricalculator.cos(60)
    0.5
    """
    # Convert degrees to radians and calculate cosine
    radians = math.radians(x)
    return math.cos(radians)