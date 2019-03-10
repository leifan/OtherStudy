import time

time.clock()

sum = 0
# for i in range(100000000):
#     sum += i
i = 0
while i<100000000:
    i += 1
    sum += i

print(time.clock())

