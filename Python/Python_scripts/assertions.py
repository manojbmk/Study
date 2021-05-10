x = 10

try:
    assert x<10
except AssertionError:
    print("something is faulty")

print(x)