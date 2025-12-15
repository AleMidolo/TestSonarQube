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
    def multiply(num1, num2):
        """
            Multiplies two big numbers.
            :param num1: The first number to multiply,str.
            :param num2: The second number to multiply,str.
            :return: The product of the two numbers,str.
            >>> bigNum = BigNumCalculator()
            >>> bigNum.multiply("12345678901234567890", "98765432109876543210")
            '1219326311370217952237463801111263526900'
        """
    
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
        
        # Ensure num1 is greater than num2 for simplicity
        if num1 == num2:
            return '0'
        
        # Determine if the result will be negative
        negative = False
        if num1 < num2:
            num1, num2 = num2, num1
            negative = True
        
        max_length = max(len(num1), len(num2))
        num1 = num1.zfill(max_length)
        num2 = num2.zfill(max_length)
        
        result = []
        borrow = 0
        
        for i in range(max_length - 1, -1, -1):
            sub = int(num1[i]) - int(num2[i]) - borrow
            if sub < 0:
                sub += 10
                borrow = 1
            else:
                borrow = 0
            result.insert(0, str(sub))
        
        # Remove leading zeros
        while len(result) > 1 and result[0] == '0':
            result.pop(0)
        
        return ('-' if negative else '') + ''.join(result)