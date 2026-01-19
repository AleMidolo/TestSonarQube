import numpy as np

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
    # Convert list to numpy array if needed
    if isinstance(vectors_all, list):
        vectors_all = np.array(vectors_all)
    
    # Normalize vector_1
    norm_1 = np.linalg.norm(vector_1)
    
    # Compute dot products between vector_1 and all vectors
    dot_products = np.dot(vectors_all, vector_1)
    
    # Compute norms of all vectors
    norms_all = np.linalg.norm(vectors_all, axis=1)
    
    # Compute cosine similarities
    cosine_sims = dot_products / (norm_1 * norms_all)
    
    return cosine_sims