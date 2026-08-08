def get_surrounding_sqrs(x, y):
    surrounding_sqr = [[x + i, y + j] for j in range(-1, 2) for i in range(-1, 2)]
    return surrounding_sqr

