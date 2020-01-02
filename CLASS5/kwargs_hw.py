import os
os.system("clear")

def address_printer(**address):

    #Address printer homework
    #Mike Strain, GA
    
    #mike strain
    #23 brown street, apartment 1
    #waltham, ma
    #02453

    i = 0
    first_name = ''
    last_name = ''
    street = ''
    street2 = ''
    city = ''
    state = ''
    zipcode = ''
    extra_values = []

    for V_input,value in address.items():

        if V_input == "first_name": first_name = value
        elif V_input == "last_name": last_name = value
        elif V_input == "street": street = value
        elif V_input == "street2": street2 = value
        elif V_input == "city": city = value
        elif V_input == "state": state = value
        elif V_input == "zipcode": zipcode = value
        else:
            # print("found extra input!")
            extra_values.append(value)
            i += 1
    
    print(first_name,last_name)
    print(street, street2)
    print(city + ",",state)
    print(zipcode)

    for val in extra_values:
        print(val)


address_printer(last_name = "Strain", \
    street = "23 Brown Street", street2 = "Apt 1", city = "Waltham", \
        state = "MA", zipcode = "02453",country = "USA", planet = "Earth", galaxy = "Milky Way")

