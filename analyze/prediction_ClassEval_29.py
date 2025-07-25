from collections import Counter


class DataStatistics:
    def mean(self, data):
        return round(self._calculate_sum(data) / len(data), 2)

    def median(self, data):
        sorted_data = sorted(data)
        n = len(sorted_data)
        return round(self._calculate_median(sorted_data, n), 2)

    def mode(self, data):
        counter = Counter(data)
        mode_count = max(counter.values())
        return self._calculate_mode(counter, mode_count)

    def _calculate_sum(self, data):
        return sum(data)

    def _calculate_median(self, sorted_data, n):
        if n % 2 == 0:
            middle = n // 2
            return (sorted_data[middle - 1] + sorted_data[middle]) / 2
        else:
            middle = n // 2
            return sorted_data[middle]

    def _calculate_mode(self, counter, mode_count):
        return [x for x, count in counter.items() if count == mode_count]