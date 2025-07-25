def popitem(self):
    """
    Remove and return the `(key, value)` pair most recently used.
    """
    if not self.data:
        raise KeyError("popitem(): dictionary is empty")
    key = self.order.pop()  # Get the most recently used key
    value = self.data.pop(key)  # Remove the key from the data
    return key, value  # Return the key-value pair