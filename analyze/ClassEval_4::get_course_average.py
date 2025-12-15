def get_course_average(self, course):
        """
        एक विशेष पाठ्यक्रम का औसत स्कोर प्राप्त करें।
        :param course: str, पाठ्यक्रम का नाम
        :return: float, यदि किसी के पास इस पाठ्यक्रम का स्कोर है तो इस पाठ्यक्रम का औसत स्कोर, या यदि किसी के पास रिकॉर्ड नहीं है तो None।
        """
        total_score = 0
        count = 0
        for student in self.students.values():
            if course in student['courses']:
                total_score += student['courses'][course]
                count += 1
        if count > 0:
            return total_score / count
        return None