class BookManagement: 
    def __init__(self):
        """
        Initialize the inventory of Book Manager.
        """
        self.inventory = {}

    def add_book(self, title, quantity=1):
        """
        Add one or several books to inventory which is sorted by book title.
        :param title: str, the book title
        :param quantity: int, default value is 1.
        """
        if title in self.inventory:
            self.inventory[title] += quantity
        else:
            self.inventory[title] = quantity

    def view_inventory(self):
        """
        Get the inventory of the Book Management.
        :return self.inventory: dictionary, {title(str): quantity(int), ...}
        >>> bookManagement = BookManagement()
        >>> bookManagement.add_book("book1", 1)
        >>> bookManagement.add_book("book2", 1)
        >>> bookManagement.view_inventory()
        {'book1': 1, 'book2': 1}
        """
        return self.inventory

    def view_book_quantity(self, title):
        """
        Get the quantity of a book.
        :param title: str, the title of the book.
        :return quantity: the quantity of this book title. return 0 when the title does not exist in self.inventory
        >>> bookManagement = BookManagement()
        >>> bookManagement.add_book("book1", 1)
        >>> bookManagement.view_book_quantity("book3")
        0
        """
        if title not in self.inventory:
            return 0
        return self.inventory[title]

    def remove_book(self, title, quantity):
        """
        इन्वेंटरी से एक या कई किताबें हटाएं जो किताब के शीर्षक द्वारा क्रमबद्ध है।
        अमान्य इनपुट मिलने पर झूठा उठाएं।
        :param title: str, किताब का शीर्षक
        :param quantity: int
        """
        if title not in self.inventory or quantity <= 0:
            raise ValueError("Invalid input")
        
        if self.inventory[title] < quantity:
            raise ValueError("Not enough books in inventory")
        
        self.inventory[title] -= quantity
        
        if self.inventory[title] == 0:
            del self.inventory[title]