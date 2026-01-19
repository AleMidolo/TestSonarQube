@staticmethod
def similarity(vector_1, vector_2):
    """
        एक वेक्टर और दूसरे वेक्टर के बीच कोसाइन समानता की गणना करें।
        :param vector_1: numpy.ndarray, वह वेक्टर जिससे समानताएँ निकाली जानी हैं, अपेक्षित आकार (dim,).
        :param vector_2: numpy.ndarray, वह वेक्टर जिससे समानताएँ निकाली जानी हैं, अपेक्षित आकार (dim,).
        :return: numpy.ndarray, `vector_1` और `vector_2` के बीच कोसाइन दूरी को शामिल करता है
        >>> vector_1 = np.array([1, 1])
        >>> vector_2 = np.array([1, 0])
        >>> VectorUtil.similarity(vector_1, vector_2)
        0.7071067811865475
        """
    norm1 = np.linalg.norm(vector_1)
    norm2 = np.linalg.norm(vector_2)
    if norm1 == 0 or norm2 == 0:
        return 0.0
    dot_product = np.dot(vector_1, vector_2)
    similarity = dot_product / (norm1 * norm2)
    return similarity