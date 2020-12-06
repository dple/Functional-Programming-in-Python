# Functional Programming in Python

In the following we examine high order functions in Python.

## reduce()

Function **reduce**(function, seq) is introduced in the package functools. This function will apply a particular *function* (1st argument) to all elements mentioned in the sequence *seq*. 

Consider the following example. Let *a<sub>0</sub>, a<sub>1</sub>, ..., a<sub>n - 1</sub>* be integers. Find **Greatest Common Divisor**, *gcd* of those numbers. One method for this problem is to find *gcd(a<sub>0</sub>, a<sub>1</sub>)*, then *gcd(gcd(a<sub>0</sub>, a<sub>1</sub>), a<sub>2</sub>)*, and so on. This will be implemented as follows:


```
def gcd(a, b):
  while b:
    a, b = b, a % b
  return a

def multiple_gcd(a):     # a is an array
  n = len(a)
  c = gcd(a[0], a[1])
  for i in range(2, n):
    c = gcd(c, a[i])
  return c
```

By using function **reduce**, code can be simplified as follows:

```
def multiple_gcd(a):
  return reduce(gcd, a) 
```
