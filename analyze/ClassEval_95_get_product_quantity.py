def get_product_quantity(self, product_id):
    """
    विशेष उत्पाद की मात्रा प्राप्त करें product_id द्वारा।
    :param product_id, int
    :return: यदि product_id इन्वेंटरी में है तो संबंधित मात्रा लौटाएं,
            अन्यथा False लौटाएं।
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