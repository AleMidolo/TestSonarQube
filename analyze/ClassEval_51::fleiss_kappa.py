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
        sum = np.sum(dataMat)
        Pe = float(ysum * xsum) / sum / sum
        P0 = float(P0 / sum * 1.0)
        cohens_coefficient = float((P0 - Pe) / (1 - Pe))
        return cohens_coefficient
    
    @staticmethod
    def fleiss_kappa(testData, N, k, n):
        """
        Calcola il valore di kappa di Fleiss per una matrice N * k
        :param testData: Matrice di dati di input, N * k
        :param N: int, Numero di campioni
        :param k: int, Numero di categorie
        :param n: int, Numero di valutatori
        :return: float, valore di kappa di Fleiss
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
        # Calculate the proportion of agreement for each category
        p = np.sum(testData, axis=0) / (N * n)
        
        # Calculate the overall agreement
        P = np.sum(p**2)
        
        # Calculate the expected agreement
        Pe = np.sum((np.sum(testData, axis=1) / n)**2) / N
        
        # Calculate Fleiss' kappa
        kappa_value = (P - Pe) / (1 - Pe)
        return kappa_value