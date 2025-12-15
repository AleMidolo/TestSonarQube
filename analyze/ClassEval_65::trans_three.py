def trans_three(self, s):
        """
        将三位数转换为单词格式
        :param s: str，三位数
        :return: str，数字的单词格式
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_three("123")
        "ONE HUNDRED AND TWENTY THREE"
        """
        s = s.zfill(3)
        if s[0] != "0":
            return self.NUMBER[int(s[0])] + " HUNDRED" + (" AND " + self.trans_two(s[1:]) if s[1:] != "00" else "")
        else:
            return self.trans_two(s[1:])