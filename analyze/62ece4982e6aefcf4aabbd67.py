def vertex3tuple(vertices):
    """
    प्रत्येक वर्टेक्स के लिए 3 पॉइंट्स लौटाएगा।  
    यह वर्टेक्स और उसके दोनों ओर के 2 पॉइंट्स को शामिल करेगा।  

    उदाहरण के लिए:  
    यदि पॉलीगॉन के वर्टेक्स ABCD हैं, तो यह निम्नलिखित 3-ट्यूपल्स लौटाएगा:  
    `DAB, ABC, BCD, CDA`  
    वर्टेक्स का क्रम:

    # A    B    C    D  -> वर्टेक्स का क्रम
    """
    n = len(vertices)
    result = []
    for i in range(n):
        # Get the current vertex and its two neighbors
        current = vertices[i]
        prev = vertices[(i - 1) % n]
        next_ = vertices[(i + 1) % n]
        result.append((prev, current, next_))
    return result