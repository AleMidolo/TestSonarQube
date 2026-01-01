@staticmethod
def compute_idf_weight_dict(total_num, number_dict):
    """
        对 number_dict 中的每个 count 计算 log(total_num+1/count+1) 
        :param total_num: int
        :param number_dict: dict
        :return: dict
        >>> num_dict = {'key1':0.1, 'key2':0.5}
        >>> VectorUtil.compute_idf_weight_dict(2, num_dict)
        {'key1': 1.0033021088637848, 'key2': 0.6931471805599453}
        """
    result = {}
    for key, count in number_dict.items():
        weight = math.log((total_num + 1) / (count + 1))
        result[key] = weight
    return result