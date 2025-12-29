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
    if not isinstance(data, (list, tuple)):
        raise Exception('the input must be a tuple([0,...,1,...],int) or a list of tuples')
    if isinstance(data, tuple):
        if len(data) != 2:
            raise Exception('tuple must have format ([binary_list], ground_truth_count)')
        sub_list, total_num = data
        sub_list = np.array(sub_list)
        if total_num == 0:
            return (0.0, [0.0])
        indices = np.where(sub_list == 1)[0]
        if len(indices) == 0:
            rr = 0.0
        else:
            first_correct_rank = indices[0] + 1
            rr = 1.0 / first_correct_rank
        return (rr, [rr])
    elif isinstance(data, list):
        if len(data) == 0:
            return (0.0, [0.0])
        separate_result = []
        for item in data:
            if not isinstance(item, tuple) or len(item) != 2:
                raise Exception('each item in list must be a tuple([binary_list], ground_truth_count)')
            sub_list, total_num = item
            sub_list = np.array(sub_list)
            indices = np.where(sub_list == 1)[0]
            if len(indices) == 0:
                rr = 0.0
            else:
                first_correct_rank = indices[0] + 1
                rr = 1.0 / first_correct_rank
            separate_result.append(rr)
        mean_rr = np.mean(separate_result)
        return (mean_rr, separate_result)