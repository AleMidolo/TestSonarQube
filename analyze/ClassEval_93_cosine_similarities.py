@staticmethod
def cosine_similarities(vector_1, vectors_all):
    """
        Calcula las similitudes coseno entre un vector y un conjunto de otros vectores.
        :param vector_1: numpy.ndarray, Vector a partir del cual se calcularán las similitudes, forma esperada (dim,).
        :param vectors_all: lista de numpy.ndarray, Para cada fila en vectors_all, se calcula la distancia desde vector_1, forma esperada (num_vectors, dim).
        :return: numpy.ndarray, Contiene la distancia coseno entre `vector_1` y cada fila en `vectors_all`, forma (num_vectors,).
        >>> vector1 = np.array([1, 2, 3])
        >>> vectors_all = [np.array([4, 5, 6]), np.array([7, 8, 9])]
        >>> VectorUtil.cosine_similarities(vector1, vectors_all)
        [0.97463185 0.95941195]
        """
    vector_1 = np.asarray(vector_1)
    vectors_all = np.asarray(vectors_all)
    norm_vector_1 = matutils.unitvec(vector_1)
    if vectors_all.ndim == 1:
        vectors_all = vectors_all.reshape(1, -1)
    norm_vectors_all = np.array([matutils.unitvec(v) for v in vectors_all])
    similarities = np.dot(norm_vectors_all, norm_vector_1)
    return similarities