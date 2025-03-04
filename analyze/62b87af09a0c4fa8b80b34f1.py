def fill(self, coord, weight=1):
    """
    *coord* पर दिए गए *weight* के साथ हिस्टोग्राम को भरें।

    यदि *coord* हिस्टोग्राम की सीमाओं के बाहर है, तो उसे अनदेखा कर दिया जाएगा।
    """
    # Check if coordinate is within histogram bounds
    if not self._in_range(coord):
        return
        
    # Get bin index for the coordinate
    bin_idx = self._get_bin_index(coord)
    
    # Add weight to the bin
    self._bins[bin_idx] += weight