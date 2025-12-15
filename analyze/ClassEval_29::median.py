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
    
    def mode(self, data):
        """
        Calculate the mode of a set of data
        :param data:list, data list
        :return:float, the mode
        >>> ds = DataStatistics()
        >>> ds.mode([2, 2, 3, 3, 4])
        [2, 3]
        """
        counter = Counter(data)
        mode_count = max(counter.values())
        mode = [x for x, count in counter.items() if count == mode_count]
        return mode
    
    def median(self, data):
        """
        डेसिमल सेपरेटर के बाद दो डिजिट तक सटीक, डेटा के ग्रुप का मीडियन कैलकुलेट करें।

        :param data: list, डेटा लिस्ट
        :return: float, मीडियन वैल्यू

        >>> ds = DataStatistics()
        >>> ds.median([2, 5, 1, 3, 4])
        3.00
        """
        sorted_data = sorted(data)
        n = len(sorted_data)
        mid = n // 2
        
        if n % 2 == 0:
            return round((sorted_data[mid - 1] + sorted_data[mid]) / 2, 2)
        else:
            return round(sorted_data[mid], 2)