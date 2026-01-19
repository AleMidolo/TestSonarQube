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
    def calculate_ap(result_list, ground_truth_num):
        """Calculate Average Precision for a single query"""
        if ground_truth_num == 0:
            return 0.0
        
        precision_sum = 0.0
        num_correct = 0
        
        for i, val in enumerate(result_list):
            if val == 1:
                num_correct += 1
                precision_at_i = num_correct / (i + 1)
                precision_sum += precision_at_i
        
        ap = precision_sum / ground_truth_num
        return ap
    
    # Check if data is a single tuple or a list of tuples
    if isinstance(data, tuple):
        # Single query case
        result_list, ground_truth_num = data
        ap = calculate_ap(result_list, ground_truth_num)
        return ap, [ap]
    else:
        # Multiple queries case
        ap_list = []
        for result_list, ground_truth_num in data:
            ap = calculate_ap(result_list, ground_truth_num)
            ap_list.append(ap)
        
        mean_ap = sum(ap_list) / len(ap_list) if ap_list else 0.0
        return mean_ap, ap_list