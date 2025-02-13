def vertex3tuple(vertices):
    result = []
    n = len(vertices)
    for i in range(n):
        left1 = vertices[i - 1] if i - 1 >= 0 else vertices[0]
        left2 = vertices[i - 2] if i - 2 >= 0 else vertices[0]
        right1 = vertices[(i + 1) % n]
        right2 = vertices[(i + 2) % n]
        result.append((left2, left1, vertices[i], right1, right2))
    return result