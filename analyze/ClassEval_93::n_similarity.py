@staticmethod
def n_similarity(vector_list_1, vector_list_2):
    """
        Calcula la similitud coseno entre dos conjuntos de vectores.
        :param vector_list_1: lista de vectores numpy
        :param vector_list_2: lista de vectores numpy
        :return: numpy.ndarray, Similitudes entre vector_list_1 y vector_list_2.
        >>> vector_list1 = [np.array([1, 2, 3]), np.array([4, 5, 6])]
        >>> vector_list2 = [np.array([7, 8, 9]), np.array([10, 11, 12])]
        >>> VectorUtil.n_similarity(vector_list1, vector_list2)
        0.9897287473881233
        """
    if not vector_list_1 or not vector_list_2:
        return 0.0
    v1_array = np.array(vector_list_1)
    v2_array = np.array(vector_list_2)
    mean_v1 = np.mean(v1_array, axis=0)
    mean_v2 = np.mean(v2_array, axis=0)
    norm_v1 = np.linalg.norm(mean_v1)
    norm_v2 = np.linalg.norm(mean_v2)
    if norm_v1 == 0 or norm_v2 == 0:
        return 0.0
    similarity = np.dot(mean_v1, mean_v2) / (norm_v1 * norm_v2)
    return similarity