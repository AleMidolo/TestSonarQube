def view_inventory(self):
    """
        पुस्तक प्रबंधन का इन्वेंटरी प्राप्त करें।
        :return self.inventory: शब्दकोश, {शीर्षक(str): मात्रा(int), ...}
        >>> bookManagement = BookManagement()
        >>> bookManagement.add_book("book1", 1)
        >>> bookManagement.add_book("book2", 1)
        >>> bookManagement.view_inventory()
        {'book1': 1, 'book2': 1}
        """
    return self.inventory.copy()