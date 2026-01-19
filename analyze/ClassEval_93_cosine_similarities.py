import numpy as np

@staticmethod
def cosine_similarities(vector_1, vectors_all):
    """
    计算一个向量与一组其他向量之间的余弦相似度。
    :param vector_1: numpy.ndarray, 用于计算相似度的向量,预期形状为 (dim,).
    :param vectors_all: numpy.ndarray的列表, 对于 vectors_all 中的每一行,计算与 vector_1 的距离,预期形状为 (num_vectors, dim).
    :return: numpy.ndarray, 包含 `vector_1` 与 `vectors_all` 中每一行之间的余弦距离,形状为 (num_vectors,).
    >>> vector1 = np.array([1, 2, 3])
    >>> vectors_all = [np.array([4, 5, 6]), np.array([7, 8, 9])]
    >>> VectorUtil.cosine_similarities(vector1, vectors_all)
    [0.97463185 0.95941195]
    """
    # Convert list of vectors to numpy array if needed
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