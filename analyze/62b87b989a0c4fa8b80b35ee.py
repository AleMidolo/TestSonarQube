def reset(self):
    """
    हिस्टोग्राम को रीसेट करें।  

    - वर्तमान संदर्भ को एक खाली डिक्शनरी में रीसेट कर दिया गया है।  
    - बिन्स को *initial_value* या *make_bins()* (प्रारंभिक सेटअप के आधार पर) के साथ पुनः प्रारंभ किया गया है।  
    """
    self.context = {}
    if hasattr(self, 'initial_value'):
        self.bins = [self.initial_value] * len(self.bins)
    else:
        self.bins = self.make_bins()