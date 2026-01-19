import numpy as np

def similarity(vector_1, vector_2):
    """
    Calcola la similarità coseno tra un vettore e un altro vettore.
    :param vector_1: numpy.ndarray, Vettore da cui calcolare le similarità, forma attesa (dim,).
    :param vector_2: numpy.ndarray, Vettore da cui calcolare le similarità, forma attesa (dim,).
    :return: numpy.ndarray, Contiene la distanza coseno tra `vector_1` e `vector_2`
    >>> vector_1 = np.array([1, 1])
    >>> vector_2 = np.array([1, 0])
    >>> VectorUtil.similarity(vector_1, vector_2)
    0.7071067811865475
    """
    dot_product = np.dot(vector_1, vector_2)
    norm_1 = np.linalg.norm(vector_1)
    norm_2 = np.linalg.norm(vector_2)
    return dot_product / (norm_1 * norm_2)