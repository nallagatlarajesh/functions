#the power of lambda is better shown when you use 
#them as an anonymous function inside another function.

#using lambda function in oprogram
def fun(n):
    return lambda a: a*n
a=fun(2)
b=fun(3)
print(a(10))
print(b(12))
