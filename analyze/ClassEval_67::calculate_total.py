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

    def add_dish(self, dish):
        """
        Check the self.menu and add into self.selected_dish if the dish count is valid.
        And if the dish has successfully been added, change the count in self.menu.
        :param dish: dict, the information of dish. dish = {"dish": dish name, "count": count, price: price}
        :return: True if successfully added, or False otherwise.
        >>> order = Order()
        >>> order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        >>> order.add_dish({"dish": "dish1", "price": 10, "count": 3})
        True
        """
        for menu_dish in self.menu:
            if dish["dish"] == menu_dish["dish"]:
                if menu_dish["count"] < dish["count"]:
                    return False
                else:
                    menu_dish["count"] -= dish["count"]
                    break
        self.selected_dishes.append(dish)
        return True
    
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
    
    def calculate_total(self):
        """
        उन व्यंजनों की कुल कीमत की गणना करें जो ऑर्डर किए गए हैं। गिनती, कीमत और बिक्री को गुणा करें।
        :return total: float, अंतिम कुल कीमत।
        >>> order = Order()
        >>> order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        >>> order.sales = {"dish1": 0.8}
        >>> order.add_dish({"dish": "dish1", "price": 10, "count": 4})
        True
        >>> order.calculate_total()
        32.0
        """
        total = 0.0
        for dish in self.selected_dishes:
            price = dish["price"] * self.sales.get(dish["dish"], 1)
            total += price * dish["count"]
        return total