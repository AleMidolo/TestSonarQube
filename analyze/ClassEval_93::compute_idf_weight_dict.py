@staticmethod
def compute_idf_weight_dict(total_num, number_dict):
    """
        प्रत्येक गिनती के लिए log(total_num+1/count+1) की गणना करें जो number_dict में है
        :param total_num: int
        :param number_dict: dict
        :return: dict
        >>> num_dict = {'key1':0.1, 'key2':0.5}
        >>> VectorUtil.compute_idf_weight_dict(2, num_dict)
        {'key1': 1.0033021088637848, 'key2': 0.6931471805599453}
        """
    result_dict = {}
    for key, count in number_dict.items():
        weight = math.log((total_num + 1) / (count + 1))
        result_dict[key] = weight
    return result_dict