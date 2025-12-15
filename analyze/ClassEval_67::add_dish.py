class Order: 
    def __init__(self):
        """
        Initialize the order management system
        self.menu stores the dishes of resturant inventory
        menu = [{"dish": dish name, "price": price, "count": count}, ...]
        self.selected_dishes stores the dished selected by customer
        selected_dish = {"dish": dish name, "count": count, price: price}
        self.sales stores the sales of each dish
        sales = {dish name: sales}
        """
        self.menu = []
        self.selected_dishes = []
        self.sales = {}

    def calculate_total(self):
        """
        Calculate the total price of dishes that have been ordered. Multiply the count, price and sales.
        :return total: float, the final total price.
        >>> order = Order()
        >>> order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        >>> order.sales = {"dish1": 0.8}
        >>> order.add_dish({"dish": "dish1", "price": 10, "count": 4})
        True
        >>> order.calculate_total()
        32.0
        """
        total = 0
        for dish in self.selected_dishes:
            total += dish["price"] * dish["count"] * self.sales[dish["dish"]]
        return total
    
    def checkout(self):
        """
        Check out the dished ordered. IF the self.selected_dishes is not empty, invoke the calculate_total
        method to check out.
        :return Flase if the self.selected_dishes is empty, or total(return value of calculate_total) otherwise.
        >>> order = Order()
        >>> order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        >>> order.sales = {"dish1": 0.8}
        >>> order.add_dish({"dish": "dish1", "price": 10, "count": 4})
        True
        >>> order.checkout()
        32.0
        """
        if len(self.selected_dishes) == 0:
            return False
        total = self.calculate_total()
        self.selected_dishes = []
        return total
    
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
            if menu_item["dish"] == dish["dish"]:
                if menu_item["count"] >= dish["count"]:
                    self.selected_dishes.append(dish)
                    menu_item["count"] -= dish["count"]
                    return True
        return False