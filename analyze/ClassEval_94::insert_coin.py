def insert_coin(self, amount):
    """
    वेंडिंग मशीन में सिक्के डालता है।
    :param amount: डालने के लिए सिक्कों की राशि, फ्लोट।
    :return: सिक्के डालने के बाद वेंडिंग मशीन का बैलेंस, फ्लोट।
    >>> vendingMachine = VendingMachine()
    >>> vendingMachine.insert_coin(1.25)
    1.25

    """
    self.balance += amount
    return self.balance