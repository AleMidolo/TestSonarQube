@staticmethod
def correlation_matrix(data):
    """
    दिए गए सूची का सहसंबंध मैट्रिक्स की गणना करता है।
    :param data: दी गई सूची, सूची।
    :return: दी गई सूची का सहसंबंध मैट्रिक्स, सूची।
    >>> statistics3 = Statistics3()
    >>> statistics3.correlation_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]

    """
    n = len(data)
    
    # Calculate means for each row
    means = []
    for row in data:
        means.append(sum(row) / len(row))
    
    # Calculate standard deviations for each row
    std_devs = []
    for i in range(n):
        variance = sum((x - means[i]) ** 2 for x in data[i]) / len(data[i])
        std_devs.append(variance ** 0.5)
    
    # Initialize correlation matrix
    corr_matrix = [[0.0 for _ in range(n)] for _ in range(n)]
    
    # Calculate correlation coefficients
    for i in range(n):
        for j in range(n):
            if std_devs[i] == 0 or std_devs[j] == 0:
                # If standard deviation is 0, correlation is 1 (constant values)
                corr_matrix[i][j] = 1.0
            else:
                # Calculate covariance
                covariance = sum((data[i][k] - means[i]) * (data[j][k] - means[j]) 
                                for k in range(len(data[i]))) / len(data[i])
                # Calculate correlation coefficient
                corr_matrix[i][j] = covariance / (std_devs[i] * std_devs[j])
    
    return corr_matrix