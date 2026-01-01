def add_product(self, product_id, name, quantity):
    """
        इन्वेंटरी में उत्पाद जोड़ें और यदि यह पहले से इन्वेंटरी में मौजूद है तो मात्रा को बढ़ाएं।
        अन्यथा, बस नए उत्पाद को डिक्ट में जोड़ें।
        :param product_id: int
        :param name: str, उत्पाद का नाम
        :param quantity: int, उत्पाद की मात्रा
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.inventory
        {1: {'name': 'product1', 'quantity': 3}}
        """
    if product_id in self.inventory:
        self.inventory[product_id]['quantity'] += quantity
    else:
        self.inventory[product_id] = {'name': name, 'quantity': quantity}