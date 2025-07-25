def pop_u16(self):
    """
    self.data के अंतिम दो बाइट्स को हटाएं और उन्हें एक बिग-एंडियन 16-बिट अनसाइनड इंटीजर के रूप में वापस करें।
    """
    if len(self.data) < 2:
        raise ValueError("Not enough bytes to pop u16")
        
    # Get last 2 bytes
    bytes_data = self.data[-2:]
    
    # Remove last 2 bytes from self.data
    self.data = self.data[:-2]
    
    # Convert bytes to big-endian 16-bit unsigned int
    value = int.from_bytes(bytes_data, byteorder='big', signed=False)
    
    return value