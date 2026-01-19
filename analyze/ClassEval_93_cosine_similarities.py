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
    import numpy as np
    
    # Convert list to numpy array if needed
    if isinstance(vectors_all, list):
        vectors_all = np.array(vectors_all)
    
    # Compute dot products between vector_1 and all vectors
    dot_products = np.dot(vectors_all, vector_1)
    
    # Compute norms
    norm_vector_1 = np.linalg.norm(vector_1)
    norms_vectors_all = np.linalg.norm(vectors_all, axis=1)
    
    # Compute cosine similarities
    cosine_sims = dot_products / (norm_vector_1 * norms_vectors_all)
    
    return cosine_sims