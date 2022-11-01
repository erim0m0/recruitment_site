import timeit

def a():
    a = ["ali", "amir"]
    if all(i in a for i in ("amir", "fateme")):
        print("yes")

def b():
    a = ["ali", "amir"]
    if "amir" in a and "fateme" in a:
        print("yes")

print(timeit.timeit(b, number=10000))
print(timeit.timeit(a, number=10000))


