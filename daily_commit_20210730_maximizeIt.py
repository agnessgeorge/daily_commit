from itertools import product
K, M = map(int,raw_input().split())
def Sq(n):
    return int(n)**2
List = []
for i in range(K):
    List.append(list(map(Sq,raw_input().split()[1:])))
print(List)
Max=0    
print([product(*List)])
for T in product(*List):
    Sum=sum(T)%M
    print(Sum)
    if Sum>Max:   #finding maximum sum out of all tuples
        Max=Sum
print(Max)