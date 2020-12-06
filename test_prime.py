import numpy as np

def isPrime(p):
    """  Checking if p is a prime by using the observation that: p = 6k +/- 1 if p > 3 """
    if p <= 3:
        return p > 1
    if p % 2 == 0 or p % 3 == 0:
        return False

    sqrt = np.sqrt(p).astype(np.int64) + 1
    for i in filter(lambda x: x % 6 == 1 or x % 6 == 5, range(5, sqrt)): 
        if p % i == 0: 
            return False

    return True

if __name__ == '__main__':
    p = 31
    if isPrime(p):
        print("{} is a prime".format(p))
    else:
        print("{} is not a prime".format(p))
