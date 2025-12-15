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
        Calcola la mediana di un gruppo di dati, con una precisione di due cifre decimali.
        :param data: list, lista dei dati
        :return: float, il valore della mediana
        >>> ds = DataStatistics()
        >>> ds.median([2, 5, 1, 3, 4])
        3.00
        """
        sorted_data = sorted(data)
        n = len(sorted_data)
        mid = n // 2
        
        if n % 2 == 0:
            median_value = (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            median_value = sorted_data[mid]
        
        return round(median_value, 2)