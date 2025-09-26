class Order:

    def __init__(self):
        self.menu = []
        self.selected_dishes = []
        self.sales = {}

    def add_dish(self, dish):
        if not self.is_dish_available(dish):
            return False
        self.update_menu_count(dish)
        self.selected_dishes.append(dish)
        return True

    def is_dish_available(self, dish):
        for menu_dish in self.menu:
            if dish["dish"] == menu_dish["dish"]:
                return menu_dish["count"] >= dish["count"]
        return False

    def update_menu_count(self, dish):
        for menu_dish in self.menu:
            if dish["dish"] == menu_dish["dish"]:
                menu_dish["count"] -= dish["count"]
                break

    def calculate_total(self):
        return sum(self.calculate_dish_total(dish) for dish in self.selected_dishes)

    def calculate_dish_total(self, dish):
        return dish["price"] * dish["count"] * self.sales[dish["dish"]]

    def checkout(self):
        if self.is_empty_order():
            return False
        total = self.calculate_total()
        self.clear_selected_dishes()
        return total

    def is_empty_order(self):
        return len(self.selected_dishes) == 0

    def clear_selected_dishes(self):
        self.selected_dishes = []