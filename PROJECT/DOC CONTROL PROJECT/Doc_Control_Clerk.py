
#%% Imports and intro code
import os
import shutil
os.system("clear")
print("\n\n\n\n\n\n")

pDropbox = './1 DOCUMENT DROPBOX'
pQueue = './2 - DOC CONTROL QUEUE'
pActive = './3 - ACTIVE FILES'
pObsolete = './4 - OBSOLETE FILES'

Q_full_names = os.listdir(pQueue)
A_folders = os.listdir(pActive)
O_folders = os.listdir(pObsolete)

#%% Setup document names and check for bad part numbers
Q_doc_names = []
Q_doc_numbers = []
Q_doc_extensions = []

for name in Q_full_names:

    # CHECK LOGIC FOR DOCUMENT NUMBER - IS IT 8 DIGITS? ARE THEY ALL NUMBERS?
    doc_number = name[0:8]
    doc_extension = name.split('.')[-1]
    try: int(doc_number)
    except: 
        print("This part {0} isn't named correctly!".format(doc_number))
        continue

    if ' ' in doc_number:
        print("This part number {0} contains a space, or isn't 8 digits.".format(doc_number))
        continue

    Q_doc_numbers.append(doc_number)
    Q_doc_names.append(name)
    Q_doc_extensions.append(doc_extension)

#%% Check unique document numbers

Q_doc_numbers_unique = []
for number in Q_doc_numbers:

    # CHECK UNIQUE DOCUMENT NUMBERS - MOST DOCUMENTS ARE ARCHIVED WITH MULTIPLE FILES
    if number not in Q_doc_numbers_unique:
        Q_doc_numbers_unique.append(number)


print(Q_doc_numbers_unique)
print(len(Q_doc_numbers_unique))

# %%

Queue = {}
for u_number in Q_doc_numbers_unique:
    
    fileInfo = [] # initialize blank list for defining properties

    for i in range(len(Q_doc_numbers)):
        
        if Q_doc_numbers[i] == u_number:

            fileInfo.append({
                'number' : Q_doc_numbers[i],
                'name' : Q_doc_names[i],
                'extension' : Q_doc_extensions[i]
            })
    
    Queue[u_number] = fileInfo

# %% START MOVING FILES AND CREATING FOLDERS...

for u_number in Queue:

    print('____Processing file {0}____\n'.format(u_number))

  
    # DCA Initial
    # need to create a new number for this folder

    if u_number not in A_folders: # if it's a completely new part number
        
        print('\t{0} is a new number, and needs a new folder.'.format(u_number))
        os.mkdir(pActive + '/' + u_number)
        print('\t***New directory created in Active files.')

    
    # DCA ECO
    # need to move the existing document from it's active folder to obsolete
    # need to create this obsolete folder if it doesn't exist..
    # need to move the new file from the queue to the active folder

    else:

        print('\t{0} already exists in the active files.'.format(u_number))

        if u_number not in O_folders: # if it doesn't yet have an obsolete folder

            print('\t{0} needs an obsolete folder.'.format(u_number))
            os.mkdir(pObsolete + '/' + u_number)
            print('\t***New directory created in Obsolete files.')
        
        # MOVE FROM ACTIVE TO OBSOLETE
        print('\tMoving the previous rev of {0} obsolete...'.format(u_number))
        files_to_obsolete = os.listdir(pActive + '/' + u_number)

        for each_file in files_to_obsolete:
            print("\t\tMoving {0} to Obsolete...".format(each_file))
            old_path = pActive + '/' + u_number + '/' + each_file
            new_path = pObsolete + '/' + u_number + '/' + each_file
            shutil.move(old_path, new_path) # <------- actually moves the file


    # MOVE FROM QUEUE TO ACTIVE
    print('\tMoving {0} from the queue to active...'.format(u_number))

    for each_file in Queue[u_number]:
        print("\t\tThe name of this file is {0}".format(each_file['name']))
        old_path = pQueue + '/' + each_file['name']
        new_path = pActive + '/' + each_file['name']
        shutil.move(old_path, new_path) # <------- actually moves the file
    
    print('\n')

# %% 

# add in functionality for the doc control log (XLSX)
# add in a cross reference for project number in PDM search?
# add in an email function
# add in a document tracking function

