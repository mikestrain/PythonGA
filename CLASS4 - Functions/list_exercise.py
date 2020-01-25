
import os
os.system("clear")

original_list = [10,20,30,4,5,6,7,8]

def copy_list(original_list):
    my_new_list = []
    
    for i in range(0,len(original_list)):
        # print(original_list[i])
        my_new_list.append(original_list[i]+1)
    return my_new_list

print(original_list)
print(copy_list(original_list))