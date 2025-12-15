def correlation_coefficient(data1, data2):
        """
        Calcola il coefficiente di correlazione di due insiemi di dati.
        :param data1: Il primo insieme di dati, lista.
        :param data2: Il secondo insieme di dati, lista.
        :return: Il coefficiente di correlazione, float.
        >>> correlation_coefficient([1, 2, 3], [4, 5, 6])
        0.9999999999999998

        """
        if len(data1) != len(data2):
            raise ValueError("Le due liste devono avere la stessa lunghezza.")
        
        n = len(data1)
        mean1 = sum(data1) / n
        mean2 = sum(data2) / n
        
        numerator = sum((data1[i] - mean1) * (data2[i] - mean2) for i in range(n))
        denominator1 = math.sqrt(sum((data1[i] - mean1) ** 2 for i in range(n)))
        denominator2 = math.sqrt(sum((data2[i] - mean2) ** 2 for i in range(n)))
        
        if denominator1 == 0 or denominator2 == 0:
            return 0.0
        
        return numerator / (denominator1 * denominator2)