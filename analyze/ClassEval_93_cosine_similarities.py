@staticmethod
def cosine_similarities(vector_1, vectors_all):
    """
        Calcola le somiglianze coseno tra un vettore e un insieme di altri vettori.
        :param vector_1: numpy.ndarray, Vettore da cui si devono calcolare le somiglianze, forma attesa (dim,).
        :param vectors_all: lista di numpy.ndarray, Per ogni riga in vectors_all, viene calcolata la distanza da vector_1, forma attesa (num_vectors, dim).
        :return: numpy.ndarray, Contiene la distanza coseno tra `vector_1` e ogni riga in `vectors_all`, forma (num_vectors,).
        >>> vector1 = np.array([1, 2, 3])
        >>> vectors_all = [np.array([4, 5, 6]), np.array([7, 8, 9])]
        >>> VectorUtil.cosine_similarities(vector1, vectors_all)
        [0.97463185 0.95941195]
        """
    if not vectors_all:
        return np.array([])
    vectors_array = np.array(vectors_all)
    norm_vector_1 = matutils.unitvec(vector_1)
    norms = np.linalg.norm(vectors_array, axis=1, keepdims=True)
    norm_vectors_all = np.where(norms > 0, vectors_array / norms, 0)
    similarities = np.dot(norm_vectors_all, norm_vector_1)
    return similarities