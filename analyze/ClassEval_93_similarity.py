import numpy as np

def similarity(vector_1, vector_2):
    """
    计算一个向量与另一个向量之间的余弦相似度。
    :param vector_1: numpy.ndarray, 要计算相似度的向量，预期形状为 (dim,).
    :param vector_2: numpy.ndarray, 要计算相似度的向量，预期形状为 (dim,).
    :return: numpy.ndarray, 包含 `vector_1` 和 `vector_2` 之间的余弦距离
    >>> vector_1 = np.array([1, 1])
    >>> vector_2 = np.array([1, 0])
    >>> VectorUtil.similarity(vector_1, vector_2)
    0.7071067811865475
    """
    # Calculate dot product
    dot_product = np.dot(vector_1, vector_2)
    
    # Calculate norms (magnitudes) of both vectors
    norm_1 = np.linalg.norm(vector_1)
    norm_2 = np.linalg.norm(vector_2)
    
    # Calculate cosine similarity
    # Handle division by zero case
    if norm_1 == 0 or norm_2 == 0:
        return 0.0
    
    cosine_similarity = dot_product / (norm_1 * norm_2)
    
    return cosine_similarity