class BigNumCalculator: 

    def add(num1, num2):
        """
        Adds two big numbers.
        :param num1: The first number to add,str.
        :param num2: The second number to add,str.
        :return: The sum of the two numbers,str.
        >>> bigNum = BigNumCalculator()
        >>> bigNum.add("12345678901234567890", "98765432109876543210")
        '111111111011111111100'
        """
    
        max_length = max(len(num1), len(num2))
        num1 = num1.zfill(max_length)
        num2 = num2.zfill(max_length)
    
        carry = 0
        result = []
        for i in range(max_length - 1, -1, -1):
            digit_sum = int(num1[i]) + int(num2[i]) + carry
            carry = digit_sum // 10
            digit = digit_sum % 10
            result.insert(0, str(digit))
    
        if carry > 0:
            result.insert(0, str(carry))
    
        return ''.join(result)
    
    @staticmethod
    def subtract(num1, num2):
        """
            Subtracts two big numbers.
            :param num1: The first number to subtract,str.
            :param num2: The second number to subtract,str.
            :return: The difference of the two numbers,str.
            >>> bigNum = BigNumCalculator()
            >>> bigNum.subtract("12345678901234567890", "98765432109876543210")
            '-86419753208641975320'
        """
    
        if len(num1) < len(num2):
            num1, num2 = num2, num1
            negative = True
        elif len(num1) > len(num2):
            negative = False
        else:
            if num1 < num2:
                num1, num2 = num2, num1
                negative = True
            else:
                negative = False

        max_length = max(len(num1), len(num2))
        num1 = num1.zfill(max_length)
        num2 = num2.zfill(max_length)

        borrow = 0
        result = []
        for i in range(max_length - 1, -1, -1):
            digit_diff = int(num1[i]) - int(num2[i]) - borrow

            if digit_diff < 0:
                digit_diff += 10
                borrow = 1
            else:
                borrow = 0

            result.insert(0, str(digit_diff))

        while len(result) > 1 and result[0] == '0':
            result.pop(0)

        if negative:
            result.insert(0, '-')

        return ''.join(result)

    @staticmethod
    def multiply(num1, num2):
        """
        दो बड़े संख्याओं को गुणा करता है।
        :param num1: गुणा करने के लिए पहला संख्या, str.
        :param num2: गुणा करने के लिए दूसरा संख्या, str.
        :return: दोनों संख्याओं का गुणनफल, str.
        >>> bigNum = BigNumCalculator()
        >>> bigNum.multiply("12345678901234567890", "98765432109876543210")
        '1219326311370217952237463801111263526900'
        """
        if num1 == "0" or num2 == "0":
            return "0"

        result = "0"
        num2_len = len(num2)
        
        for i in range(num2_len):
            digit = int(num2[num2_len - 1 - i])
            if digit != 0:
                partial_product = BigNumCalculator.add(num1 + '0' * i, '0' * (len(num1) + i - 1))
                result = BigNumCalculator.add(result, partial_product)

        return result