result = None
try:
    a = float(input("Enter number 1:"))
    b = float(input("Enter number 2:"))

    result = a/b
except ZeroDivisionError as e:
    print("Zero Division Error")
except Exception as b:
    print("Other exception catched ",type(b))
else:
    print("__else__")
finally:
    print("__finally__")
print("Result = ", result)
print("END")