def popitem(self):
    if not self.freq_map:
        raise KeyError("popitem(): dictionary is empty")
    
    # Find the least frequently used key
    least_freq = min(self.freq_map.values())
    least_freq_keys = [key for key, freq in self.freq_map.items() if freq == least_freq]
    
    # If there are multiple keys with the same frequency, we can choose one (e.g., the first one)
    key_to_remove = least_freq_keys[0]
    
    # Remove the key from the frequency map and the main storage
    value = self.storage.pop(key_to_remove)
    del self.freq_map[key_to_remove]
    
    return (key_to_remove, value)