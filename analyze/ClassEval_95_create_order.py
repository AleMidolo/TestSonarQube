def create_order(self, order_id, product_id, quantity):
    """
    एक ऑर्डर बनाएं जिसमें उत्पाद की जानकारी शामिल हो, जैसे कि आईडी और मात्रा।
    और नए ऑर्डर को self.orders में डालें।
    स्थिति का डिफ़ॉल्ट मान 'Shipped' है।
    :param order_id: int
    :param product_id: int
    :param quantity: चयनित उत्पाद की मात्रा।
    :return False: केवल तभी यदि product_id इन्वेंटरी में नहीं है या मात्रा पर्याप्त नहीं है
    >>> warehouse.add_product(1, "product1", 3)
    >>> warehouse.create_order(1, 1, 2)
    >>> warehouse.orders
    {1: {'product_id': 1, 'quantity': 2, 'status': 'Shipped'}}
    >>> warehouse.create_order(1, 2, 2)
    False
    """
    # Check if product_id exists in inventory
    if product_id not in self.inventory:
        return False
    
    # Check if sufficient quantity is available
    if self.inventory[product_id]['quantity'] < quantity:
        return False
    
    # Create the order
    self.orders[order_id] = {
        'product_id': product_id,
        'quantity': quantity,
        'status': 'Shipped'
    }
    
    # Reduce the inventory quantity
    self.inventory[product_id]['quantity'] -= quantity