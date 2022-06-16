Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def f(n):
    a, b, c=0, 1, 2
    if n>=3:
        while n>=3:
            a, b, c=b, c, c+a+b
            n-=1
        return c
    else:
        return n

    
def f(n, a=0, b=1, c=2):
    if n in(0, 1, 2):
        return n
    else:
        return f(n-3, b, c, a+b+c)+f(n-2, b, c, a+b+c)+f(n-1, b, c, a+b+c)


def f(n):
    if n in (0, 1, 2, 3):
        return n
    return f(n-1)+f(n-2)+f(n-3)

def pascal(n, m):
    if n==1 or n==m or n==2:
        return 1
    else:
        return pascal(n-1, m-1)+pascal(n-1, m)

    
def fast_pow(m, n):
    res=1
    if n==0:
        return 1
    if is_even(n):
        while n/2>0:
            res*=m
            n-=1
        return  res
    else:
        while n>0:
            res*=m
            n-=1
        return res

    
def is_even(n):
    if n%2==0:
        return True
    return False

def contain(data, val):
    i=0
    _count=0
    while i<len(data):
        if data[i]==val:
            _count+=1
        i+=1
    if _count==0:
        return False
    return True

def remave_all(data, value):
    i=0
    while i<len(data):
        if data[i]==value or data[len(data)-1]==value:
            data.remove(value)
        i+=1
    return data

def reserve(data):
    data1=data[::-1]
    print(data1)

    
def min(data):
    i=0
    _min=data[0]
    while i<len(data):
        if data[i]<_min:
            _min=data[i]
        i+=1
    return _min

def max(data):
    i=0
    _max=data[0]
    while i<len(data):
        if data[i]>_max:
            _max=data[i]
        i+=1
    return _max