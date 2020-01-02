

def reverse_lookup(value,dictionary):
    for items in dictionary.items():
        if items[1] == value:
            return items[0]

# proper form is to declare dictionaries across multiple lines!
state_capitals = {
  "Alaska" : "Juneau",
  "Colorado" : "Denver",
  "Oregon" : "Salem",
  "Texas" : "Austin"
  }

value = "Denver"

print(reverse_lookup(value,state_capitals))