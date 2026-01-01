@staticmethod
def map(data):
    """
        compute the MAP of the input data. MAP is a widely used evaluation index. It is the mean of AP (average precision).
        :param data: the data must be a tuple, list 0,1,eg.([1,0,...],5).  In each tuple (actual result,ground truth num),ground truth num is the total ground num.
         ([1,0,...],5),
        or list of tuple eg. [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)].
        1 stands for a correct answer, 0 stands for a wrong answer.
        :return: if input data is list, return the recall of this list. if the input data is list of list, return the
        average recall on all list. The second return value is a list of precision for each input.
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
        precision_at_k = []
        relevant_count = 0
        for k in range(len(sub_list)):
            if sub_list[k] == 1:
                relevant_count += 1
                precision_at_k.append(relevant_count / (k + 1))
        if len(precision_at_k) == 0:
            ap = 0.0
        else:
            ap = np.mean(precision_at_k)
        return (ap, [ap])
    if type(data) == list:
        separate_result = []
        for sub_list, total_num in data:
            sub_list = np.array(sub_list)
            if total_num == 0:
                ap = 0.0
            else:
                precision_at_k = []
                relevant_count = 0
                for k in range(len(sub_list)):
                    if sub_list[k] == 1:
                        relevant_count += 1
                        precision_at_k.append(relevant_count / (k + 1))
                if len(precision_at_k) == 0:
                    ap = 0.0
                else:
                    ap = np.mean(precision_at_k)
            separate_result.append(ap)
        return (np.mean(separate_result), separate_result)