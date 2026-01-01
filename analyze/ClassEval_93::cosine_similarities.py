@staticmethod
def cosine_similarities(vector_1, vectors_all):
    """
        计算一个向量与一组其他向量之间的余弦相似度。
        :param vector_1: numpy.ndarray, 用于计算相似度的向量，预期形状为 (dim,).
        :param vectors_all: numpy.ndarray的列表, 对于 vectors_all 中的每一行，计算与 vector_1 的距离，预期形状为 (num_vectors, dim).
        :return: numpy.ndarray, 包含 `vector_1` 与 `vectors_all` 中每一行之间的余弦距离，形状为 (num_vectors,).
        >>> vector1 = np.array([1, 2, 3])
        >>> vectors_all = [np.array([4, 5, 6]), np.array([7, 8, 9])]
        >>> VectorUtil.cosine_similarities(vector1, vectors_all)
        [0.97463185 0.95941195]
        """
    unit_vector_1 = matutils.unitvec(vector_1)
    similarities = []
    for vector in vectors_all:
        similarity = dot(unit_vector_1, matutils.unitvec(vector))
        similarities.append(similarity)
    return np.array(similarities)