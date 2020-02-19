# %%
from xlrd import open_workbook
from xlutils.copy import copy
from datetime import datetime
import fReadWriteLog
import sys
import pyperclip

loc = './Document Number Log.xls'

print("""_______________________________\n
 AUTOMATED PART REQUEST SYSTEM
Written by M. Strain on 2/19/20
_______________________________\n
please wait...
""")

print("What is the job number?")
print('\tPlease input a 4 digit number.')
print('\tTypical example: 1360')
print('\tIRAD example: 0464.')
print('\tProposal example 6342')
print('\tFacilities example: 0002')
print('\tNot applicable, or no project: 0000\n')

while True:
    job_number = input(">>>")
    if len(job_number) == 4:
        try: 
            int(job_number)
            break
        except:
            print('please enter a valid number.')
    else:
        print('please enter a valid number.')

print('\n\nWhat is your name? Please enter first initial, last name.')
print('\tExample: J. ONeil')
print('\tExample: M. Strain\n')
requestor = input(">>>")

temp_description = 'RESERVED FOR ' + requestor.upper()
date_assigned = datetime.now().strftime(r"%Y/%m/%d")

with open_workbook(loc,formatting_info=True,on_demand=True) as wb:
    
    sheet = wb.sheet_by_index(0)
    last_number = sheet.cell_value(sheet.nrows-1,0)
    new_number = last_number + 1

    wb2 = copy(wb)
    sheet2 = wb2.get_sheet(0)

    sheet2.write(sheet.nrows,0,int(new_number))
    sheet2.write(sheet.nrows,1,temp_description)
    # col 2 is document type
    sheet2.write(sheet.nrows,3,job_number)
    # col 4 is keywords
    sheet2.write(sheet.nrows,5,requestor.upper())
    sheet2.write(sheet.nrows,6,date_assigned)

try: 
    wb2.save(loc)
    print("\nYour part number is {0}.\n".format(int(new_number)))
    pyperclip.copy(str(int(new_number)))
    print('Your part number has been copied to the clipboard.')

except PermissionError:
    print("Can't give you a part number, the log is already open. Contact the system admin to resolve this problem.")
    

input('Press any key to exit...')
