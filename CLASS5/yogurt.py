def yogurt_land(spoon, **kwargs):
  print(spoon)
  # We need a loop, because we don't know how many kwargs there are.
  for keyword, flavor in kwargs.items():
    # kwargs.items has the keyword and the value, which we're calling "flavor" in the loop.
    print("My", keyword, "is a", flavor)
# Like before, the unnamed arg has to come first!
yogurt_land("large!", first_froyo="vanilla", second_froyo="chocolate", third_froyo="banana")