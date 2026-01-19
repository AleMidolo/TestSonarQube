def add_dish(self, dish):
    """
    检查 self.menu 并在 dish 数量有效时添加到 self.selected_dish 中。
    如果菜品成功添加，则更改 self.menu 中的数量。
    :param dish: dict，菜品的信息。 dish = {"dish": 菜品名称, "count": 数量, price: 价格}
    :return: 如果成功添加则返回 True，否则返回 False。
    >>> order = Order()
    >>> order.menu.append({"dish": "dish1", "price": 10, "count": 5})
    >>> order.add_dish({"dish": "dish1", "price": 10, "count": 3})
    True
    """
    # 在菜单中查找对应的菜品
    for menu_item in self.menu:
        if menu_item["dish"] == dish["dish"]:
            # 检查菜单中的数量是否足够
            if menu_item["count"] >= dish["count"]:
                # 减少菜单中的数量
                menu_item["count"] -= dish["count"]
                
                # 检查 selected_dish 中是否已有该菜品
                found = False
                for selected_item in self.selected_dish:
                    if selected_item["dish"] == dish["dish"]:
                        # 如果已存在，增加数量
                        selected_item["count"] += dish["count"]
                        found = True
                        break
                
                # 如果不存在，添加新菜品
                if not found:
                    self.selected_dish.append({
                        "dish": dish["dish"],
                        "price": dish["price"],
                        "count": dish["count"]
                    })
                
                return True
            else:
                # 数量不足
                return False
    
    # 菜品不在菜单中
    return False