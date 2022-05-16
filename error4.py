a = (0)

b = (1)

numbers = []

try:
    while b > a:
        numbers += b
except TypeError:
    b += 1
except TypeError:
    print(b)

