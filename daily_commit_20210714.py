c = raw_input().split()
a = int(c[0])
b = int(c[1])

d = []
for bb in range(b):
    i = raw_input().split()
    aaa = []
    for j in i:
        aaa.append(j)
    d.append(aaa)
sum = 0
sums = []

for x in range(a): #3
    for y in range(b): #5

        sum += float(d[y][x])
    sums.append(float(sum/b))
    sum = 0


for z in sums:

    print("{:.1f}".format(z))