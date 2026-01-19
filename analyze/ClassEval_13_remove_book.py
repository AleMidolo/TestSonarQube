def remove_book(self, title, quantity):
    """
    从按书名排序的库存中移除一本或多本书籍。
    如果输入无效则引发错误。
    :param title: str，书名
    :param quantity: int
    """
    if not isinstance(title, str) or not title.strip():
        raise ValueError("书名必须是非空字符串")
    
    if not isinstance(quantity, int) or quantity <= 0:
        raise ValueError("数量必须是正整数")
    
    if not hasattr(self, 'inventory'):
        raise AttributeError("库存不存在")
    
    if title not in self.inventory:
        raise KeyError(f"书籍 '{title}' 不在库存中")
    
    if self.inventory[title] < quantity:
        raise ValueError(f"库存不足：'{title}' 当前库存为 {self.inventory[title]}，无法移除 {quantity} 本")
    
    self.inventory[title] -= quantity
    
    if self.inventory[title] == 0:
        del self.inventory[title]