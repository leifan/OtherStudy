import os

d = [d for d in os.listdir()]

print(d)

for i,v in enumerate(d):
    print(i, '----', v)

dd = ["[" + str(i+1) + "]" + v for i,v in enumerate(d)]
print(dd)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print(L2)

#生成器
g = (x * x for x in range(10))
print(g)
print(next(g))
print(next(g))

for i in g:
    print(i)


