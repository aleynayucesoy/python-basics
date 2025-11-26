import random

print(" --- Rastgele liste ---")
n = 10
li = random.sample(range(1,101), n)
print(li)

print("\n//////////////////\n")

print ( "min=" , min (li))
print ( "max=" , max (li))

print("\n//////////////////\n")

print("--- Çift sayıları filtreleme ---")
for j in random.sample(range(1,21), n):
    if j % 2 == 0:
        print(j)
        
print("--- Tek sayıları filtreleme ---")
for j in random.sample(range(1,21), n):
    if j % 2:
        print(j)
        
print("\n//////////////////\n")
print("--- Slicing ---")

print(li)
print("\n//////////////////\n")

print("- li[1:4] =>", li[1:4])

a = li[2:]
print("- a = li[2:] =>", a)

b = li[:3]
print("- b = li[:3] =>", b)

c = li[1:8:3]
print("- c = li[1:8:3] =>", c)

d = li[::2]
print("- d = li[::2] =>", d)

e = li[-2:]
print("- e = li[-2:] =>", e)

f = li[:-3]
print("- f = li[:-3] =>", f)

g = li[-4:-1]
print("- g = li[-4:-1] =>", g)

h = li[-8:-1:2]
print("- h = li[-8:-1:2] =>", h)

