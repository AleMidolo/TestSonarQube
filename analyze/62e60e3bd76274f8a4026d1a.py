def from_raw_values(cls, values):
    bookmarks = []
    for value in values:
        bookmarks.append(value.strip())
    return cls(bookmarks)