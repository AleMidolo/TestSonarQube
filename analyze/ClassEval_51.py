import numpy as np


class KappaCalculator:
    TOTAL_SUM = 1.0

    @staticmethod
    def kappa(testData, k):
        dataMat = np.mat(testData)
        P0 = KappaCalculator.calculate_P0(dataMat, k)
        Pe = KappaCalculator.calculate_Pe(dataMat)
        cohens_coefficient = KappaCalculator.calculate_cohens_coefficient(P0, Pe)
        return cohens_coefficient

    @staticmethod
    def fleiss_kappa(testData, N, k, n):
        dataMat = np.mat(testData, float)
        P0 = KappaCalculator.calculate_fleiss_P0(dataMat, N, k, n)
        Pe = KappaCalculator.calculate_fleiss_Pe(dataMat, k)
        ans = (P0 - Pe) / (KappaCalculator.TOTAL_SUM - Pe)
        return ans[0, 0]

    @staticmethod
    def calculate_P0(dataMat, k):
        P0 = 0.0
        for i in range(k):
            P0 += dataMat[i, i] * KappaCalculator.TOTAL_SUM
        return float(P0 / np.sum(dataMat) * KappaCalculator.TOTAL_SUM)

    @staticmethod
    def calculate_Pe(dataMat):
        xsum = np.sum(dataMat, axis=1)
        ysum = np.sum(dataMat, axis=0)
        total_sum = np.sum(dataMat)
        return float(ysum * xsum) / (total_sum ** 2)

    @staticmethod
    def calculate_cohens_coefficient(P0, Pe):
        return float((P0 - Pe) / (KappaCalculator.TOTAL_SUM - Pe))

    @staticmethod
    def calculate_fleiss_P0(dataMat, N, k, n):
        P0 = 0.0
        for i in range(N):
            temp = KappaCalculator.calculate_temp(dataMat, i, k, n)
            P0 += temp
        return KappaCalculator.TOTAL_SUM * P0 / N

    @staticmethod
    def calculate_temp(dataMat, i, k, n):
        temp = 0.0
        for j in range(k):
            temp += KappaCalculator.TOTAL_SUM * dataMat[i, j] ** 2
        temp -= n
        return temp / ((n - 1) * n)

    @staticmethod
    def calculate_fleiss_Pe(dataMat, k):
        ysum = np.sum(dataMat, axis=0)
        total_sum = np.sum(dataMat)
        for i in range(k):
            ysum[0, i] = (ysum[0, i] / total_sum) ** 2
        return ysum * np.ones((k, 1)) * KappaCalculator.TOTAL_SUM