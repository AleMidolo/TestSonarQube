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
    if type(data) != list and type(data) != tuple:
        raise Exception('the input must be a tuple([0,...,1,...],int) or a iteration of list of tuple')
    if len(data) == 0:
        return (0.0, [0.0])
    if type(data) == tuple:
        sub_list, total_num = data
        sub_list = np.array(sub_list)
        if total_num == 0:
            return (0.0, [0.0])
        positions = np.where(sub_list == 1)[0] + 1
        if len(positions) == 0:
            return (0.0, [0.0])
        precisions = []
        for i, pos in enumerate(positions):
            precision_at_k = (i + 1) / pos
            precisions.append(precision_at_k)
        ap = np.mean(precisions)
        return (ap, [ap])
    if type(data) == list:
        separate_result = []
        for sub_list, total_num in data:
            sub_list = np.array(sub_list)
            if total_num == 0:
                ap = 0.0
            else:
                positions = np.where(sub_list == 1)[0] + 1
                if len(positions) == 0:
                    ap = 0.0
                else:
                    precisions = []
                    for i, pos in enumerate(positions):
                        precision_at_k = (i + 1) / pos
                        precisions.append(precision_at_k)
                    ap = np.mean(precisions)
            separate_result.append(ap)
        return (np.mean(separate_result), separate_result)