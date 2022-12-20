# import timeit
#
# def a():
#     A = [1, 10, 5, 4, 4, 3, 8]
#     b = sorted(A)
#     return b
#
# def b():
#     A = [1, 10, 5, 4, 4, 3, 8]
#     count_A = max(A) + 1
#     B = [0] * count_A
#     for i in A:
#         B[i] += 1
#     A = []
#     for i in range(count_A):
#         A += [i] * B[i]
#     return A
#
# print(timeit.timeit(b, number=10000))
# print(timeit.timeit(a, number=10000))
#
#



