def pop_u16(self):
    """
    self.data के अंतिम दो बाइट्स को हटाएं और उन्हें एक बिग-एंडियन 16-बिट अनसाइनड इंटीजर के रूप में वापस करें।
    """
    if len(self.data) < 2:
        raise ValueError("Not enough data to pop 16 bits.")
    
    # Get the last two bytes
    last_two_bytes = self.data[-2:]
    
    # Remove the last two bytes from self.data
    self.data = self.data[:-2]
    
    # Convert the last two bytes to a big-endian unsigned 16-bit integer
    return (last_two_bytes[0] << 8) | last_two_bytes[1]