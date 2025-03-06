from functools import lru_cache as _lru_cache

def lru_cache(maxsize=128, typed=False):
    """
    एक डेकोरेटर जो एक फ़ंक्शन को एक मेमोराइज़िंग कॉलेबल के साथ रैप करता है,
    जो `maxsize` तक के परिणामों को सेव करता है। यह परिणामों को 
    Least Recently Used (LRU) एल्गोरिदम के आधार पर प्रबंधित करता है।
    """
    return _lru_cache(maxsize=maxsize, typed=typed)