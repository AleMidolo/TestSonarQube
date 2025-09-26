import numpy as np


class MetricsCalculator2:
    def __init__(self):
        pass

    @staticmethod
    def mrr(data):
        MetricsCalculator2._validate_input(data)

        if len(data) == 0:
            return 0.0, [0.0]

        if isinstance(data, tuple):
            return MetricsCalculator2._calculate_mrr_for_tuple(data)

        if isinstance(data, list):
            return MetricsCalculator2._calculate_mrr_for_list(data)

    @staticmethod
    def map(data):
        MetricsCalculator2._validate_input(data)

        if len(data) == 0:
            return 0.0, [0.0]

        if isinstance(data, tuple):
            return MetricsCalculator2._calculate_map_for_tuple(data)

        if isinstance(data, list):
            return MetricsCalculator2._calculate_map_for_list(data)

    @staticmethod
    def _validate_input(data):
        if not isinstance(data, (list, tuple)):
            raise Exception("the input must be a tuple([0,...,1,...],int) or a iteration of list of tuple")

    @staticmethod
    def _calculate_mrr_for_tuple(data):
        (sub_list, total_num) = data
        sub_list = np.array(sub_list)
        if total_num == 0:
            return 0.0, [0.0]

        ranking_array = 1.0 / (np.arange(len(sub_list)) + 1)
        mr_np = sub_list * ranking_array

        mr = MetricsCalculator2._first_positive(mr_np)
        return mr, [mr]

    @staticmethod
    def _calculate_mrr_for_list(data):
        separate_result = []
        for (sub_list, total_num) in data:
            sub_list = np.array(sub_list)
            mr = 0.0 if total_num == 0 else MetricsCalculator2._calculate_mrr_for_tuple((sub_list, total_num))[0]
            separate_result.append(mr)
        return np.mean(separate_result), separate_result

    @staticmethod
    def _calculate_map_for_tuple(data):
        (sub_list, total_num) = data
        sub_list = np.array(sub_list)
        if total_num == 0:
            return 0.0, [0.0]

        ranking_array = 1.0 / (np.arange(len(sub_list)) + 1)
        right_ranking_list = MetricsCalculator2._calculate_right_ranking(sub_list)

        ap = np.sum(np.array(right_ranking_list) * ranking_array) / total_num
        return ap, [ap]

    @staticmethod
    def _calculate_map_for_list(data):
        separate_result = []
        for (sub_list, total_num) in data:
            sub_list = np.array(sub_list)
            ap = 0.0 if total_num == 0 else MetricsCalculator2._calculate_map_for_tuple((sub_list, total_num))[0]
            separate_result.append(ap)
        return np.mean(separate_result), separate_result

    @staticmethod
    def _calculate_right_ranking(sub_list):
        right_ranking_list = []
        count = 1
        for t in sub_list:
            if t == 0:
                right_ranking_list.append(0)
            else:
                right_ranking_list.append(count)
                count += 1
        return right_ranking_list

    @staticmethod
    def _first_positive(mr_np):
        for team in mr_np:
            if team > 0:
                return team
        return 0.0