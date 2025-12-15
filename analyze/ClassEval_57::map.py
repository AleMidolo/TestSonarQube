import numpy as np

class MetricsCalculator2: 
    def __init__(self):
        pass

    @staticmethod
    def mrr(data):
        """
        compute the MRR of the input data. MRR is a widely used evaluation index. It is the mean of reciprocal rank.
        :param data: the data must be a tuple, list 0,1,eg.([1,0,...],5).  In each tuple (actual result,ground truth num),ground truth num is the total ground num.
         ([1,0,...],5),
        or list of tuple eg. [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)].
        1 stands for a correct answer, 0 stands for a wrong answer.
        :return: if input data is list, return the recall of this list. if the input data is list of list, return the
        average recall on all list. The second return value is a list of precision for each input.
        >>> MetricsCalculator2.mrr(([1, 0, 1, 0], 4))
        >>> MetricsCalculator2.mrr([([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)])
        1.0, [1.0]
        0.75, [1.0, 0.5]
        """
    
        if type(data) != list and type(data) != tuple:
            raise Exception(
                "the input must be a tuple([0,...,1,...],int) or a iteration of list of tuple")
    
        if len(data) == 0:
            return 0.0, [0.0]
        if type(data) == tuple:
            (sub_list, total_num) = data
            sub_list = np.array(sub_list)
            if total_num == 0:
                return 0.0, [0.0]
            else:
                ranking_array = 1.0 / (np.array(list(range(len(sub_list)))) + 1)
                mr_np = sub_list * ranking_array
    
                mr = 0.0
                for team in mr_np:
                    if team > 0:
                        mr = team
                        break
                return mr, [mr]
    
        if type(data) == list:
            separate_result = []
            for (sub_list, total_num) in data:
                sub_list = np.array(sub_list)
    
                if total_num == 0:
                    mr = 0.0
                else:
                    ranking_array = 1.0 / \
                        (np.array(list(range(len(sub_list)))) + 1)
                    mr_np = sub_list * ranking_array
    
                    mr = 0.0
                    for team in mr_np:
                        if team > 0:
                            mr = team
                            break
    
                separate_result.append(mr)
            return np.mean(separate_result), separate_result

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
            raise Exception(
                "the input must be a tuple([0,...,1,...],int) or a iteration of list of tuple")
        
        if len(data) == 0:
            return 0.0, [0.0]
        
        if type(data) == tuple:
            (sub_list, total_num) = data
            sub_list = np.array(sub_list)
            if total_num == 0:
                return 0.0, [0.0]
            else:
                precision = np.cumsum(sub_list) / (np.arange(1, len(sub_list) + 1))
                ap = np.sum(precision * sub_list) / np.sum(sub_list)
                return ap, [ap]
        
        if type(data) == list:
            separate_result = []
            for (sub_list, total_num) in data:
                sub_list = np.array(sub_list)
                if total_num == 0:
                    ap = 0.0
                else:
                    precision = np.cumsum(sub_list) / (np.arange(1, len(sub_list) + 1))
                    ap = np.sum(precision * sub_list) / np.sum(sub_list)
                separate_result.append(ap)
            return np.mean(separate_result), separate_result