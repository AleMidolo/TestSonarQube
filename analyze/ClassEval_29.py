from collections import Counter


class DataStatistics:
    def mean(self, data):
        return round(self._calculate_mean(data), 2)

    def _calculate_mean(self, data):
        return sum(data) / len(data)

    def median(self, data):
        sorted_data = sorted(data)
        n = len(sorted_data)
        return self._calculate_median(sorted_data, n)

    def _calculate_median(self, sorted_data, n):
        if n % 2 == 0:
            middle = n // 2
            return round((sorted_data[middle - 1] + sorted_data[middle]) / 2, 2)
        else:
            middle = n // 2
            return sorted_data[middle]

    def mode(self, data):
        counter = Counter(data)
        mode_count = max(counter.values())
        return self._calculate_mode(counter, mode_count)

    def _calculate_mode(self, counter, mode_count):
        return [x for x, count in counter.items() if count == mode_count]