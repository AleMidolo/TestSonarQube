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

    >>> metrics_calculator.mrr(([1, 0, 1, 0], 4))
    1.0, [1.0]

    >>> metrics_calculator.mrr([([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)])
    0.75, [1.0, 0.5]
    """
    if type(data) != list and type(data) != tuple:
        raise Exception('the input must be a tuple([0,...,1,...],int) or a iteration of list of tuple')
    if len(data) == 0:
        return (0.0, [0.0])

    def calculate_mrr(sub_list, total_num):
        if total_num == 0:
            return 0.0
        for idx, value in enumerate(sub_list):
            if value == 1:
                return 1.0 / (idx + 1)
        return 0.0
    if type(data) == tuple:
        sub_list, total_num = data
        mrr_value = calculate_mrr(sub_list, total_num)
        return (mrr_value, [mrr_value])
    if type(data) == list:
        mrr_values = []
        for sub_list, total_num in data:
            mrr_value = calculate_mrr(sub_list, total_num)
            mrr_values.append(mrr_value)
        return (np.mean(mrr_values), mrr_values)