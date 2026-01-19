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
        raise Exception('the input must be a tuple or a list of tuples')
    if len(data) == 0:
        return (0.0, [])
    if type(data) == tuple:
        sub_list, total_num = data
        reciprocal_rank = 0.0
        for idx, value in enumerate(sub_list):
            if value == 1:
                reciprocal_rank = 1.0 / (idx + 1)
                break
        return (reciprocal_rank, [reciprocal_rank])
    if type(data) == list:
        reciprocal_ranks = []
        for sub_list, total_num in data:
            reciprocal_rank = 0.0
            for idx, value in enumerate(sub_list):
                if value == 1:
                    reciprocal_rank = 1.0 / (idx + 1)
                    break
            reciprocal_ranks.append(reciprocal_rank)
        return (np.mean(reciprocal_ranks), reciprocal_ranks)