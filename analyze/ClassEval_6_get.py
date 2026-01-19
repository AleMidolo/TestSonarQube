def get(self, index):
    """
    calcula el tamaño de cada bloque y el resto de la división, y calcula las posiciones de inicio y fin correspondientes basadas en el índice de la partición.
    :param index: el índice de la partición, int.
    :return: el bloque correspondiente, lista.
    >>> a = AvgPartition([1, 2, 3, 4], 2)
    >>> a.get(0)
    [1, 2]

    """
    total_length = len(self.data)
    num_partitions = self.num_partitions
    
    # Calcular el tamaño base de cada bloque y el resto
    base_size = total_length // num_partitions
    remainder = total_length % num_partitions
    
    # Las primeras 'remainder' particiones tendrán un elemento extra
    if index < remainder:
        start = index * (base_size + 1)
        end = start + base_size + 1
    else:
        start = remainder * (base_size + 1) + (index - remainder) * base_size
        end = start + base_size
    
    return self.data[start:end]