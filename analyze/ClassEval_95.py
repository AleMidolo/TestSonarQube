class Warehouse:
    def __init__(self):
        self.inventory = {}  # Product ID: Product
        self.orders = {}  # Order ID: Order

    def add_product(self, product_id, name, quantity):
        if product_id not in self.inventory:
            self.inventory[product_id] = {'name': name, 'quantity': quantity}
        else:
            self._increase_product_quantity(product_id, quantity)

    def update_product_quantity(self, product_id, quantity):
        if product_id in self.inventory:
            self._increase_product_quantity(product_id, quantity)

    def get_product_quantity(self, product_id):
        return self.inventory.get(product_id, {}).get('quantity', False)

    def create_order(self, order_id, product_id, quantity):
        if self._is_product_available(product_id, quantity):
            self._decrease_product_quantity(product_id, quantity)
            self.orders[order_id] = {'product_id': product_id, 'quantity': quantity, 'status': 'Shipped'}
        else:
            return False

    def change_order_status(self, order_id, status):
        if order_id in self.orders:
            self.orders[order_id]['status'] = status
        else:
            return False

    def track_order(self, order_id):
        return self.orders.get(order_id, {}).get('status', False)

    def _increase_product_quantity(self, product_id, quantity):
        self.inventory[product_id]['quantity'] += quantity

    def _decrease_product_quantity(self, product_id, quantity):
        self.inventory[product_id]['quantity'] -= quantity

    def _is_product_available(self, product_id, quantity):
        return self.get_product_quantity(product_id) >= quantity