import numpy as np

class KappaCalculator: 

    def kappa(testData, k):
        """
        Calculate the cohens kappa value of a k-dimensional matrix
        :param testData: The k-dimensional matrix that needs to calculate the cohens kappa value
        :param k: int, Matrix dimension
        :return:float, the cohens kappa value of the matrix
        >>> KappaCalculator.kappa([[2, 1, 1], [1, 2, 1], [1, 1, 2]], 3)
        0.25
        """
    
        dataMat = np.mat(testData)
        P0 = 0.0
        for i in range(k):
            P0 += dataMat[i, i] * 1.0
        xsum = np.sum(dataMat, axis=1)
        ysum = np.sum(dataMat, axis=0)
        total_sum = np.sum(dataMat)
        Pe = float(ysum * xsum) / total_sum / total_sum
        P0 = float(P0 / total_sum * 1.0)
        cohens_coefficient = float((P0 - Pe) / (1 - Pe))
        return cohens_coefficient

    @staticmethod
    def fleiss_kappa(testData, N, k, n):
        """
        计算 N * k 矩阵的 Fleiss kappa 值
        :param testData: 输入数据矩阵，N * k
        :param N: int, 样本数量
        :param k: int, 类别数量
        :param n: int, 评分者数量
        :return: float, Fleiss kappa 值
        >>> KappaCalculator.fleiss_kappa([[0, 0, 0, 0, 14],
                                         [0, 2, 6, 4, 2],
                                         [0, 0, 3, 5, 6],
                                         [0, 3, 9, 2, 0],
                                         [2, 2, 8, 1, 1],
                                         [7, 7, 0, 0, 0],
                                         [3, 2, 6, 3, 0],
                                         [2, 5, 3, 2, 2],
                                         [6, 5, 2, 1, 0],
                                         [0, 2, 2, 3, 7]], 10, 5, 14)
        0.20993070442195522
        """
        # Calculate the proportion of ratings for each category
        p = np.sum(testData, axis=0) / (N * n)
        
        # Calculate the overall agreement
        P = np.sum((np.sum(testData, axis=1) * (np.sum(testData, axis=1) - 1))) / (n * (n - 1) * N)
        
        # Calculate the expected agreement
        Pe = np.sum(p**2)
        
        # Calculate Fleiss' Kappa
        kappa_value = (P - Pe) / (1 - Pe)
        return kappa_value