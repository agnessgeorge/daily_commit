# okay
n = int(input("write a number \n"))
a = [b for b in range(1,n+1)]

#remove even numbers
marked_numbers = []
a = a[::2]
a[0] = 2
x = len(a)
#iterations
#index using i

i = 0
while len(marked_numbers) != x:
    temp = a[i]
    marked_numbers.append(temp)
    for aa in a[i+1:]:
        if aa%temp ==  0:
            a.remove(aa)
            marked_numbers.append(aa)
    i += 1

print(a)
print(len(a))