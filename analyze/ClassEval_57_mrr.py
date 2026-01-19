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
    def calculate_rr(result_list):
        """Calculate reciprocal rank for a single list"""
        for i, val in enumerate(result_list):
            if val == 1:
                return 1.0 / (i + 1)
        return 0.0
    
    # Check if data is a single tuple or a list of tuples
    if isinstance(data, tuple):
        # Single tuple case
        result_list, ground_truth_num = data
        rr = calculate_rr(result_list)
        return rr, [rr]
    else:
        # List of tuples case
        rr_list = []
        for result_list, ground_truth_num in data:
            rr = calculate_rr(result_list)
            rr_list.append(rr)
        
        # Calculate mean reciprocal rank
        mean_rr = sum(rr_list) / len(rr_list) if rr_list else 0.0
        return mean_rr, rr_list