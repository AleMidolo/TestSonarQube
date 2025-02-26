def fill(self, coord, weight=1):
    """
    *coord* पर दिए गए *weight* के साथ हिस्टोग्राम को भरें।

    यदि *coord* हिस्टोग्राम की सीमाओं के बाहर है, तो उसे अनदेखा कर दिया जाएगा।
    """
    if not self.is_within_bounds(coord):
        return
    self.histogram[coord] += weight