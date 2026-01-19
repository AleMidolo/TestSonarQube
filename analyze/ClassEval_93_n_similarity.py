import numpy as np

@staticmethod
def n_similarity(vector_list_1, vector_list_2):
    """
    计算两个向量集合之间的余弦相似度。
    :param vector_list_1: numpy 向量的列表
    :param vector_list_2: numpy 向量的列表
    :return: numpy.ndarray, vector_list_1 和 vector_list_2 之间的相似度。
    >>> vector_list1 = [np.array([1, 2, 3]), np.array([4, 5, 6])]
    >>> vector_list2 = [np.array([7, 8, 9]), np.array([10, 11, 12])]
    >>> VectorUtil.n_similarity(vector_list1, vector_list2)
    0.9897287473881233
    """
    # 计算两个向量集合的平均向量
    mean_vector_1 = np.mean(vector_list_1, axis=0)
    mean_vector_2 = np.mean(vector_list_2, axis=0)
    
    # 计算余弦相似度
    dot_product = np.dot(mean_vector_1, mean_vector_2)
    norm_1 = np.linalg.norm(mean_vector_1)
    norm_2 = np.linalg.norm(mean_vector_2)
    
    cosine_similarity = dot_product / (norm_1 * norm_2)
    
    return cosine_similarity