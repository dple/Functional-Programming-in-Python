from functools import reduce

def inner_product(a, b):
    return reduce(lambda x, y: x + y, map(lambda x, y: x * y, a, b))

if __name__ == '__main__':
    a = [3, 1, 2]
    b = [2, 4, 3]
    print(inner_product(a, b))
