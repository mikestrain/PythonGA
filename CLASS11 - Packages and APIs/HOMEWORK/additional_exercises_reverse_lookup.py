import os
os.system("clear")

def reverse_lookup(lookup_value,dictionary):
    lookup_key = None
    for key in dictionary:
        if state_capitals[key] == lookup_value:
            lookup_key = key
    return lookup_key

lookup_value = "Boston"

state_capitals = {
    "Alaska":"Juneau",
    "Colorado":"Denver",
    "Texas":"Austin",
    "Ohio":"Columbus",
    "Massachusetts":"Boston"
}

print(reverse_lookup(lookup_value,state_capitals))