from collections import Counter

class DataStatistics: 

    def mean(self, data):
        """
        Calculate the average value of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the mean value
        >>> ds = DataStatistics()
        >>> ds.mean([1, 2, 3, 4, 5])
        3.00
        """
        return round(sum(data) / len(data), 2)
    
    def median(self, data):
        """
        Calculate the median of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the median value
        >>> ds = DataStatistics()
        >>> ds.median([2, 5, 1, 3, 4])
        3.00
        """
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n % 2 == 0:
            middle = n // 2
            return round((sorted_data[middle - 1] + sorted_data[middle]) / 2, 2)
        else:
            middle = n // 2
            return round(sorted_data[middle], 2)

    def mode(self, data):
        """
        डेटा के एक सेट का मोड कैलकुलेट करें।

        :param data: list, डेटा लिस्ट
        :return: float, मोड

        >>> ds = DataStatistics()
        >>> ds.mode([2, 2, 3, 3, 4])
        [2, 3]
        """
        count = Counter(data)
        max_freq = max(count.values())
        modes = [key for key, freq in count.items() if freq == max_freq]
        return modes