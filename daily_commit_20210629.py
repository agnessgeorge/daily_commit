import math
ab = int(input())
bc = int(input())

def find_angle(ab,bc):
    ac = (ab**2 + bc**2)**0.5
    mbc = round(math.degrees(math.acos(bc/ac)))
    return mbc

a = find_angle(ab,bc)
print(str(int(a)) + u'\xb0')
