@staticmethod
def cosine_similarities(vector_1, vectors_all):
    """
        Compute cosine similarities between one vector and a set of other vectors.
        :param vector_1: numpy.ndarray, Vector from which similarities are to be computed, expected shape (dim,).
        :param vectors_all: list of numpy.ndarray, For each row in vectors_all, distance from vector_1 is computed, expected shape (num_vectors, dim).
        :return: numpy.ndarray, Contains cosine distance between `vector_1` and each row in `vectors_all`, shape (num_vectors,).
        >>> vector1 = np.array([1, 2, 3])
        >>> vectors_all = [np.array([4, 5, 6]), np.array([7, 8, 9])]
        >>> VectorUtil.cosine_similarities(vector1, vectors_all)
        [0.97463185 0.95941195]
        """
    vectors_all_array = np.array(vectors_all)
    norm_vector_1 = matutils.unitvec(vector_1)
    norm_vectors_all = np.array([matutils.unitvec(v) for v in vectors_all_array])
    similarities = np.dot(norm_vectors_all, norm_vector_1)
    return similarities