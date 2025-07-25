class VendingMachine:
    def __init__(self):
        self.inventory = {}
        self.balance = 0

    def add_item(self, item_name, price, quantity):
        if not self.restock_item(item_name, quantity):
            self.inventory[item_name] = self.create_item(price, quantity)

    def create_item(self, price, quantity):
        return {'price': price, 'quantity': quantity}

    def insert_coin(self, amount):
        self.balance += amount
        return self.balance

    def purchase_item(self, item_name):
        item = self.get_item(item_name)
        if item and self.can_purchase(item):
            self.process_purchase(item)
            return self.balance
        return False

    def get_item(self, item_name):
        return self.inventory.get(item_name)

    def can_purchase(self, item):
        return item['quantity'] > 0 and self.balance >= item['price']

    def process_purchase(self, item):
        self.balance -= item['price']
        item['quantity'] -= 1

    def restock_item(self, item_name, quantity):
        if item_name in self.inventory:
            self.inventory[item_name]['quantity'] += quantity
            return True
        return False

    def display_items(self):
        if not self.inventory:
            return False
        return self.format_items()

    def format_items(self):
        items = [f"{item_name} - ${item_info['price']} [{item_info['quantity']}]" 
                 for item_name, item_info in self.inventory.items()]
        return "\n".join(items)