class BookManagement:
    def __init__(self):
        self.inventory = {}

    def add_book(self, title, quantity=1):
        self.inventory[title] = self.inventory.get(title, 0) + quantity

    def remove_book(self, title, quantity):
        if not self._can_remove_book(title, quantity):
            raise ValueError("Not enough books to remove or book does not exist.")
        self.inventory[title] -= quantity
        if self.inventory[title] == 0:
            del self.inventory[title]

    def view_inventory(self):
        return self.inventory

    def view_book_quantity(self, title):
        return self.inventory.get(title, 0)

    def _can_remove_book(self, title, quantity):
        return title in self.inventory and self.inventory[title] >= quantity