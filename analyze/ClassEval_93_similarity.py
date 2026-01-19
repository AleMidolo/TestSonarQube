@staticmethod
def similarity(vector_1, vector_2):
    """
        计算一个向量与另一个向量之间的余弦相似度。
        :param vector_1: numpy.ndarray, 要计算相似度的向量，预期形状为 (dim,).
        :param vector_2: numpy.ndarray, 要计算相似度的向量，预期形状为 (dim,).
        :return: numpy.ndarray, 包含 `vector_1` 和 `vector_2` 之间的余弦距离
        >>> vector_1 = np.array([1, 1])
        >>> vector_2 = np.array([1, 0])
        >>> VectorUtil.similarity(vector_1, vector_2)
        0.7071067811865475
        """
    norm1 = np.linalg.norm(vector_1)
    norm2 = np.linalg.norm(vector_2)
    if norm1 == 0 or norm2 == 0:
        return 0.0
    dot_product = np.dot(vector_1, vector_2)
    similarity = dot_product / (norm1 * norm2)
    return similarity