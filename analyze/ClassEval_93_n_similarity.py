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
        return np.array([0.0])
    vectors_1 = np.array(vector_list_1)
    vectors_2 = np.array(vector_list_2)
    mean_1 = np.mean(vectors_1, axis=0)
    mean_2 = np.mean(vectors_2, axis=0)
    norm_1 = np.linalg.norm(mean_1)
    norm_2 = np.linalg.norm(mean_2)
    if norm_1 == 0 or norm_2 == 0:
        return np.array([0.0])
    similarity = np.dot(mean_1, mean_2) / (norm_1 * norm_2)
    return similarity