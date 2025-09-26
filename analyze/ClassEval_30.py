import numpy as np


class DataStatistics2:
    def __init__(self, data):
        self.data = np.array(data)

    def get_sum(self):
        return self._calculate_sum()

    def get_min(self):
        return self._calculate_min()

    def get_max(self):
        return self._calculate_max()

    def get_variance(self):
        return self._calculate_variance()

    def get_std_deviation(self):
        return self._calculate_std_deviation()

    def get_correlation(self):
        return self._calculate_correlation()

    def _calculate_sum(self):
        return np.sum(self.data)

    def _calculate_min(self):
        return np.min(self.data)

    def _calculate_max(self):
        return np.max(self.data)

    def _calculate_variance(self):
        return round(np.var(self.data), 2)

    def _calculate_std_deviation(self):
        return round(np.std(self.data), 2)

    def _calculate_correlation(self):
        return np.corrcoef(self.data, rowvar=False)