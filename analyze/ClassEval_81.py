import math

class Statistics3:
    @staticmethod
    def median(data):
        sorted_data = sorted(data)
        n = len(sorted_data)
        return Statistics3._median_value(sorted_data, n)

    @staticmethod
    def _median_value(sorted_data, n):
        if n % 2 == 1:
            return sorted_data[n // 2]
        else:
            return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2

    @staticmethod
    def mode(data):
        counts = Statistics3._count_values(data)
        max_count = max(counts.values())
        mode_values = [value for value, count in counts.items() if count == max_count]
        return mode_values

    @staticmethod
    def _count_values(data):
        counts = {}
        for value in data:
            counts[value] = counts.get(value, 0) + 1
        return counts

    @staticmethod
    def correlation(x, y):
        n = len(x)
        mean_x = Statistics3.mean(x)
        mean_y = Statistics3.mean(y)
        numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
        denominator = Statistics3._correlation_denominator(x, mean_x, y, mean_y)
        if denominator == 0:
            return None
        return numerator / denominator

    @staticmethod
    def _correlation_denominator(x, mean_x, y, mean_y):
        return math.sqrt(sum((xi - mean_x) ** 2 for xi in x) * sum((yi - mean_y) ** 2 for yi in y))

    @staticmethod
    def mean(data):
        if len(data) == 0:
            return None
        return sum(data) / len(data)

    @staticmethod
    def correlation_matrix(data):
        matrix = []
        for i in range(len(data[0])):
            row = Statistics3._correlation_row(data, i)
            matrix.append(row)
        return matrix

    @staticmethod
    def _correlation_row(data, i):
        return [Statistics3.correlation([row[i] for row in data], [row[j] for row in data]) for j in range(len(data[0]))]

    @staticmethod
    def standard_deviation(data):
        n = len(data)
        if n < 2:
            return None
        mean_value = Statistics3.mean(data)
        variance = sum((x - mean_value) ** 2 for x in data) / (n - 1)
        return math.sqrt(variance)

    @staticmethod
    def z_score(data):
        mean_value = Statistics3.mean(data)
        std_deviation = Statistics3.standard_deviation(data)
        if std_deviation is None or std_deviation == 0:
            return None
        return [(x - mean_value) / std_deviation for x in data]