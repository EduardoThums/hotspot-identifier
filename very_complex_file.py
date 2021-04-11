class A(object):
    def meth(self):
        return sum(i for i in range(10) if i - 2 < 5)

def fib(n):
    if n < 2: return 1
    return fib(n - 1) + fib(n - 2)