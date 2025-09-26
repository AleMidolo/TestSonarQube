import numpy as np
from gensim import matutils
from numpy import dot, array


class VectorUtil:
    @staticmethod
    def similarity(vector_1, vector_2):
        return dot(matutils.unitvec(vector_1), matutils.unitvec(vector_2))

    @staticmethod
    def cosine_similarities(vector_1, vectors_all):
        norm = np.linalg.norm(vector_1)
        all_norms = np.linalg.norm(vectors_all, axis=1)
        dot_products = dot(vectors_all, vector_1)
        return VectorUtil._calculate_similarities(norm, all_norms, dot_products)

    @staticmethod
    def _calculate_similarities(norm, all_norms, dot_products):
        return dot_products / (norm * all_norms)

    @staticmethod
    def n_similarity(vector_list_1, vector_list_2):
        if not (len(vector_list_1) and len(vector_list_2)):
            raise ZeroDivisionError('At least one of the passed list is empty.')

        return dot(matutils.unitvec(array(vector_list_1).mean(axis=0)),
                   matutils.unitvec(array(vector_list_2).mean(axis=0)))

    @staticmethod
    def compute_idf_weight_dict(total_num, number_dict):
        index_2_key_map = {}
        count_list = []

        for index, (key, count) in enumerate(number_dict.items()):
            index_2_key_map[index] = key
            count_list.append(count)

        a = np.array(count_list)
        a = VectorUtil._smooth_idf(a, total_num)
        return VectorUtil._create_idf_dict(a, index_2_key_map)

    @staticmethod
    def _smooth_idf(count_array, total_num):
        return np.log((total_num + 1) / (count_array + 1))

    @staticmethod
    def _create_idf_dict(a, index_2_key_map):
        return {index_2_key_map[index]: w for index, w in enumerate(a)}