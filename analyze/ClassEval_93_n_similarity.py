@staticmethod
def n_similarity(vector_list_1, vector_list_2):
    """
        दो वेक्टर सेट के बीच कोसाइन समानता की गणना करें।
        :param vector_list_1: numpy वेक्टर की सूची
        :param vector_list_2: numpy वेक्टर की सूची
        :return: numpy.ndarray, vector_list_1 और vector_list_2 के बीच समानताएँ।
        >>> vector_list1 = [np.array([1, 2, 3]), np.array([4, 5, 6])]
        >>> vector_list2 = [np.array([7, 8, 9]), np.array([10, 11, 12])]
        >>> VectorUtil.n_similarity(vector_list1, vector_list2)
        0.9897287473881233
        """
    if not vector_list_1 or not vector_list_2:
        return 0.0
    v1 = np.array(vector_list_1)
    v2 = np.array(vector_list_2)
    avg_v1 = np.mean(v1, axis=0)
    avg_v2 = np.mean(v2, axis=0)
    norm1 = np.linalg.norm(avg_v1)
    norm2 = np.linalg.norm(avg_v2)
    if norm1 == 0 or norm2 == 0:
        return 0.0
    similarity = np.dot(avg_v1, avg_v2) / (norm1 * norm2)
    return similarity