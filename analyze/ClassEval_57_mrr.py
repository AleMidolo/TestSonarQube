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
        raise Exception('the input must be a tuple([0,...,1,...],int) or a iteration of list of tuple')
    if len(data) == 0:
        return (0.0, [0.0])
    if type(data) == tuple:
        sub_list, total_num = data
        sub_list = np.array(sub_list)
        if total_num == 0:
            return (0.0, [0.0])
        first_correct_idx = None
        for i, val in enumerate(sub_list):
            if val == 1:
                first_correct_idx = i
                break
        if first_correct_idx is None:
            return (0.0, [0.0])
        else:
            rr = 1.0 / (first_correct_idx + 1)
            return (rr, [rr])
    if type(data) == list:
        separate_result = []
        for sub_list, total_num in data:
            sub_list = np.array(sub_list)
            if total_num == 0:
                rr = 0.0
            else:
                first_correct_idx = None
                for i, val in enumerate(sub_list):
                    if val == 1:
                        first_correct_idx = i
                        break
                if first_correct_idx is None:
                    rr = 0.0
                else:
                    rr = 1.0 / (first_correct_idx + 1)
            separate_result.append(rr)
        return (np.mean(separate_result), separate_result)