import numpy as np

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
    # Compute the mean vector for each list
    mean_vector_1 = np.mean(vector_list_1, axis=0)
    mean_vector_2 = np.mean(vector_list_2, axis=0)
    
    # Compute cosine similarity between the two mean vectors
    dot_product = np.dot(mean_vector_1, mean_vector_2)
    norm_1 = np.linalg.norm(mean_vector_1)
    norm_2 = np.linalg.norm(mean_vector_2)
    
    cosine_similarity = dot_product / (norm_1 * norm_2)
    
    return cosine_similarity