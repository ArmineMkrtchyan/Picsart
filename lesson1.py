Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def pow(m):
    n=1
    while not guess_enough(n, m):
        n=improve(n, m)
    return n

def guess_enough(value , target):
    if abs(value**3-target)<0.0001:
        return True
    else:
        return False

    
def improve(root, target):
    return ((target/(root**2))+(2*root))/3

pow(8)
2.000004911675504
pow(-8)
-2.0
pow(64)
4.000000000076121