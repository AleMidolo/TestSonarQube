import math

class DataStatistics4:

    @staticmethod
    def correlation_coefficient(data1, data2):
        n = len(data1)
        mean1 = DataStatistics4.calculate_mean(data1, n)
        mean2 = DataStatistics4.calculate_mean(data2, n)

        numerator = DataStatistics4.calculate_numerator(data1, data2, mean1, mean2, n)
        denominator = DataStatistics4.calculate_denominator(data1, data2, mean1, mean2, n)

        return numerator / denominator if denominator != 0 else 0

    @staticmethod
    def calculate_mean(data, n):
        return sum(data) / n

    @staticmethod
    def calculate_numerator(data1, data2, mean1, mean2, n):
        return sum((data1[i] - mean1) * (data2[i] - mean2) for i in range(n))

    @staticmethod
    def calculate_denominator(data1, data2, mean1, mean2, n):
        return math.sqrt(sum((data1[i] - mean1) ** 2 for i in range(n))) * \
               math.sqrt(sum((data2[i] - mean2) ** 2 for i in range(n)))

    @staticmethod
    def skewness(data):
        n = len(data)
        mean = DataStatistics4.calculate_mean(data, n)
        std_deviation = DataStatistics4.calculate_std_deviation(data, mean, n)

        skewness = DataStatistics4.calculate_skewness(data, mean, n, std_deviation)

        return skewness

    @staticmethod
    def calculate_std_deviation(data, mean, n):
        variance = sum((x - mean) ** 2 for x in data) / n
        return math.sqrt(variance)

    @staticmethod
    def calculate_skewness(data, mean, n, std_deviation):
        return sum((x - mean) ** 3 for x in data) * n / ((n - 1) * (n - 2) * std_deviation ** 3) if std_deviation != 0 else 0

    @staticmethod
    def kurtosis(data):
        n = len(data)
        mean = DataStatistics4.calculate_mean(data, n)
        std_dev = DataStatistics4.calculate_std_deviation(data, mean, n)

        if std_dev == 0:
            return math.nan

        centered_data = [(x - mean) for x in data]
        fourth_moment = sum(x ** 4 for x in centered_data) / n

        kurtosis_value = (fourth_moment / std_dev ** 4) - 3

        return kurtosis_value

    @staticmethod
    def pdf(data, mu, sigma):
        pdf_values = [1 / (sigma * math.sqrt(2 * math.pi)) * math.exp(-0.5 * ((x - mu) / sigma) ** 2) for x in data]
        return pdf_values