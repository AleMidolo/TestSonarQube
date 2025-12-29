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
    dish_name = dish['dish']
    requested_count = dish['count']
    price = dish['price']
    for menu_item in self.menu:
        if menu_item['dish'] == dish_name and menu_item['price'] == price:
            if menu_item['count'] >= requested_count:
                menu_item['count'] -= requested_count
                existing_dish = None
                for selected_dish in self.selected_dishes:
                    if selected_dish['dish'] == dish_name and selected_dish['price'] == price:
                        existing_dish = selected_dish
                        break
                if existing_dish:
                    existing_dish['count'] += requested_count
                else:
                    self.selected_dishes.append({'dish': dish_name, 'count': requested_count, 'price': price})
                return True
            else:
                return False
    return False