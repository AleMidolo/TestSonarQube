def get(self, key, default=None):
    """
    D.get(k[, d]) -> D[k] यदि k D में है, तो D[k] लौटाया जाएगा, अन्यथा d। d का डिफ़ॉल्ट मान None है।
    """
    return self.data[key] if key in self.data else default