animals = {"dog": "cute, furry animal", "cat": "cute, arrogant animal", "elephant": "large mammal"}

#unlike lists, you need to print out key and value together

# animals[0] will print an error

print(animals["dog"]) # this will work, but how to know what the values are?

print(animals.items()) # this turns a dictionary into a list!

for item in animals.items():
    # print(item[0])
    print(item[0], item[1], sep=": \t")

# you can also do it this way, where there's a key and a value
# this only works for dictionary
for k, v in animals.items():
    # print(item[0])
    print(k, v, sep=": \t")