@staticmethod
def cosine_similarities(vector_1, vectors_all):
    """
        एक वेक्टर और अन्य वेक्टरों के सेट के बीच कोसाइन समानताएँ की गणना करें।
        :param vector_1: numpy.ndarray, वह वेक्टर जिससे समानताएँ की जानी हैं, अपेक्षित आकार (dim,).
        :param vectors_all: numpy.ndarray की सूची, vectors_all में प्रत्येक पंक्ति के लिए, vector_1 से दूरी की गणना की जाती है, अपेक्षित आकार (num_vectors, dim).
        :return: numpy.ndarray, `vector_1` और `vectors_all` में प्रत्येक पंक्ति के बीच कोसाइन दूरी को शामिल करता है, आकार (num_vectors,).
        >>> vector1 = np.array([1, 2, 3])
        >>> vectors_all = [np.array([4, 5, 6]), np.array([7, 8, 9])]
        >>> VectorUtil.cosine_similarities(vector1, vectors_all)
        [0.97463185 0.95941195]
        """
    return np.array([VectorUtil.similarity(vector_1, vector) for vector in vectors_all])