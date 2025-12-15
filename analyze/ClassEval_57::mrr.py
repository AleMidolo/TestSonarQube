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
        इनपुट डेटा का MRR (Mean Reciprocal Rank) कैलकुलेट करें।
        MRR एक आम तौर पर इस्तेमाल होने वाला इवैल्यूएशन इंडेक्स है, जो रेसिप्रोकल रैंक का मीन होता है।

        :param data: डेटा एक टपल या टपल की लिस्ट हो सकता है।
                     टपल का फ़ॉर्मेट: ([1, 0, ...], ground_truth_count)
                     उदाहरण:
                         ([1, 0, ...], 5)
                         [([1, 0, 1, ...], 5), ([1, 0, ...], 6), ([0, 0, ...], 5)]
                     1 सही जवाब दिखाता है, 0 गलत जवाब दिखाता है।

        :return: 
            - अगर इनपुट एक टपल है → उसकी MRR वैल्यू
            - अगर इनपुट टपल की एक लिस्ट है → सभी की एवरेज MRR वैल्यू
            - साथ में एक लिस्ट जिसमें हर इनपुट के लिए प्रिसिजन/रिसिप्रोकल रैंक शामिल हों।

        >>> MetricsCalculator2.mrr(([1, 0, 1, 0], 4))
        1.0, [1.0]

        >>> MetricsCalculator2.mrr([([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)])
        0.75, [1.0, 0.5]
        """
        if type(data) != list and type(data) != tuple:
            raise Exception("the input must be a tuple or a list of tuples")

        if type(data) == tuple:
            data = [data]

        reciprocal_ranks = []
        for (sub_list, total_num) in data:
            if total_num == 0:
                reciprocal_ranks.append(0.0)
                continue

            try:
                first_correct_index = sub_list.index(1)
                reciprocal_rank = 1 / (first_correct_index + 1)
            except ValueError:
                reciprocal_rank = 0.0

            reciprocal_ranks.append(reciprocal_rank)

        return np.mean(reciprocal_ranks), reciprocal_ranks