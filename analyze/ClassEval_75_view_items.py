def view_items(self) -> dict:
    """
    返回当前购物清单项目
    :return: dict，当前购物清单项目
    >>> shoppingcart.add_item("apple", 1, 5)
    >>> shoppingcart.remove_item("apple", 3)
    >>> shoppingcart.view_items()
    {"apple":{"price":1, "quantity":2}}
    """
    return self.items