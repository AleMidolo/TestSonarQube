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
    if len(data) == 0:
        return (0.0, [0.0])
    if isinstance(data, tuple):
        sub_list, total_num = data
        sub_list = np.array(sub_list)
        if total_num == 0:
            return (0.0, [0.0])
        first_correct_idx = np.where(sub_list == 1)[0]
        if len(first_correct_idx) == 0:
            rr = 0.0
        else:
            rr = 1.0 / (first_correct_idx[0] + 1)
        return (rr, [rr])
    if isinstance(data, list):
        separate_result = []
        for sub_list, total_num in data:
            sub_list = np.array(sub_list)
            if total_num == 0:
                rr = 0.0
            else:
                first_correct_idx = np.where(sub_list == 1)[0]
                if len(first_correct_idx) == 0:
                    rr = 0.0
                else:
                    rr = 1.0 / (first_correct_idx[0] + 1)
            separate_result.append(rr)
        mean_rr = np.mean(separate_result) if separate_result else 0.0
        return (mean_rr, separate_result)