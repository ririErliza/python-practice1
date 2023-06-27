items=[0,1,2,3,4,5]
print(items)
# [0, 1, 2, 3, 4, 5]



# for n in range(6):
#     print(n)

# 0
# 1
# 2
# 3
# 4
# 5

print('--------------------------')

for n in range(3,10):
    print(n)

# 3
# 4
# 5
# 6
# 7
# 8
# 9

print('--------------------------')


for m in range(0,20,4):
    print(m)

# 0
# 4
# 8
# 12
# 16

print('--------------------------')


burgers = ['beef','chicken', 'veg', 'supreme', 'double']

for b in range(len(burgers)):
    print(b, burgers[b])

# 0 beef
# 1 chicken
# 2 veg
# 3 supreme
# 4 double

print('--------------------------')

# going from backward

for b in range(len(burgers)-1,-1,-1):
    print(b, burgers[b])

# 4 double
# 3 supreme
# 2 veg
# 1 chicken
# 0 beef

print('--------------------------')

for b in range(-1,-1,-1):
    print(b, burgers[b])

# this give the same result as above
# 4 double
# 3 supreme
# 2 veg
# 1 chicken
# 0 beef

