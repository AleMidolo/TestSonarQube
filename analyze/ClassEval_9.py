class BigNumCalculator:
    @staticmethod
    def add(num1, num2):
        num1, num2 = BigNumCalculator._pad_numbers(num1, num2)
        carry = 0
        result = []

        for i in range(len(num1) - 1, -1, -1):
            digit_sum, carry = BigNumCalculator._calculate_digit_sum(num1[i], num2[i], carry)
            result.insert(0, str(digit_sum))

        if carry > 0:
            result.insert(0, str(carry))

        return ''.join(result)

    @staticmethod
    def subtract(num1, num2):
        num1, num2, negative = BigNumCalculator._prepare_subtraction(num1, num2)
        num1, num2 = BigNumCalculator._pad_numbers(num1, num2)
        borrow = 0
        result = []

        for i in range(len(num1) - 1, -1, -1):
            digit_diff, borrow = BigNumCalculator._calculate_digit_difference(num1[i], num2[i], borrow)
            result.insert(0, str(digit_diff))

        BigNumCalculator._remove_leading_zeros(result)

        if negative:
            result.insert(0, '-')

        return ''.join(result)

    @staticmethod
    def multiply(num1, num2):
        len1, len2 = len(num1), len(num2)
        result = [0] * (len1 + len2)

        for i in range(len1 - 1, -1, -1):
            for j in range(len2 - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1, p2 = i + j, i + j + 1
                total = mul + result[p2]

                result[p1] += total // 10
                result[p2] = total % 10

        start = 0
        while start < len(result) - 1 and result[start] == 0:
            start += 1

        return ''.join(map(str, result[start:]))

    @staticmethod
    def _pad_numbers(num1, num2):
        max_length = max(len(num1), len(num2))
        return num1.zfill(max_length), num2.zfill(max_length)

    @staticmethod
    def _calculate_digit_sum(digit1, digit2, carry):
        digit_sum = int(digit1) + int(digit2) + carry
        return digit_sum % 10, digit_sum // 10

    @staticmethod
    def _prepare_subtraction(num1, num2):
        if len(num1) < len(num2) or (len(num1) == len(num2) and num1 < num2):
            num1, num2 = num2, num1
            return num1, num2, True
        return num1, num2, False

    @staticmethod
    def _calculate_digit_difference(digit1, digit2, borrow):
        digit_diff = int(digit1) - int(digit2) - borrow
        if digit_diff < 0:
            digit_diff += 10
            borrow = 1
        else:
            borrow = 0
        return digit_diff, borrow

    @staticmethod
    def _remove_leading_zeros(result):
        while len(result) > 1 and result[0] == '0':
            result.pop(0)