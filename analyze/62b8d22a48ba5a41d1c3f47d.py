def pop(self, key, default=__marker):
    """
    D.pop(k[, d]) -> v
    निर्दिष्ट कुंजी (key) को हटाएं और संबंधित मान (value) लौटाएं।
    यदि कुंजी नहीं मिलती है, तो यदि 'd' दिया गया है तो उसे लौटाया जाएगा, 
    अन्यथा KeyError उत्पन्न किया जाएगा।
    """
    if key in self:
        value = self[key]
        del self[key]
        return value
    elif default is not self.__marker:
        return default
    else:
        raise KeyError(key)