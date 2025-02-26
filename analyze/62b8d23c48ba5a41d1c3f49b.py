def popitem(self):
    """
    移除并返回最近使用的键值对。
    """
    if not self.data:
        raise KeyError("popitem(): dictionary is empty")
    key = self.order.pop()  # Get the last key from the order list
    value = self.data.pop(key)  # Remove the key from the data dictionary
    return key, value  # Return the key-value pair