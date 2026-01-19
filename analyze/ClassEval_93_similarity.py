def similarity(vector_1, vector_2):
    """
        Calcula la similitud coseno entre un vector y otro vector.
        :param vector_1: numpy.ndarray, Vector del cual se calcularán las similitudes, forma esperada (dim,).
        :param vector_2: numpy.ndarray, Vector del cual se calcularán las similitudes, forma esperada (dim,).
        :return: numpy.ndarray, Contiene la distancia coseno entre `vector_1` y `vector_2`
        >>> vector_1 = np.array([1, 1])
        >>> vector_2 = np.array([1, 0])
        >>> similarity(vector_1, vector_2)
        0.7071067811865475
        """
    norm_1 = np.linalg.norm(vector_1)
    norm_2 = np.linalg.norm(vector_2)
    if norm_1 == 0 or norm_2 == 0:
        return 0.0
    return dot(vector_1, vector_2) / (norm_1 * norm_2)