import math

@staticmethod
def compute_idf_weight_dict(total_num, number_dict):
    """
    Calcola log(total_num+1/count+1) per ogni conteggio in number_dict
    :param total_num: int
    :param number_dict: dict
    :return: dict
    >>> num_dict = {'key1':0.1, 'key2':0.5}
    >>> VectorUtil.compute_idf_weight_dict(2, num_dict)
    {'key1': 1.0033021088637848, 'key2': 0.6931471805599453}
    """
    result = {}
    for key, count in number_dict.items():
        result[key] = math.log((total_num + 1) / (count + 1))
    return result