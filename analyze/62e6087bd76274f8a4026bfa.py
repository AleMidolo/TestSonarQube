def pop_u16(self):
    """
    self.data के अंतिम दो बाइट्स को हटाएं और उन्हें एक बिग-एंडियन 16-बिट अनसाइनड इंटीजर के रूप में वापस करें।
    """
    if len(self.data) < 2:
        raise ValueError("Not enough bytes in self.data to pop a 16-bit integer")
    
    # Extract the last two bytes
    byte1 = self.data.pop()
    byte2 = self.data.pop()
    
    # Combine the bytes in big-endian order
    u16_value = (byte2 << 8) | byte1
    
    return u16_value