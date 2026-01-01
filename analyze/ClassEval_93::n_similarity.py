@staticmethod
def n_similarity(vector_list_1, vector_list_2):
    """
        Compute cosine similarity between two sets of vectors.
        :param vector_list_1: list of numpy vector
        :param vector_list_2: list of numpy vector
        :return: numpy.ndarray, Similarities between vector_list_1 and vector_list_2.
        >>> vector_list1 = [np.array([1, 2, 3]), np.array([4, 5, 6])]
        >>> vector_list2 = [np.array([7, 8, 9]), np.array([10, 11, 12])]
        >>> VectorUtil.n_similarity(vector_list1, vector_list2)
        0.9897287473881233
        """
    similarities = []
    for vec1 in vector_list_1:
        for vec2 in vector_list_2:
            sim = VectorUtil.similarity(vec1, vec2)
            similarities.append(sim)
    return np.array(similarities)