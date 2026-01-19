def total_price(self) -> float:
    """
        खरीदारी सूची में सभी वस्तुओं की कुल कीमत की गणना करें, जो प्रत्येक वस्तु की मात्रा को उसकी कीमत से गुणा करके प्राप्त होती है
        :return:float, खरीदारी सूची में सभी वस्तुओं की कुल कीमत
        >>> shoppingcart = ShoppingCart()
        >>> shoppingcart.add_item("सेब", 1, 5)
        >>> shoppingcart.add_item("केला", 2, 3)
        >>> shoppingcart.total_price()
        11.0
        """
    total = 0.0
    for item, details in self.items.items():
        total += details['price'] * details['quantity']
    return total