import functools

class memoized(object):
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned
    (not reevaluated).
    '''
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value
    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__
    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)

@memoized
def fibonacci(n):
    "Return the nth fibonacci number."
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

@memoized
def fact(n):
    if n in (0, 1):
        return 1
    return n * fact(n - 1) 
if __name__ == '__main__':
    n = 1000
    for i in range(n):
        fibonacci(i)
    print(fibonacci(n))
    print()
    for i in range(n):
        fact(i)
    print(fact(n))
