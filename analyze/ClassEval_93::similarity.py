def similarity(vector_1, vector_2):
    """
    Compute the cosine similarity between one vector and another vector.
    :param vector_1: numpy.ndarray, Vector from which similarities are to be computed, expected shape (dim,).
    :param vector_2: numpy.ndarray, Vector from which similarities are to be computed, expected shape (dim,).
    :return: numpy.ndarray, Contains cosine distance between `vector_1` and `vector_2`
    >>> vector_1 = np.array([1, 1])
    >>> vector_2 = np.array([1, 0])
    >>> similarity(vector_1, vector_2)
    0.7071067811865475
    """
    
    norm_1 = np.linalg.norm(vector_1)
    norm_2 = np.linalg.norm(vector_2)
    
    if norm_1 == 0 or norm_2 == 0:
        return 0.0
    
    dot_product = np.dot(vector_1, vector_2)
    return dot_product / (norm_1 * norm_2)