import numpy as np

class KappaCalculator: 

    @staticmethod
    def fleiss_kappa(testData, N, k, n):
        """
            Calculate the fliss kappa value of an N * k matrix
            :param testData: Input data matrix, N * k
            :param N: int, Number of samples
            :param k: int, Number of categories
            :param n: int, Number of raters
            :return: float, fleiss kappa value
            >>> KappaCalculator.fleiss_kappa([[0, 0, 0, 0, 14],
            >>>                              [0, 2, 6, 4, 2],
            >>>                              [0, 0, 3, 5, 6],
            >>>                              [0, 3, 9, 2, 0],
            >>>                              [2, 2, 8, 1, 1],
            >>>                              [7, 7, 0, 0, 0],
            >>>                              [3, 2, 6, 3, 0],
            >>>                              [2, 5, 3, 2, 2],
            >>>                              [6, 5, 2, 1, 0],
            >>>                              [0, 2, 2, 3, 7]], 10, 5, 14)
            0.20993070442195522
            """
    
        dataMat = np.mat(testData, float)
        oneMat = np.ones((k, 1))
        sum = 0.0
        P0 = 0.0
        for i in range(N):
            temp = 0.0
            for j in range(k):
                sum += dataMat[i, j]
                temp += 1.0 * dataMat[i, j] ** 2
            temp -= n
            temp /= (n - 1) * n
            P0 += temp
        P0 = 1.0 * P0 / N
        ysum = np.sum(dataMat, axis=0)
        for i in range(k):
            ysum[0, i] = (ysum[0, i] / sum) ** 2
        Pe = ysum * oneMat * 1.0
        ans = (P0 - Pe) / (1 - Pe)
        return ans[0, 0]

    @staticmethod
    def kappa(testData, k):
        """
        计算k维矩阵的Cohen's kappa值
        :param testData: 需要计算Cohen's kappa值的k维矩阵
        :param k: int, 矩阵维度
        :return: float, 矩阵的Cohen's kappa值
        >>> KappaCalculator.kappa([[2, 1, 1], [1, 2, 1], [1, 1, 2]], 3)
        0.25
        """
        n = len(testData)
        p0 = 0.0
        p1 = 0.0
        
        for i in range(n):
            total = sum(testData[i])
            p0 += (total * (total - 1)) / (n * (n - 1))
            for j in range(k):
                p1 += (testData[i][j] * (testData[i][j] - 1)) / (n * (n - 1))
        
        p0 /= n
        p1 /= n
        
        kappa_value = (p0 - p1) / (1 - p1) if (1 - p1) != 0 else 0
        return kappa_value