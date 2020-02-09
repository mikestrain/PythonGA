
#%% Imports and intro code
import os
import shutil
os.system("clear")
testing_mode = True

pDropbox = './1 DOCUMENT DROPBOX'
pQueue = './2 - DOC CONTROL QUEUE'
pActive = './3 - ACTIVE FILES'
pObsolete = './4 - OBSOLETE FILES'

Q_full_names = os.listdir(pQueue)
A_folders = os.listdir(pActive)
O_folders = os.listdir(pObsolete)

print("""
WELCOME TO THE BUSEK DOC CONTROL CLERK PROGRAM.
Written by Mike Strain on 2/2/2020.

 - Meant to check file name formatting, and move files around to appropriate folders.
 - Capitalizes files if they are in lowercase
 
""")
input('Press any key to continue...\n')

#%% Setup document names and check for bad part numbers
print("Checking all document names for bad formatting or bad part numbers.")
print("All documents should follow the format 700XXXX (X) DESCRIPTION, PART, ETC\n")
Q_doc_names = []
Q_doc_numbers = []
Q_doc_extensions = []
Q_doc_revs = []

for name in Q_full_names:

    # CHECK LOGIC FOR DOCUMENT NUMBER - IS IT 8 DIGITS? ARE THEY ALL NUMBERS?
    doc_number = name[0:8]
    doc_extension = name.split('.')[-1]

    # check that it's an integer
    try: int(doc_number)
    except: 
        print("\tThe part {0} isn't an integer. Please reformat.".format(doc_number))
        continue

    # check that the number doesn't contain a space
    if ' ' in doc_number:
        print("\tThe part number {0} contains a space, or isn't 8 digits. Please reformat.".format(doc_number))
        continue

    doc_split = name.split()

    # check that the file name is not a monolithic string
    try: doc_split[1]
    except:
        print("\tThe part {0} is one single string. Please reformat.".format(doc_number))
        continue

    # check that the second entry in doc_split contains open/closed parenthesis
    if ('(' or ')') not in doc_split[1]:
        print("\tThe part {0}'s revision is not enclosed by (). Please reformat.".format(doc_number))
        continue

    # check that the part says (1) not (REV 1)
    if 'R' in doc_split[1]:
        print('\tPlease reformat {0} as (#) instead of (REV #) or (R#).'.format(doc_number))
        continue
    
    doc_rev = doc_split[1][1:-1] #meant to remove the parenthesis from the revision
    print(doc_rev,'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    Q_doc_numbers.append(doc_number)
    Q_doc_names.append(name)
    Q_doc_extensions.append(doc_extension)
    Q_doc_revs.append(doc_rev)

print('\nAll document names checked for formatting...')
input('Press any key to continue...')

#%% Check unique document numbers
os.system('clear')
print("Checking documents for unique part numbers.")
Q_doc_numbers_unique = []
for number in Q_doc_numbers:

    # CHECK UNIQUE DOCUMENT NUMBERS - MOST DOCUMENTS ARE ARCHIVED WITH MULTIPLE FILES
    if number not in Q_doc_numbers_unique:
        Q_doc_numbers_unique.append(number)


# print(Q_doc_numbers_unique)
print('The Queue contains',len(Q_doc_numbers_unique),'unique part numbers to be processed.')
print("Finished checking documents for unique part numbers.\n\n")
input('Press any key to continue...')

# %%
os.system('clear')
print("Forming a Queue from unique part numbers, with dictionary of properties...")
Queue = {}
for u_number in Q_doc_numbers_unique:
    
    fileInfo = [] # initialize blank list for defining properties

    for i in range(len(Q_doc_numbers)):
        
        if Q_doc_numbers[i] == u_number:

            fileInfo.append({
                'number' : Q_doc_numbers[i],
                'name' : Q_doc_names[i],
                'revision' : Q_doc_revs[i],
                'extension' : Q_doc_extensions[i]
            })
    
    Queue[u_number] = fileInfo
print('Finished forming Queue.\n\n')
input('Press any key to continue...')

# %% START MOVING FILES AND CREATING FOLDERS...
os.system('clear')
print('Moving files and creating new folders.')


for u_number in Queue:

    print('____Processing file {0}____\n'.format(u_number))

  
    # DCA Initial
    # need to create a new number for this folder

    if u_number not in A_folders: # if it's a completely new part number
        
        print('\t{0} is a new number, and needs a new folder.'.format(u_number))
        if not testing_mode: os.mkdir(pActive + '/' + u_number)
        print('\t***New directory created in Active files.')

    
    # DCA ECO
    # need to move the existing document from it's active folder to obsolete
    # need to create this obsolete folder if it doesn't exist..
    # need to move the new file from the queue to the active folder

    else:

        print('\t{0} already exists in the active files.'.format(u_number))

        if u_number not in O_folders: # if it doesn't yet have an obsolete folder

            print('\t{0} needs an obsolete folder.'.format(u_number))
            if not testing_mode: os.mkdir(pObsolete + '/' + u_number)
            print('\t***New directory created in Obsolete files.')
        
        # MOVE FROM ACTIVE TO OBSOLETE
        print('\tMoving the previous rev of {0} obsolete...'.format(u_number))
        files_to_obsolete = os.listdir(pActive + '/' + u_number)

        for each_file in files_to_obsolete:
            print("\t\tMoving {0} from Active to Obsolete...".format(each_file))
            old_path = pActive + '/' + u_number + '/' + each_file
            new_path = pObsolete + '/' + u_number + '/' + each_file.upper()
            if not testing_mode: shutil.move(old_path, new_path) # <------- actually moves the file


    # MOVE FROM QUEUE TO ACTIVE
    print('\tMoving {0} from the queue to active...'.format(u_number))

    for each_file in Queue[u_number]:
        print("\t\tMoving {0} from Queue to Active".format(each_file['name']))
        old_path = pQueue + '/' + each_file['name']
        new_path = pActive + '/' + u_number + '/' + each_file['name'].upper()
        if not testing_mode: shutil.move(old_path, new_path) # <------- actually moves the file
    
    print('\n')
    input('Press a key to continue...')

print('Finished moving files and creating new folders.\n\n')
input('press any key to exit!')

# %% 

# add in functionality for the doc control log (XLSX)
# add in a cross reference for project number in PDM search?
# add in an email function
# add in a document tracking function



