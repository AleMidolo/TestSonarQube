def reset(self):
    """
    histogram को रीसेट करें।  

    - वर्तमान संदर्भ को एक खाली डिक्शनरी में रीसेट कर दिया गया है।  
    - बिन्स को *initial_value* या *make_bins()* (प्रारंभिक सेटअप के आधार पर) के साथ पुनः प्रारंभ किया गया है।  
    """
    self.data = {}
    self.bins = self.initial_value if hasattr(self, 'initial_value') else self.make_bins()