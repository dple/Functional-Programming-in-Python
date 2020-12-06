# Functional Programming in Python

In the following we examine high order functions in Python.

## Reduce

Function **reduce**(function, seq) is introduced in the package functools. This function will apply a particular *function* (1st argument) to all elements mentioned in the sequence *seq*. 

Consider the following example. Let *a<sub>0</sub>, a<sub>1</sub>, ..., a<sub>n - 1</sub>* be integers. Find **Greatest Common Divisor**, *gcd* of those numbers. One method for this problem is to find *gcd(a<sub>0</sub>, a<sub>1</sub>)*, then *gcd(gcd(a<sub>0</sub>, a<sub>1</sub>), a<sub>2</sub>)*, and so on. This will be implemented as follows:


```
def gcd(a, b):
  while b:
    a, b = b, a % b
  return a

def multiple_gcd(arr):     # a is an array
  n = len(arr)
  c = gcd(arr[0], arr[1])
  for i in range(2, n):
    c = gcd(c, arr[i])
  return c
```

By using function **reduce**, code can be simplified as follows:

```
def multiple_gcd(arr):
  return reduce(gcd, arr) 
```

## Map
Function **map**(function, iter) allows us to apply a *function* to every element in an iterable object. For example, Ceasar cipher can be implemented by using **map()** as follows:

```
def ceasar_cipher(plain):
    in_ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz '
    out = 'XYZABCDEFGHIJKLMNOPQRSTUVWxyzabcdefghijklmnopqrstuvw '
    return ''.join(map(lambda x: out[in_.index(x)], plain))
```


Another example combinning **map** and **reduce** is to calculate an inner product of two vectors x, y:

```
def inner_product(a, b):
    return reduce(lambda x, y: x + y, map(lambda x, y: x * y, a, b))
```

