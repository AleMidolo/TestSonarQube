class Warehouse: 
    def __init__(self):
        """
        Initialize two fields.
        self.inventory is a dict that stores the products.
        self.inventory = {Product ID: Product}
        self.orders is a dict that stores the products in a order.
        self.orders = {Order ID: Order}
        """
        self.inventory = {}  # Product ID: Product
        self.orders = {}  # Order ID: Order

    def add_product(self, product_id, name, quantity):
        """
        Add product to inventory and plus the quantity if it has existed in inventory.
        Or just add new product to dict otherwise.
        :param product_id: int
        :param name: str, product name
        :param quantity: int, product quantity
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.inventory
        {1: {'name': 'product1', 'quantity': 3}}
        """
        if product_id not in self.inventory:
            self.inventory[product_id] = {'name': name, 'quantity': quantity}
        else:
            self.inventory[product_id]['quantity'] += quantity

    def update_product_quantity(self, product_id, quantity):
        """
        According to product_id, add the quantity to the corresponding product in inventory.
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.update_product_quantity(1, -1)
        >>> warehouse.inventory
        {1: {'name': 'product1', 'quantity': 2}}
        """
        if product_id in self.inventory:
            self.inventory[product_id]['quantity'] += quantity

    def get_product_quantity(self, product_id):
        """
        Get the quantity of specific product by product_id.
        :param product_id, int
        :return: if the product_id is in inventory then return the corresponding quantity,
                or False otherwise.
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.get_product_quantity(1)
        3
        >>> warehouse.get_product_quantity(2)
        False
        """
        if product_id in self.inventory:
            return self.inventory[product_id]['quantity']
        else:
            return False

    def change_order_status(self, order_id, status):
        """
        Change the status of order if the input order_id is in self.orders.
        :param order_id: int
        :param status: str, the state that is going to change to
        :return False: only if the order_id is not in self.orders
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.create_order(1, 1, 2)
        >>> warehouse.change_order_status(1, "done")
        >>> warehouse.orders
        {1: {'product_id': 1, 'quantity': 2, 'status': 'done'}}
        """
        if order_id in self.orders:
            self.orders[order_id]['status'] = status
        else:
            return False

    def track_order(self, order_id):
        """
        Get the status of specific order.
        :param order_id: int
        :return False: only if the order_id is not in self.orders.
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.create_order(1, 1, 2)
        >>> warehouse.track_order(1)
        'Shipped'
        """
        if order_id in self.orders:
            return self.orders[order_id]['status']
        else:
            return False

    def create_order(self, order_id, product_id, quantity):
        """
        创建一个订单，其中包含产品的信息，如ID和数量。
        并将新订单放入self.orders中。
        状态的默认值为'Shipped'。
        :param order_id: int
        :param product_id: int
        :param quantity: 被选择的产品数量。
        :return False: 仅当product_id不在库存中或数量不足时
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.create_order(1, 1, 2)
        >>> warehouse.orders
        {1: {'product_id': 1, 'quantity': 2, 'status': 'Shipped'}}
        >>> warehouse.create_order(1, 2, 2)
        False
        """
        if product_id not in self.inventory or self.inventory[product_id]['quantity'] < quantity:
            return False
        self.orders[order_id] = {'product_id': product_id, 'quantity': quantity, 'status': 'Shipped'}
        self.inventory[product_id]['quantity'] -= quantity