def similarity(vector_1, vector_2):
    """
        计算一个向量与另一个向量之间的余弦相似度。
        :param vector_1: numpy.ndarray, 要计算相似度的向量，预期形状为 (dim,).
        :param vector_2: numpy.ndarray, 要计算相似度的向量，预期形状为 (dim,).
        :return: numpy.ndarray, 包含 `vector_1` 和 `vector_2` 之间的余弦距离
        >>> vector_1 = np.array([1, 1])
        >>> vector_2 = np.array([1, 0])
        >>> similarity(vector_1, vector_2)
        0.7071067811865475
        """
    norm_1 = np.linalg.norm(vector_1)
    norm_2 = np.linalg.norm(vector_2)
    dot_product = np.dot(vector_1, vector_2)
    return dot_product / (norm_1 * norm_2)