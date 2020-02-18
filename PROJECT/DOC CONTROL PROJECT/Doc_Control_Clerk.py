
#%% IMPORTS AND INTRO CODE
import sys
import os
import shutil
from datetime import datetime

import fEdgeCases # custom module
import fSendEmail # custom module
import fPrintLog as f # custom module
import fReadWriteLog # custom module

dt_string = datetime.now().strftime(r"%Y/%m/%d %H:%M:%S")
os.system("cls")
testing_mode = True

f.PrintLog("Today is " + dt_string)
f.PrintLog("""_______________________________________________\n
WELCOME TO THE BUSEK DOC CONTROL CLERK PROGRAM.
Written by Mike Strain on 2/2/2020.
_______________________________________________

 - Meant to check file name formatting, and move files around to appropriate folders.
 - Capitalizes files if they are in lowercase
""")

pDropbox = './1 DOCUMENT DROPBOX'
pQueue = './2 - DOC CONTROL QUEUE'
pActive = './3 - ACTIVE FILES'
pObsolete = './4 - OBSOLETE FILES'
pDocControlLog = './Document Number Log 20200221.xls'
pEmailList = './Project_Email_List.txt'

if fReadWriteLog.fDidYouCloseTheLog(pDocControlLog) != True:
    print("Please close the doc log before running this program...")
    input("Press any key to exit.")
    sys.exit()

Q_full_names = os.listdir(pQueue)
A_folders = os.listdir(pActive)
O_folders = os.listdir(pObsolete)



input('Press any key to continue...\n')

#%% SETUP DOCUMENT NAMES AND CHECK FOR BAD PART NUMBERS...

f.PrintLog("Checking all document names for bad formatting or bad part numbers.")
f.PrintLog("All documents should follow the format 700XXXX (X) DESCRIPTION, PART, ETC\n")

Q_doc_names = [name for name in Q_full_names if fEdgeCases.fEdgeCases(name)]    # filter the list of names that pass the fEdgeCases function with "true"
Q_doc_numbers = [name[0:8] for name in Q_doc_names]                             # extract the part numbers from the first 8 digits
Q_doc_extensions = [name.split('.')[-1] for name in Q_doc_names]                # extract the extension by separating by '.' and taking the last item in the list
Q_doc_revs = [name.split()[1][1:-1] for name in Q_doc_names]                    # split by spaces, take the second entry [1] that should be a rev with a parenthasis, and the take out the parenthasis

f.PrintLog('\nAll document names checked for formatting...')
input('Press any key to continue...')

#%% CONDENSE ALL THE UNIQUE PART NUMBERS

os.system('cls')
f.PrintLog("Checking documents for unique part numbers.")
Q_doc_numbers_unique = []
for number in Q_doc_numbers:

    # Check unique part numbers - most documents are archived in multiple formats (STEP and PDF)
    if number not in Q_doc_numbers_unique:
        Q_doc_numbers_unique.append(number)

# f.PrintLog(Q_doc_numbers_unique)
f.PrintLog('The Queue contains '+ str(len(Q_doc_numbers_unique)) + ' unique part numbers to be processed.')
f.PrintLog("Finished checking documents for unique part numbers.\n\n")
input('Press any key to continue...')

# %% FORM A QUEUE FROM ALL THE UNIQUE PART NUMBERS...

# os.system('cls')
print("Forming a Queue from unique part numbers, with dictionary of properties...")
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
f.PrintLog('Finished forming Queue.\n\n')
input('Press any key to continue...')

# %% START MOVING FILES AND CREATING FOLDERS...

os.system('cls')
f.PrintLog("""
_______________________________________________\n
       MOVING FILES INTO DOC CONTROL....
_______________________________________________
""")
f.PrintLog('Moving files and creating new folders.')


for u_number in Queue:

    f.PrintLog('____Processing file {0}____\n'.format(u_number))
  
    # DCA Initial
    # need to create a new number for this folder

    if u_number not in A_folders: # if it's a completely new part number
        
        f.PrintLog('\t{0} is a new number, and needs a new folder.'.format(u_number))
        if not testing_mode: os.mkdir(pActive + '/' + u_number)
        f.PrintLog('\t***New directory created in Active files.')
    
    # DCA ECO
    # need to move the existing document from it's active folder to obsolete
    # need to create this obsolete folder if it doesn't exist..
    # need to move the new file from the queue to the active folder

    else:

        f.PrintLog('\t{0} already exists in the active files.'.format(u_number))

        if u_number not in O_folders: # if it doesn't yet have an obsolete folder

            f.PrintLog('\t{0} needs an obsolete folder.'.format(u_number))
            if not testing_mode: os.mkdir(pObsolete + '/' + u_number)
            f.PrintLog('\t***New directory created in Obsolete files.')
        
        # MOVE FROM ACTIVE TO OBSOLETE
        f.PrintLog('\tMoving the previous rev of {0} obsolete...'.format(u_number))
        files_to_obsolete = os.listdir(pActive + '/' + u_number)

        for each_file in files_to_obsolete:
            f.PrintLog("\t\tMoving {0} from Active to Obsolete...".format(each_file))
            old_path = pActive + '/' + u_number + '/' + each_file
            new_path = pObsolete + '/' + u_number + '/' + each_file.upper()
            if not testing_mode: shutil.move(old_path, new_path) # <------- actually moves the file


    # MOVE FROM QUEUE TO ACTIVE
    f.PrintLog('\tMoving {0} from the queue to active...'.format(u_number))

    for each_file in Queue[u_number]:
        f.PrintLog("\t\tMoving {0} from Queue to Active".format(each_file['name']))
        old_path = pQueue + '/' + each_file['name']
        new_path = pActive + '/' + u_number + '/' + each_file['name'].upper()
        if not testing_mode: shutil.move(old_path, new_path) # <------- actually moves the file
    
    f.PrintLog('\n')
    input('Press a key to continue...')

f.PrintLog('Finished moving files and creating new folders.\n\n')
input('Press a key to continue...')


# %% LOOKUP EACH UNIQUE PART IN THE DOC CONTROL LOG, AND RETAIN THAT DATA.
Email_Dict = fSendEmail.fBuildEmailList(pEmailList) # build the list of emails for each project
Email_List = [] #start a blank list for unique emails

for u_number in Queue:
    f.PrintLog('\t\tLooking up P/N ' + u_number + ' in Doc Control Log. Please wait.')

    log_doc_description, log_doc_type, log_doc_project, log_doc_user = fReadWriteLog.fReadLog(int(u_number),pDocControlLog)
    f.PrintLog('\t\tFound ' + u_number + ' in Doc Control Log. Writing info.\n')
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
f.PrintLog('Writing file info to doc control log...\n')
if not testing_mode: fReadWriteLog.fWriteLog(Queue,pDocControlLog)
f.PrintLog('All set!\n')

# %% SEND AN EMAIL TO INFORM EACH PERSON THEIR DOCUMENTS HAVE BEEN RELEASED...
os.system('cls')
f.PrintLog('Sending emails to notify each person of the REV change...')

for address in Email_List:
    if address != '':
        f.PrintLog('\t\tSending an email to ' + address + '...')
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

f.PrintLog('Finished Sending Emails....\n\n')
input('press any key to exit!')
