def pop_u16(self):
    """
    self.data के अंतिम दो बाइट्स को हटाएं और उन्हें एक बिग-एंडियन 16-बिट अनसाइनड इंटीजर के रूप में वापस करें।
    """
    if len(self.data) < 2:
        raise ValueError("Not enough bytes in self.data to pop a 16-bit integer.")
    
    # Extract the last two bytes
    u16_bytes = self.data[-2:]
    # Remove the last two bytes from self.data
    self.data = self.data[:-2]
    
    # Convert the bytes to a big-endian unsigned 16-bit integer
    u16_value = int.from_bytes(u16_bytes, byteorder='big', signed=False)
    
    return u16_value