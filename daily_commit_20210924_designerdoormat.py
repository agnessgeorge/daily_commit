# Enter your code here. Read input from STDIN. Print output to STDOUT
# Mat size must be X. ( is an odd natural number, and  is  times .)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.

n,m  = input().split()
welcome = "WELCOME"
pattern = '.|.'
for x in range(int(n)):
    if x%2 == 1:
        xx = pattern*x
        print(xx.center(int(m),'-'))
    else:
        pass
print(welcome.center(int(m),'-'))
rvs = []
for r in range(int(n)):
    if r%2 == 1:
        rvs.append(r)
    else:
        pass

rvs_2 = list(reversed(rvs))
for x in rvs_2:
    if x%2 == 1:
        xx = pattern*x
        print(xx.center(int(m),'-'))
    else:
        pass
