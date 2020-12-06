from functools import reduce

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def multiple_gcd(A):      # A is an array of intergers    
    return reduce(gcd, b)   

if __name__ == '__main__':    
    print(multiple_gcd([16, 32, 40]))
