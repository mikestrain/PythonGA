
def check_in_class(*class_list):

    pyclass = ['mike','vivake','chuck']

    for student in class_list:
        if student in pyclass:
            x = student in class_list
            print(student,"is in the class")

check_in_class("mike","bob","chuck","eva")