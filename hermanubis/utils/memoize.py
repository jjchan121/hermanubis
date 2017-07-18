from functools import partial

"""
http://code.activestate.com/recipes/577452-a-memoize-decorator-for-instance-methods/
"""

class memoize(object):
    """cache the return value of a method

    This class is meant to be used as a decorator of methods. The return value
    from a given method invocation will be cached on the instance whose method
    was invoked. All arguments passed to a method decorated with memoize must
    be hashable.

    If a memoized method is invoked directly on its class the result will not
    be cached. Instead the method will be invoked like a static method:
    class Obj(object):
        @memoize
        def add_to(self, arg):
            return self + arg
    Obj.add_to(1) # not enough arguments
    Obj.add_to(1, 2) # returns 3, result is not cached
    """
    def __init__(self, func):
        self.func = func
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self.func
        return partial(self, obj)
    def __call__(self, *args, **kw):
        obj = args[0]
        try:
            cache = obj.__cache
        except AttributeError:
            cache = obj.__cache = {}
        key = (self.func, args[1:], frozenset(kw.items()))
        try:
            res = cache[key]
        except KeyError:
            res = cache[key] = self.func(*args, **kw)
        return res


    # class Test(object):
    #     v = 0
    #     @memoize
    #     def inc_add(self, arg):
    #         self.v += 1
    #         return self.v + arg
    #
    # t = Test()
    # assert t.inc_add(2) == t.inc_add(2)
    # assert Test.inc_add(t, 2) != Test.inc_add(t, 2)


class Foo(object):
    def __init__(self, a):
        self.a = a

    @memoize
    def evaluate(self, b):
        print("do the calculation")
        return self.a * b


#
# @memoize
# def foo(a, b):
#     return a * b


foo = Foo(10.0)

print (foo.evaluate(5.0))
print (foo.evaluate(5.0))
