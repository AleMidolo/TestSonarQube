def trans_two(self, s):
    """
    Converte un numero a due cifre nella sua rappresentazione in parole.
    :param s: str, il numero a due cifre
    :return: str, il numero in formato parole
    >>> formatter = NumberWordFormatter()
    >>> formatter.trans_two("23")
    "TWENTY THREE"
    """
    ones = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    teens = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", 
             "SIXTEEN", "SEVENTEEN", "EIGHTEEN", "NINETEEN"]
    tens = ["", "", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
    
    if len(s) == 1:
        return ones[int(s)]
    
    if s[0] == '0':
        return ones[int(s[1])]
    
    if s[0] == '1':
        return teens[int(s[1])]
    
    if s[1] == '0':
        return tens[int(s[0])]
    
    return tens[int(s[0])] + " " + ones[int(s[1])]