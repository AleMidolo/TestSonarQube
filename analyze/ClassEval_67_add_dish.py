def add_dish(self, dish):
    """
    self.menu की जांच करें और यदि डिश की संख्या मान्य है तो self.selected_dish में जोड़ें।
    और यदि डिश सफलतापूर्वक जोड़ी गई है, तो self.menu में संख्या बदलें।
    :param dish: dict, डिश की जानकारी। dish = {"dish": डिश का नाम, "count": संख्या, price: मूल्य}
    :return: यदि सफलतापूर्वक जोड़ा गया तो True, अन्यथा False।
    >>> order = Order()
    >>> order.menu.append({"dish": "dish1", "price": 10, "count": 5})
    >>> order.add_dish({"dish": "dish1", "price": 10, "count": 3})
    True
    """
    # self.menu में डिश खोजें
    for menu_item in self.menu:
        if menu_item["dish"] == dish["dish"]:
            # जांचें कि क्या पर्याप्त संख्या उपलब्ध है
            if menu_item["count"] >= dish["count"]:
                # self.selected_dish में जोड़ें
                self.selected_dish.append(dish)
                # self.menu में संख्या घटाएं
                menu_item["count"] -= dish["count"]
                return True
            else:
                # पर्याप्त संख्या उपलब्ध नहीं है
                return False
    
    # डिश menu में नहीं मिली
    return False