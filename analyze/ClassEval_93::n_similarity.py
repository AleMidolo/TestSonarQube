@staticmethod
def n_similarity(vector_list_1, vector_list_2):
    """
        Calcola la similarità coseno tra due insiemi di vettori.
        :param vector_list_1: lista di vettori numpy
        :param vector_list_2: lista di vettori numpy
        :return: numpy.ndarray, Similarità tra vector_list_1 e vector_list_2.
        >>> vector_list1 = [np.array([1, 2, 3]), np.array([4, 5, 6])]
        >>> vector_list2 = [np.array([7, 8, 9]), np.array([10, 11, 12])]
        >>> VectorUtil.n_similarity(vector_list1, vector_list2)
        0.9897287473881233
        """
    if not vector_list_1 or not vector_list_2:
        return 0.0
    v1_array = np.array(vector_list_1)
    v2_array = np.array(vector_list_2)
    avg_vector_1 = np.mean(v1_array, axis=0)
    avg_vector_2 = np.mean(v2_array, axis=0)
    norm1 = np.linalg.norm(avg_vector_1)
    norm2 = np.linalg.norm(avg_vector_2)
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return np.dot(avg_vector_1, avg_vector_2) / (norm1 * norm2)