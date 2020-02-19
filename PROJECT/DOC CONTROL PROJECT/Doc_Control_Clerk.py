
#%% IMPORTS AND INTRO CODE
import sys
import os
from datetime import datetime

import fEdgeCases # custom module
import fSendEmail # custom module
import fPrintLog as f # custom module
import fReadWriteLog # custom module
import fMoveFiles #custom module
import fWriteRunningTotals # custom module

testing_mode = False
pDropbox = './1 DOCUMENT DROPBOX'
pQueue = './2 - DOC CONTROL QUEUE'
pActive = './3 - ACTIVE FILES'
pObsolete = './4 - OBSOLETE FILES'
pDocControlLog = './Document Number Log.xls'
pEmailList = './!Supporting Functions/Project_Email_List.txt'
pPrintLog = './!Supporting Functions/Doc_Control_Clerk_Log.txt'
pRunningProjectTotals = './!Supporting Functions/Project_Running_Totals.txt'

dt_string = datetime.now().strftime(r"%Y/%m/%d %H:%M:%S")
os.system("cls")

f.PrintLog("Today is " + dt_string,pPrintLog)
f.PrintLog("""_______________________________________________\n
WELCOME TO THE BUSEK DOC CONTROL CLERK PROGRAM.
Written by Mike Strain on 2/2/2020.
_______________________________________________

 - Meant to check file name formatting, and move files around to appropriate folders.
 - Capitalizes files if they are in lowercase
 - Reads from the doc control log to get the project number and other descriptors
 - Cross references the email list to get an appropriate email for this project PI or CogE
 - Writes back to the doc control log with the newly released parts and descriptions
 - Shuffles files around between the Queue, Active, and Obsolete
 - Keeps a running log of what's been moved for backup purposes
 - Keeps a daily running total of how many files have been processed per day per project

""",pPrintLog)

if fReadWriteLog.fDidYouCloseTheLog(pDocControlLog) != True:
    print("Please close the doc log before running this program...")
    input("Press any key to exit.")
    sys.exit()

Q_full_names = os.listdir(pQueue)
A_folders = os.listdir(pActive)
O_folders = os.listdir(pObsolete)

input('Press any key to continue...\n')

#%% SETUP DOCUMENT NAMES AND CHECK FOR BAD PART NUMBERS...

f.PrintLog("Checking all document names for bad formatting or bad part numbers.",pPrintLog)
f.PrintLog("All documents should follow the format 700XXXX (X) DESCRIPTION, PART, ETC\n",pPrintLog)

Q_doc_names = [name for name in Q_full_names if fEdgeCases.fEdgeCases(name)]    # filter the list of names that pass the fEdgeCases function with "true"
Q_doc_numbers = [name[0:8] for name in Q_doc_names]                             # extract the part numbers from the first 8 digits
Q_doc_extensions = [name.split('.')[-1] for name in Q_doc_names]                # extract the extension by separating by '.' and taking the last item in the list
Q_doc_revs = [name.split()[1][1:-1] for name in Q_doc_names]                    # split by spaces, take the second entry [1] that should be a rev with a parenthasis, and the take out the parenthasis

f.PrintLog('\nAll document names checked for formatting...',pPrintLog)
# input('Press any key to continue...')

#%% CONDENSE ALL THE UNIQUE PART NUMBERS

# os.system('cls')
f.PrintLog("Checking documents for unique part numbers.",pPrintLog)
Q_doc_numbers_unique = []
for number in Q_doc_numbers:

    # Check unique part numbers - most documents are archived in multiple formats (STEP and PDF)
    if number not in Q_doc_numbers_unique:
        Q_doc_numbers_unique.append(number)

# f.PrintLog(Q_doc_numbers_unique)
f.PrintLog('The Queue contains '+ str(len(Q_doc_numbers_unique)) + ' unique part numbers to be processed.',pPrintLog)
f.PrintLog("Finished checking documents for unique part numbers.\n\n",pPrintLog)
# input('Press any key to continue...')

# %% FORM A QUEUE FROM ALL THE UNIQUE PART NUMBERS...

# os.system('cls')
f.PrintLog("Forming a Queue from unique part numbers, with dictionary of properties...",pPrintLog)
Queue = {}
for u_number in Q_doc_numbers_unique:
    
    fileInfo = [] # initialize blank list for defining properties

    for i in range(len(Q_doc_numbers)):
        
        if Q_doc_numbers[i] == u_number:

            fileInfo.append({
                'number' : Q_doc_numbers[i],
                'name' : Q_doc_names[i],
                'description' : Q_doc_names[i].split(')')[-1].split('.')[0][1:],
                'revision' : Q_doc_revs[i],
                'extension' : Q_doc_extensions[i]
            })
    
    Queue[u_number] = fileInfo
f.PrintLog('Finished forming Queue.\n\n',pPrintLog)
input('Press any key to continue...')

# %% START MOVING FILES AND CREATING FOLDERS...

os.system('cls')
f.PrintLog("""
_______________________________________________\n
       MOVING FILES INTO DOC CONTROL....
_______________________________________________
""",pPrintLog)
f.PrintLog('Moving files and creating new folders.',pPrintLog)
items_to_skip = []

# u_number, testing_mode, print_mode, A_folders, pActive, O_folders, pObsolete
for u_number in Queue:

    # Do a dry run of the file move operation with test_mode as true, and print_mode as true.
    fMoveFiles.fMoveFiles(u_number, Queue[u_number], True, True, A_folders, pActive, O_folders, pObsolete, pQueue,pPrintLog)
    f.PrintLog('\n',pPrintLog)
    while True:
        decision = input('Press (Y) to pass this file into doc control, or (N) to reject it..')
        if decision.upper() == 'Y':
            # Actually move these files.
            fMoveFiles.fMoveFiles(u_number, Queue[u_number], False, False, A_folders, pActive, O_folders, pObsolete, pQueue,pPrintLog)
            break
        elif decision.upper() == 'N':
            f.PrintLog('The file ' + str(u_number) + ' has been skipped for processing. Moving on to the next file.',pPrintLog)
            items_to_skip.append(u_number)
            break

#Remove items from the queue that have been skipped:
for item in items_to_skip:
    Queue.pop(item,None) # remove this entry from the queue entirely

f.PrintLog('Finished moving files and creating new folders.\n\n',pPrintLog)
input('Press a key to continue...')



# %% LOOKUP EACH UNIQUE PART IN THE DOC CONTROL LOG, AND RETAIN THAT DATA.
Email_Dict = fSendEmail.fBuildEmailList(pEmailList) # build the list of emails for each project
Email_List = [] #start a blank list for unique emails
os.system("cls")
f.PrintLog("""
_______________________________________________\n
      READING AND WRITING DOC CONTROL LOG
                    & 
         SENDING NOTIFICATION EMAILS
_______________________________________________
""",pPrintLog)

for u_number in Queue:
    f.PrintLog('\t\tLooking up P/N ' + u_number + ' in Doc Control Log. Please wait.',pPrintLog)

    log_doc_description, log_doc_type, log_doc_project, log_doc_user = fReadWriteLog.fReadLog(int(u_number),pDocControlLog)
    f.PrintLog('\t\tFound ' + u_number + ' in Doc Control Log. Writing info.\n',pPrintLog)
    
    try: int(log_doc_project)
    except: log_doc_project = 0

    log_dict = {
        'doc_description' : log_doc_description,
        'doc_type' : log_doc_type,
        'doc_project' : str(int(log_doc_project)),
        'doc_user' : log_doc_user,
        'doc_email' : fSendEmail.fRetrieveEmail(str(int(log_doc_project)),Email_Dict)
    }

    Queue[u_number].append(log_dict)
    
    for address in log_dict['doc_email']:
        if address not in Email_List:
            Email_List.append(address)
    
    
# %% WRITE THE DOC CONTROL LOG WITH THE NEW REVISIONS AND DESCRIPTIONS FOR EACH PART...
f.PrintLog('Writing file info to doc control log...\n',pPrintLog)
if not testing_mode: fReadWriteLog.fWriteLog(Queue,pDocControlLog)
f.PrintLog('All set!\n',pPrintLog)

# write the running totals for each project to this log for today, for future use...
fWriteRunningTotals.fWriteRunningTotals(Queue,pRunningProjectTotals)

# %% SEND AN EMAIL TO INFORM EACH PERSON THEIR DOCUMENTS HAVE BEEN RELEASED...
# os.system('cls')
f.PrintLog('Sending emails to notify each person of the REV change...',pPrintLog)

for address in Email_List:
    if address != '':
        f.PrintLog('\t\tSending an email to ' + address + '...',pPrintLog)
        notification_files = []

        for u_number in Queue:
            if address in Queue[u_number][-1]['doc_email']: 
                notification_files.append(u_number + '        ' + Queue[u_number][0]['description'])

        message = """<p>Hello,<br>
                This message is to inform you that the following files have been released on the doc control server:<br><br>
                """ + '<br>'.join(notification_files) + """<br><br>
                This is an automated message.<br>
                <br>
                Thank you,<br>
                Doc Control Robot</p>"""

        if not testing_mode: fSendEmail.fSendEmail(address,message)

f.PrintLog('Finished Sending Emails....\n\n',pPrintLog)
input('press any key to exit!')


# %%
