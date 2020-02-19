
def PrintLog(str_in,pPrintLog):

    print(str_in)

    with open(pPrintLog, "a") as my_file:
        my_str = str_in + "\n"
        my_file.writelines(my_str)