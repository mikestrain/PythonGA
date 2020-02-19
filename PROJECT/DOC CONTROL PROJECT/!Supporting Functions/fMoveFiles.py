
import fPrintLog as f # custom module
import shutil
import os

def fMoveFiles(u_number, pdf_and_step_list, testing_mode, print_mode, A_folders, pActive, O_folders, pObsolete, pQueue,pPrintLog):

    if print_mode: f.PrintLog('____Processing file {0}____\n'.format(u_number),pPrintLog)

    # DCA Initial
    # need to create a new number for this folder

    if u_number not in A_folders: # if it's a completely new part number
        
        if print_mode: f.PrintLog('\t{0} is a new number, and needs a new folder.'.format(u_number),pPrintLog)
        if not testing_mode: os.mkdir(pActive + '/' + u_number)
        if print_mode: f.PrintLog('\t***New directory will be created in Active files.',pPrintLog)

    # DCA ECO
    # need to move the existing document from it's active folder to obsolete
    # need to create this obsolete folder if it doesn't exist..
    # need to move the new file from the queue to the active folder

    else:

        if print_mode: f.PrintLog('\t{0} already exists in the active files.'.format(u_number),pPrintLog)

        if u_number not in O_folders: # if it doesn't yet have an obsolete folder

            if print_mode: f.PrintLog('\t{0} needs an obsolete folder.'.format(u_number),pPrintLog)
            if not testing_mode: os.mkdir(pObsolete + '/' + u_number)
            if print_mode: f.PrintLog('\t***New directory will be created in Obsolete files.',pPrintLog)
        
        # MOVE FROM ACTIVE TO OBSOLETE
        if print_mode: f.PrintLog('\tMoving the previous rev of {0} obsolete...'.format(u_number),pPrintLog)
        files_to_obsolete = os.listdir(pActive + '/' + u_number)

        for each_file in files_to_obsolete:
            if print_mode: f.PrintLog("\t\tMoving {0} from Active to Obsolete...".format(each_file),pPrintLog)
            old_path = pActive + '/' + u_number + '/' + each_file
            new_path = pObsolete + '/' + u_number + '/' + each_file.upper()
            if not testing_mode: shutil.move(old_path, new_path) # <------- actually moves the file

    # MOVE FROM QUEUE TO ACTIVE
    if print_mode: f.PrintLog('\tMoving {0} from the queue to active...'.format(u_number),pPrintLog)

    for each_file in pdf_and_step_list:
        if print_mode: f.PrintLog("\t\tMoving {0} from Queue to Active".format(each_file['name']),pPrintLog)
        old_path = pQueue + '/' + each_file['name']
        new_path = pActive + '/' + u_number + '/' + each_file['name'].upper()
        if not testing_mode: shutil.move(old_path, new_path) # <------- actually moves the file
