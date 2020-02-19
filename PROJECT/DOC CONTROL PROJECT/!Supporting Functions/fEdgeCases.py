
def fEdgeCases(name):

    accept_file = True # start by accepting all files, and change this value if it fails the criteria below

        # CHECK LOGIC FOR DOCUMENT NUMBER - IS IT 8 DIGITS? ARE THEY ALL NUMBERS?
    doc_number = name[0:8]
    doc_split = name.split()

    # check that it's an integer
    try: int(doc_number)
    except: 
        print("\tThe part {0} isn't an integer. Please reformat.".format(doc_number))
        accept_file = False

    # check that the number doesn't contain a space
    if ' ' in doc_number:
        print("\tThe part number {0} contains a space, or isn't 8 digits. Please reformat.".format(doc_number))
        accept_file = False

    # check that the file name is not a monolithic string
    try: doc_split[1]
    except:
        print("\tThe part {0} is one single string. Please reformat.".format(doc_number))
        accept_file = False

    # check that the second entry in doc_split contains open/closed parenthesis
    if ('(' or ')') not in doc_split[1]:
        print("\tThe part {0}'s revision is not enclosed by (). Please reformat.".format(doc_number))
        accept_file = False

    # check that the part says (1) not (REV 1)
    if 'R' in doc_split[1]:
        print('\tPlease reformat {0} as (#) instead of (REV #) or (R#).'.format(doc_number))
        accept_file = False

    
    # AT THE END OF THE FUNCTION, RETURN accept_file
    return accept_file
    
