class Order:

    def __init__(self):
        self.menu = []
        self.selected_dishes = []
        self.sales = {}

    def add_dish(self, dish):
        menu_dish = self.find_menu_dish(dish["dish"])
        if menu_dish and self.is_dish_available(menu_dish, dish["count"]):
            menu_dish["count"] -= dish["count"]
            self.selected_dishes.append(dish)
            return True
        return False

    def find_menu_dish(self, dish_name):
        for menu_dish in self.menu:
            if menu_dish["dish"] == dish_name:
                return menu_dish
        return None

    def is_dish_available(self, menu_dish, count):
        return menu_dish["count"] >= count

    def calculate_total(self):
        return sum(dish["price"] * dish["count"] * self.sales[dish["dish"]] for dish in self.selected_dishes)

    def checkout(self):
        if not self.selected_dishes:
            return False
        total = self.calculate_total()
        self.selected_dishes.clear()
        return total