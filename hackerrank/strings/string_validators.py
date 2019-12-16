input_str = input()
all_num = False
all_alpha = False
all_digits = False
all_lower = False
all_upper = False
for i in input_str:
    if(i.isalnum()):
        all_num = True
    if(i.isalpha()):
        all_alpha = True
    if(i.isdigit()):
        all_digits = True
    if(i.islower()):
        all_lower = True
    if(i.isupper()):
        all_upper = True

print(all_num)
print(all_alpha)
print(all_digits)
print(all_lower)
print(all_upper)
