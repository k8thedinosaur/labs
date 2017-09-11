#
#
# class Foo:
#     def __init__(self, name):
#         self.name = name
#
# lst = []
#
# for i in range(100):
#     lst.append(Foo(i))
#
#
# for x in lst:
#     print(x.name)

# # comprehension
# lst = []
# for i in range(1, 21):
#     lst.append(i)
# print(lst)
#
# lst2 = [i for i in range(1, 21)]
# print(lst2)
#
# dict = {i:i+1 for i in range(1, 21)}
# print(dict)

# recursion: a function that calls itself until a condition is met
# def easy_rec(n):
#     if n > 100:
#         return n
#     else:
#         return n + easy_rec(n + 1)
#
# print(easy_rec(1))
#
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n-2) + fib(n-1)
#
# print([fib(f) for f in range(35)])

