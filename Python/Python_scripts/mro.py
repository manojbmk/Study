class A:
    def func(self):
        def_value="A"
        return def_value

class B(A):
    def func(self):
        def_value="B"
        return def_value


class C(A,B):
    def func(self):
        def_value="C"
        return def_value

cat = C()
print(cat.func())

print(C.__mro__)