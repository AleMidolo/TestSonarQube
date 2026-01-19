def view_book_quantity(self, title):
    """
    एक पुस्तक की मात्रा प्राप्त करें।
    :param title: str, पुस्तक का शीर्षक।
    :return quantity: इस पुस्तक के शीर्षक की मात्रा। जब शीर्षक self.inventory में मौजूद नहीं हो तो 0 लौटाएं।
    >>> bookManagement = BookManagement()
    >>> bookManagement.add_book("book1", 1)
    >>> bookManagement.view_book_quantity("book3")
    0
    """
    return self.inventory.get(title, 0)