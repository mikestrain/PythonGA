# %%
from xlrd import open_workbook
from xlutils.copy import copy
from datetime import datetime

def fReadLog(number_to_search,loc):
    #open doc control log
    #read the right file name
    #format it in the correct way

    with open_workbook(loc) as wb:
        sheet = wb.sheet_by_index(0)
        # print(sheet.nrows)

        doc_names = []

        for i in range(1,sheet.nrows):
            try: 
                doc_name = int(sheet.cell_value(i,0))
                doc_names.append(doc_name)
            except: 
                print(type(sheet.cell_value(i,0)))
                print(i)
                print('Found an error in doc control log, please check for blanks or non-integers in number list.')
            

        try:
            number_index = doc_names.index(number_to_search)
            
            excel_index = number_index + 1 #excel starts from base 1, and also starts on the 2nd row
            log_doc_description = sheet.cell_value(excel_index,1)
            log_doc_type = sheet.cell_value(excel_index,2)
            log_doc_project = sheet.cell_value(excel_index,3)
            log_doc_user = sheet.cell_value(excel_index,5)

        except:
            print('Could not find part number in doc control log. Might be a facilities part.')
            log_doc_description = ''
            log_doc_type = ''
            log_doc_project = ''
            log_doc_user = ''
            log_doc_email = ''

    # print(log_doc_description)
    # print(log_doc_type)
    # print(log_doc_email)
    # print(log_doc_user)
    # print('Column index in excel is',excel_index)

    return log_doc_description, log_doc_type, log_doc_project, log_doc_user


def fWriteLog(Queue, loc):

    with open_workbook(loc,formatting_info=True,on_demand=True) as wb:
        
        doc_names = []
        sheet = wb.sheet_by_index(0)

        for i in range(1,sheet.nrows):
                    try: 
                        doc_name = int(sheet.cell_value(i,0))
                        doc_names.append(doc_name)
                    except: 
                        print(type(sheet.cell_value(i,0)))
                        print(i)
                        print('Found an error in doc control log, please check for blanks or non-integers in number list.')
                
        wb2 = copy(wb)
        sheet2 = wb2.get_sheet(0)

        for u_number in Queue:

                    try:
                        number_index = doc_names.index(int(u_number))
                        excel_index = number_index + 1 #excel starts from base 1, and also starts on the 2nd row
                        print("\t\tWriting P/N",u_number,"to the log...")
                        sheet2.write(excel_index,1,Queue[u_number][0]['description'])
                        sheet2.write(excel_index,8,Queue[u_number][0]['revision'])
                        sheet2.write(excel_index,9,datetime.now().strftime(r"%Y/%m/%d"))

                    except:
                        print('Could not find part number in doc control log. Might be a facilities part.')

    wb2.save(loc)

def fDidYouCloseTheLog(loc):
    # function that checks if the log is open
    with open_workbook(loc,formatting_info=True,on_demand=True) as wb:
        wb2 = copy(wb)
    
    try: 
        wb2.save(loc)
        return True
    except PermissionError:
        return False

# loc = '.\Document Number Log 20200221.xls'


# Queue = {'70019590': [{'number': '70019590',
#    'name': '70019590 (1) TEST PART #1.pdf',
#    'description': 'TEST PART #1',
#    'revision': '1',
#    'extension': 'pdf'},
#   {'number': '70019590',
#    'name': '70019590 (1) TEST PART #1.STEP',
#    'description': 'TEST PART #1',
#    'revision': '1',
#    'extension': 'STEP'}],
#  '70019591': [{'number': '70019591',
#    'name': '70019591 (1) TEST PART #2.pdf',
#    'description': 'TEST PART #2',
#    'revision': '1',
#    'extension': 'pdf'},
#   {'number': '70019591',
#    'name': '70019591 (1) TEST PART #2.STEP',
#    'description': 'TEST PART #2',
#    'revision': '1',
#    'extension': 'STEP'}],
#  '70019592': [{'number': '70019592',
#    'name': '70019592 (1) TEST PART #3.pdf',
#    'description': 'TEST PART #3',
#    'revision': '1',
#    'extension': 'pdf'},
#   {'number': '70019592',
#    'name': '70019592 (1) TEST PART #3.STEP',
#    'description': 'TEST PART #3',
#    'revision': '1',
#    'extension': 'STEP'}],
#  '70019596': [{'number': '70019596',
#    'name': '70019596 (1) TEST PART #7.pdf',
#    'description': 'TEST PART #7',
#    'revision': '1',
#    'extension': 'pdf'},
#   {'number': '70019596',
#    'name': '70019596 (1) TEST PART #7.STEP',
#    'description': 'TEST PART #7',
#    'revision': '1',
#    'extension': 'STEP'}],
#  '70019597': [{'number': '70019597',
#    'name': '70019597 (1) TEST PART #8.pdf',
#    'description': 'TEST PART #8',
#    'revision': '1',
#    'extension': 'pdf'},
#   {'number': '70019597',
#    'name': '70019597 (1) TEST PART #8.STEP',
#    'description': 'TEST PART #8',
#    'revision': '1',
#    'extension': 'STEP'}]}

# fWriteLog(Queue,loc)

