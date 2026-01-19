def calculate_total(self):
    """
    计算已点菜品的总价格。将数量、价格和销售额相乘。
    :return total: float, 最终总价格。
    >>> order = Order()
    >>> order.menu.append({"dish": "dish1", "price": 10, "count": 5})
    >>> order.sales = {"dish1": 0.8}
    >>> order.add_dish({"dish": "dish1", "price": 10, "count": 4})
    True
    >>> order.calculate_total()
    32.0
    """
    total = 0.0
    for item in self.menu:
        dish_name = item["dish"]
        price = item["price"]
        count = item["count"]
        
        # 获取销售折扣,如果没有则默认为1.0(无折扣)
        discount = self.sales.get(dish_name, 1.0)
        
        # 计算该菜品的总价: 数量 * 价格 * 折扣
        total += count * price * discount
    
    return total