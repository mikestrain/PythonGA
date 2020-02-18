
def PrintLog(str_in):

    print(str_in)

    with open("Doc_Control_Clerk_Log.txt", "a") as my_file:
        my_str = str_in + "\n"
        my_file.writelines(my_str)