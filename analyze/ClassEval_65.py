class NumberWordFormatter:
    def __init__(self):
        self.NUMBER = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
        self.NUMBER_TEEN = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", "SIXTEEN", "SEVENTEEN",
                            "EIGHTEEN", "NINETEEN"]
        self.NUMBER_TEN = ["TEN", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
        self.NUMBER_MORE = ["", "THOUSAND", "MILLION", "BILLION"]
        self.NUMBER_SUFFIX = ["k", "w", "", "m", "", "", "b", "", "", "t", "", "", "p", "", "", "e"]

    def format(self, x):
        return self.format_string(str(x)) if x is not None else ""

    def format_string(self, x):
        lstr, rstr = self.split_number_string(x)
        lstrrev = lstr[::-1]
        lstrrev = self.pad_left(lstrrev)

        lm = self.convert_integer_part(lstrrev)
        xs = self.format_cents(rstr)

        return self.format_final_output(lm, xs)

    def split_number_string(self, x):
        return (x.split('.') + [''])[:2]

    def pad_left(self, lstrrev):
        if len(lstrrev) % 3 == 1:
            return lstrrev + "00"
        elif len(lstrrev) % 3 == 2:
            return lstrrev + "0"
        return lstrrev

    def convert_integer_part(self, lstrrev):
        a = [''] * 5
        lm = ""
        for i in range(len(lstrrev) // 3):
            a[i] = lstrrev[3 * i:3 * i + 3][::-1]
            lm = self.append_translated_part(a[i], lm, i)
        return lm

    def append_translated_part(self, part, lm, index):
        if part != "000":
            return self.trans_three(part) + " " + self.parse_more(index) + " " + lm
        return lm + self.trans_three(part)

    def format_cents(self, rstr):
        return f"AND CENTS {self.trans_two(rstr)} " if rstr else ""

    def format_final_output(self, lm, xs):
        if not lm.strip():
            return "ZERO ONLY"
        return f"{lm.strip()} {xs}ONLY"

    def trans_two(self, s):
        s = s.zfill(2)
        if s[0] == "0":
            return self.NUMBER[int(s[-1])]
        elif s[0] == "1":
            return self.NUMBER_TEEN[int(s) - 10]
        elif s[1] == "0":
            return self.NUMBER_TEN[int(s[0]) - 1]
        else:
            return self.NUMBER_TEN[int(s[0]) - 1] + " " + self.NUMBER[int(s[-1])]

    def trans_three(self, s):
        if s[0] == "0":
            return self.trans_two(s[1:])
        elif s[1:] == "00":
            return f"{self.NUMBER[int(s[0])]} HUNDRED"
        else:
            return f"{self.NUMBER[int(s[0])]} HUNDRED AND {self.trans_two(s[1:])}"

    def parse_more(self, i):
        return self.NUMBER_MORE[i]