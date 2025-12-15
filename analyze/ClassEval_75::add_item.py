class ShoppingCart: 
    def __init__(self):
        """
        Initialize the items representing the shopping list as an empty dictionary
        """
        self.items = {}

    def remove_item(self, item, quantity=1):
        """
        Subtract the specified quantity of item from the shopping list items
        :param item:string, Item to be subtracted in quantity
        :param quantity:int, Quantity to be subtracted
        :return:None
        >>> shoppingcart = ShoppingCart()
        >>> shoppingcart.add_item("apple", 1, 5)
        >>> shoppingcart.remove_item("apple", 3)
        >>> shoppingcart.view_items()
        {"apple":{"price":1, "quantity":2}}
        """
        if item in self.items:
            self.items[item]['quantity'] -= quantity
            if self.items[item]['quantity'] <= 0:
                del self.items[item]

    def view_items(self) -> dict:
        """
        Return the current shopping list items
        :return:dict, the current shopping list items
        >>> shoppingcart = ShoppingCart()
        >>> shoppingcart.add_item("apple", 1, 5)
        >>> shoppingcart.remove_item("apple", 3)
        >>> shoppingcart.view_items()
        {"apple":{"price":1, "quantity":2}}
        """
        return self.items
    
    def total_price(self) -> float:
        """
        Calculate the total price of all items in the shopping list, which is the quantity of each item multiplied by the price
        :return:float, the total price of all items in the shopping list
        >>> shoppingcart = ShoppingCart()
        >>> shoppingcart.add_item("apple", 1, 5)
        >>> shoppingcart.add_item("banana", 2, 3)
        >>> shoppingcart.total_price()
        11.0
        """
        return sum([item['quantity'] * item['price'] for item in self.items.values()])

    def add_item(self, item, price, quantity=1):
        """
        将商品信息添加到购物清单中，包括价格和数量。默认数量为1
        :param item: string, 要添加的商品
        :param price: float, 商品的价格
        :param quantity:int, 商品的数量，默认为1
        :return: None
        >>> shoppingcart = ShoppingCart()
        >>> shoppingcart.add_item("apple", 1, 5)
        >>> shoppingcart.view_items()
        {"apple":{"price":1, "quantity":5}}
        """
        if item in self.items:
            self.items[item]['quantity'] += quantity
        else:
            self.items[item] = {'price': price, 'quantity': quantity}