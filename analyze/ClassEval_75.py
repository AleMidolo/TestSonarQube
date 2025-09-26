class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price, quantity=1):
        self.items[item] = self._create_item_entry(price, quantity)

    def _create_item_entry(self, price, quantity):
        return {'price': price, 'quantity': quantity}

    def remove_item(self, item, quantity=1):
        if item in self.items:
            self._decrease_item_quantity(item, quantity)

    def _decrease_item_quantity(self, item, quantity):
        self.items[item]['quantity'] -= quantity

    def view_items(self) -> dict:
        return self.items

    def total_price(self) -> float:
        return sum(self._calculate_item_total(item) for item in self.items.values())

    def _calculate_item_total(self, item):
        return item['quantity'] * item['price']