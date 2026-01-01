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
    vecs1 = np.array(vector_list_1)
    vecs2 = np.array(vector_list_2)
    avg_vec1 = np.mean(vecs1, axis=0)
    avg_vec2 = np.mean(vecs2, axis=0)
    norm1 = np.linalg.norm(avg_vec1)
    norm2 = np.linalg.norm(avg_vec2)
    if norm1 == 0 or norm2 == 0:
        return np.array([0.0])
    similarity = np.dot(avg_vec1, avg_vec2) / (norm1 * norm2)
    return similarity