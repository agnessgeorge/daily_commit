s = raw_input("enter a string")
lwr = ''
upp = ''
evn = ''
odd = ''
sorted_lower = ''
sorted_upper = ''
sorted_even = ''
sorted_odd = ''
new_s_sorted = ''
for t in s:
    if t.islower() == True:
        lwr += t
sorted_lower = sorted(lwr) 
sorted_lower_string = ''.join(sorted_lower) 
new_s_sorted += sorted_lower_string

for t in s:
    if t.isupper() == True:
        upp += t
sorted_upper = sorted(upp) 
sorted_upper_string = ''.join(sorted_upper) 
new_s_sorted += sorted_upper_string
for t in s:
    if t.isdigit() == True and ((int(t))%2) != 0:
        odd += t
sorted_odd = sorted(odd) 
sorted_odd_string = ''.join(sorted_odd) 
new_s_sorted += sorted_odd_string    
for t in s:
    if t.isdigit() == True and ((int(t))%2) == 0:
        evn += t
sorted_even = sorted(evn) 
sorted_even_string = ''.join(sorted_even) 
new_s_sorted += sorted_even_string    
print(new_s_sorted)