import numpy as np

class MetricsCalculator2: 
    def __init__(self):
        pass

    @staticmethod
    def map(data):
        """
            compute the MAP of the input data. MAP is a widely used evaluation index. It is the mean of AP (average precision).
            :param data: the data must be a tuple, list 0,1,eg.([1,0,...],5).  In each tuple (actual result,ground truth num),ground truth num is the total ground num.
             ([1,0,...],5),
            or list of tuple eg. [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)].
            1 stands for a correct answer, 0 stands for a wrong answer.
            :return: if input data is list, return the recall of this list. if the input data is list of list, return the
            average recall on all list. The second return value is a list of precision for each input.
            >>> MetricsCalculator2.map(([1, 0, 1, 0], 4))
            >>> MetricsCalculator2.map([([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)])
            0.41666666666666663, [0.41666666666666663]
            0.3333333333333333, [0.41666666666666663, 0.25]
        """
    
        if type(data) != list and type(data) != tuple:
            raise Exception(
                    "the input must be a tuple([0,...,1,...],int) or a iteration of list of tuple")

        if len(data) == 0:
            return 0.0, [0.0]
        if type(data) == tuple:
            (sub_list, total_num) = data
            sub_list = np.array(sub_list)
            if total_num == 0:
                return 0.0, [0.0]
            else:
                ranking_array = 1.0 / \
                        (np.array(list(range(len(sub_list)))) + 1)

                right_ranking_list = []
                count = 1
                for t in sub_list:
                    if t == 0:
                        right_ranking_list.append(0)
                    else:
                        right_ranking_list.append(count)
                        count += 1

                ap = np.sum(np.array(right_ranking_list)
                            * ranking_array) / total_num
                return ap, [ap]

        if type(data) == list:
            separate_result = []
            for (sub_list, total_num) in data:
                sub_list = np.array(sub_list)

                if total_num == 0:
                    ap = 0.0
                else:
                    ranking_array = 1.0 / \
                            (np.array(list(range(len(sub_list)))) + 1)

                    right_ranking_list = []
                    count = 1
                    for t in sub_list:
                        if t == 0:
                            right_ranking_list.append(0)
                        else:
                            right_ranking_list.append(count)
                            count += 1

                    ap = np.sum(np.array(right_ranking_list)
                                * ranking_array) / total_num

                separate_result.append(ap)
            return np.mean(separate_result), separate_result

    @staticmethod
    def mrr(data):
        """
        calcola l'MRR dei dati di input. L'MRR è un indice di valutazione ampiamente utilizzato. È la media del rango reciproco.
        :param data: i dati devono essere una tupla, lista 0,1, ad esempio ([1,0,...],5). In ogni tupla (risultato attuale, numero di verità di base), il numero di verità di base è il numero totale di verità di base.
         ([1,0,...],5),
        o lista di tuple ad esempio [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)].
        1 rappresenta una risposta corretta, 0 rappresenta una risposta sbagliata.
        :return: se i dati di input sono una lista, restituisce il richiamo di questa lista. se i dati di input sono una lista di liste, restituisce la
        media del richiamo su tutte le liste. Il secondo valore di ritorno è una lista di precisione per ciascun input.
        >>> MetricsCalculator2.mrr(([1, 0, 1, 0], 4))
        >>> MetricsCalculator2.mrr([([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)])
        1.0, [1.0]
        0.75, [1.0, 0.5]
        """
        if type(data) != list and type(data) != tuple:
            raise Exception(
                "the input must be a tuple([0,...,1,...],int) or a iteration of list of tuple")

        if len(data) == 0:
            return 0.0, [0.0]

        if type(data) == tuple:
            (sub_list, total_num) = data
            rank = np.where(np.array(sub_list) == 1)[0]
            if len(rank) == 0:
                return 0.0, [0.0]
            else:
                mrr_value = 1.0 / (rank[0] + 1)
                return mrr_value, [mrr_value]

        if type(data) == list:
            mrr_values = []
            for (sub_list, total_num) in data:
                rank = np.where(np.array(sub_list) == 1)[0]
                if len(rank) == 0:
                    mrr_values.append(0.0)
                else:
                    mrr_value = 1.0 / (rank[0] + 1)
                    mrr_values.append(mrr_value)
            return np.mean(mrr_values), mrr_values