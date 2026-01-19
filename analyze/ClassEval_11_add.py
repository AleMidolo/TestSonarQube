def add(states, stat):
    """
    मौजूदा स्टेटस में एक स्टेटस जोड़ें, और पैरामीटर्स चेक करें कि वे लीगल हैं या नहीं।

    :param states: मौजूदा स्टेटस, int.
    :param stat: जोड़ा जाने वाला स्टेटस, int.
    :return: स्टेटस जोड़ने के बाद का स्टेटस, int.

    >>> bit_status_util = BitStatusUtil()
    >>> bit_status_util.add(2, 4)
    6
    """
    # Validate parameters
    if not isinstance(states, int) or not isinstance(stat, int):
        raise TypeError("Both parameters must be integers")
    
    if states < 0 or stat < 0:
        raise ValueError("Parameters must be non-negative integers")
    
    # Add the status using bitwise OR operation
    # This ensures that the bit at the position of 'stat' is set in 'states'
    return states | stat