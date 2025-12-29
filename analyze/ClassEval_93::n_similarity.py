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
    similarities = []
    for vec1 in vector_list_1:
        for vec2 in vector_list_2:
            sim = VectorUtil.similarity(vec1, vec2)
            similarities.append(sim)
    return np.array(similarities).mean()