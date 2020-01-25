import os
os.system("clear")

def sum_everything(*args):
    if type(args[0]) == int or type(args[0]) == float:
        final_sum = 0
    else:
        final_sum = ''

    for number in args:
        final_sum = final_sum + number
    
    return final_sum

print(sum_everything(1.125, 2, 3, 4, 5, 6, 7, 8, 9))
print(sum_everything())