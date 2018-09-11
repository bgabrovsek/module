# module
Realizes a (right) module (python 3+)
https://en.wikipedia.org/wiki/Module_(mathematics)

The set should support == and >, since terms in the module are ordered by the set element.

INPUT SAMPLE:

m1 = module(2, "c")

m1 += (-6, "x")

m2 = module(15, "a")

m3 = module(3, "x")

print(m1)

print(m1+m2+m3)

print(10*m1+m2//3-m3)



OUTPUT:

2c -6x

15a + 2c -3x

5a + 20c -63x



