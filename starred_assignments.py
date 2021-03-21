import timeit


def test1():
    ls = list(range(1_000_000))
    _, end = ls[:-1:], ls[-1]
    return end


def test2():
    ls = list(range(1_000_000))
    *_, end = ls
    return end


ti1 = timeit.timeit("test1()", setup="from __main__ import test1", number=100)
ti2 = timeit.timeit("test2()", setup="from __main__ import test2", number=100)
print(ti1)
print(ti2)
