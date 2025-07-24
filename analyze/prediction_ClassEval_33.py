class DiscountStrategy:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = cart
        self.promotion = promotion
        self.__total = self.calculate_total()

    def calculate_total(self):
        return sum(item['quantity'] * item['price'] for item in self.cart)

    def due(self):
        discount = self.calculate_discount()
        return self.__total - discount

    def calculate_discount(self):
        if self.promotion is None:
            return 0
        return self.promotion(self)

    @staticmethod
    def FidelityPromo(order):
        return order.calculate_total() * 0.05 if order.customer['fidelity'] >= 1000 else 0

    @staticmethod
    def BulkItemPromo(order):
        return sum(item['quantity'] * item['price'] * 0.1 for item in order.cart if item['quantity'] >= 20)

    @staticmethod
    def LargeOrderPromo(order):
        return order.calculate_total() * 0.07 if len({item['product'] for item in order.cart}) >= 10 else 0