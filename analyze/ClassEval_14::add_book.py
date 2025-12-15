def add_book(self, title, author):
        """
        निर्दिष्ट शीर्षक और लेखक के साथ डेटाबेस में एक पुस्तक जोड़ता है,
        इसकी उपलब्धता को 1 के रूप में उधार लेने के लिए मुक्त सेट करता है।
        :param title: str, पुस्तक का शीर्षक
        :param author: str, लेखक का नाम
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.create_table()
        >>> book_db.add_book('book1', 'author')
        """
        self.cursor.execute('''
                INSERT INTO books (title, author, available) VALUES (?, ?, 1)
            ''', (title, author))
        self.connection.commit()