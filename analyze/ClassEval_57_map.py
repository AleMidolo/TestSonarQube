@staticmethod
def map(data):
    """
    इनपुट डेटा का MAP गणना करें। MAP एक व्यापक रूप से उपयोग किया जाने वाला मूल्यांकन सूचकांक है। यह AP (औसत सटीकता) का औसत है।
    :param data: डेटा एक ट्यूपल, सूची 0,1 होना चाहिए, जैसे कि ([1,0,...],5)। प्रत्येक ट्यूपल में (वास्तविक परिणाम, ग्राउंड ट्रुथ संख्या), ग्राउंड ट्रुथ संख्या कुल ग्राउंड संख्या है।
    ([1,0,...],5),
    या ट्यूपल की सूची जैसे कि [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)]।
    1 एक सही उत्तर के लिए है, 0 एक गलत उत्तर के लिए है।
    :return: यदि इनपुट डेटा सूची है, तो इस सूची की पुनः प्राप्ति लौटाएं। यदि इनपुट डेटा सूची की सूची है, तो सभी सूचियों पर औसत पुनः प्राप्ति लौटाएं। दूसरा लौटने वाला मान प्रत्येक इनपुट के लिए सटीकता की एक सूची है।
    >>> MetricsCalculator2.map(([1, 0, 1, 0], 4))
    >>> MetricsCalculator2.map([([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)])
    0.41666666666666663, [0.41666666666666663]
    0.3333333333333333, [0.41666666666666663, 0.25]
    """
    def calculate_ap(results, ground_truth_count):
        """Calculate Average Precision for a single query"""
        if ground_truth_count == 0:
            return 0.0
        
        precision_sum = 0.0
        relevant_count = 0
        
        for i, result in enumerate(results):
            if result == 1:
                relevant_count += 1
                precision_at_i = relevant_count / (i + 1)
                precision_sum += precision_at_i
        
        ap = precision_sum / ground_truth_count
        return ap
    
    # Check if data is a single tuple or a list of tuples
    if isinstance(data, tuple):
        # Single query case
        results, ground_truth_count = data
        ap = calculate_ap(results, ground_truth_count)
        return ap, [ap]
    else:
        # Multiple queries case
        ap_list = []
        for results, ground_truth_count in data:
            ap = calculate_ap(results, ground_truth_count)
            ap_list.append(ap)
        
        mean_ap = sum(ap_list) / len(ap_list) if ap_list else 0.0
        return mean_ap, ap_list