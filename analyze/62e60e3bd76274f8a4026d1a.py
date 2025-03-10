def from_raw_values(cls, values):
    """
    Create a Bookmarks object from a list of raw bookmark string values.

    You should not need to use this method unless you want to deserialize
    bookmarks.

    :param values: ASCII string values (raw bookmarks)
    :type values: Iterable[str]
    """
    # Assuming the Bookmarks class is defined elsewhere
    bookmarks = cls()
    for value in values:
        # Process each raw bookmark value and add it to the Bookmarks object
        # This is a placeholder for the actual deserialization logic
        bookmark = process_raw_bookmark(value)  # Replace with actual processing logic
        bookmarks.add(bookmark)
    return bookmarks

# Placeholder function for processing raw bookmark values
def process_raw_bookmark(raw_value):
    # Implement the logic to convert raw_value into a bookmark object
    return raw_value  # Replace with actual processing logic