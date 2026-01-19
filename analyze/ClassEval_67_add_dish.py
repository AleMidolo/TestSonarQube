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
    for menu_item in self.menu:
        if menu_item['dish'] == dish['dish']:
            if menu_item['count'] >= dish['count']:
                self.selected_dishes.append(dish)
                menu_item['count'] -= dish['count']
                return True
    return False