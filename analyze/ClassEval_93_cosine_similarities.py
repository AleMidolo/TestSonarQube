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
    import numpy as np
    
    # Convert vectors_all to numpy array if it's a list
    vectors_all = np.array(vectors_all)
    
    # Calculate dot products between vector_1 and all vectors
    dot_products = np.dot(vectors_all, vector_1)
    
    # Calculate norms
    norm_vector_1 = np.linalg.norm(vector_1)
    norms_vectors_all = np.linalg.norm(vectors_all, axis=1)
    
    # Calculate cosine similarities
    cosine_sims = dot_products / (norm_vector_1 * norms_vectors_all)
    
    return cosine_sims