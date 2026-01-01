def view_items(self) -> dict:
    """
        वर्तमान शॉपिंग लिस्ट आइटम लौटाएं
        :return: dict, वर्तमान शॉपिंग लिस्ट आइटम
        >>> shoppingcart = ShoppingCart()
        >>> shoppingcart.add_item("apple", 1, 5)
        >>> shoppingcart.remove_item("apple", 3)
        >>> shoppingcart.view_items()
        {"apple":{"price":1, "quantity":2}}
        """
    return self.items