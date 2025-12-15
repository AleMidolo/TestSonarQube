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
        计算输入数据的MAP。MAP是一个广泛使用的评估指标。它是AP（平均精度）的均值。
        :param data: 数据必须是一个元组，列表 0,1，例如（[1,0,...],5）。在每个元组中（实际结果，真实标签数量），真实标签数量是总的真实数量。
        ([1,0,...],5)，
        或者元组的列表，例如 [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)]。
        1代表正确答案，0代表错误答案。
        :return: 如果输入数据是列表，则返回该列表的召回率。如果输入数据是列表的列表，则返回所有列表的平均召回率。第二个返回值是每个输入的精度列表。
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
                precision_sum = 0.0
                correct_count = 0
                for i, value in enumerate(sub_list):
                    if value == 1:
                        correct_count += 1
                        precision_sum += correct_count / (i + 1)
                ap = precision_sum / min(total_num, correct_count) if correct_count > 0 else 0.0
                return ap, [ap]
        
        if type(data) == list:
            separate_result = []
            for (sub_list, total_num) in data:
                sub_list = np.array(sub_list)
                precision_sum = 0.0
                correct_count = 0
                for i, value in enumerate(sub_list):
                    if value == 1:
                        correct_count += 1
                        precision_sum += correct_count / (i + 1)
                ap = precision_sum / min(total_num, correct_count) if correct_count > 0 else 0.0
                separate_result.append(ap)
            return np.mean(separate_result), separate_result