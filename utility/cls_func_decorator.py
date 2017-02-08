# sklearn has a decorator class to throw deprecation warnings. It can be applied to both classes and functions

from sklearn.utils import deprecated


@deprecated()
def func_1():
    print('Function 1 is called.')

func_1()


@deprecated('Extra msg added')
def func_2():
    print('Function 2 is called.')

func_2()


@deprecated('Cls extra msg added.')
class A:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

A(1, 2, 3)


# __call__ magic method
# if define __call__ method in a class, it looks like we add a () operator to this class

class B:
    def __init__(self):
        self.list = []

    def __call__(self, good):
        print('Adding {}'.format(good))
        self.list.append(good)


b = B()
b('Beef')
b('Chicken')
print(b.list)


# How class decorator works
class ClassDecorator:
    def __init__(self, x):
        self.x = x

    def __call__(self, cls):
        print('Decorator is called.')
        # save class's original __init__
        init = cls.__init__

        def wrapped(*args, **kwargs):
            print('Class {} is decorated'.format(cls.__name__))
            return init(*args, **kwargs)
        cls.__init__ = wrapped
        wrapped.__name__ = '__init__'

        # just for fun
        cls.what_is_this = self.x
        return cls


@ClassDecorator('ghost')
class C:
    def __init__(self, output):
        print(output)

C('Hello machine learning')
