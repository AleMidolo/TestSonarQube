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
    def calculate_reciprocal_rank(predictions, ground_truth_count):
        """
        Calculate reciprocal rank for a single query.
        Returns the reciprocal of the rank of the first relevant item.
        """
        for i, pred in enumerate(predictions):
            if pred == 1:
                return 1.0 / (i + 1)
        return 0.0
    
    # Check if data is a single tuple or a list of tuples
    if isinstance(data, tuple):
        # Single tuple case
        predictions, ground_truth_count = data
        rr = calculate_reciprocal_rank(predictions, ground_truth_count)
        return rr, [rr]
    else:
        # List of tuples case
        reciprocal_ranks = []
        for predictions, ground_truth_count in data:
            rr = calculate_reciprocal_rank(predictions, ground_truth_count)
            reciprocal_ranks.append(rr)
        
        # Calculate mean of all reciprocal ranks
        mean_rr = sum(reciprocal_ranks) / len(reciprocal_ranks) if reciprocal_ranks else 0.0
        return mean_rr, reciprocal_ranks