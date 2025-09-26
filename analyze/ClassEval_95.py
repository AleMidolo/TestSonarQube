class Warehouse:
    def __init__(self):
        self.inventory = {}  # Product ID: Product
        self.orders = {}  # Order ID: Order

    def add_product(self, product_id, name, quantity):
        if product_id not in self.inventory:
            self.inventory[product_id] = self._create_product(name, quantity)
        else:
            self._increase_product_quantity(product_id, quantity)

    def _create_product(self, name, quantity):
        return {'name': name, 'quantity': quantity}

    def _increase_product_quantity(self, product_id, quantity):
        self.inventory[product_id]['quantity'] += quantity

    def update_product_quantity(self, product_id, quantity):
        if self._product_exists(product_id):
            self._increase_product_quantity(product_id, quantity)

    def _product_exists(self, product_id):
        return product_id in self.inventory

    def get_product_quantity(self, product_id):
        if self._product_exists(product_id):
            return self.inventory[product_id]['quantity']
        return False

    def create_order(self, order_id, product_id, quantity):
        if self._is_orderable(product_id, quantity):
            self._decrease_product_quantity(product_id, quantity)
            self.orders[order_id] = self._create_order(product_id, quantity)
        else:
            return False

    def _is_orderable(self, product_id, quantity):
        return self.get_product_quantity(product_id) >= quantity

    def _decrease_product_quantity(self, product_id, quantity):
        self.update_product_quantity(product_id, -quantity)

    def _create_order(self, product_id, quantity):
        return {'product_id': product_id, 'quantity': quantity, 'status': 'Shipped'}

    def change_order_status(self, order_id, status):
        if self._order_exists(order_id):
            self.orders[order_id]['status'] = status
        return False

    def _order_exists(self, order_id):
        return order_id in self.orders

    def track_order(self, order_id):
        if self._order_exists(order_id):
            return self.orders[order_id]['status']
        return False