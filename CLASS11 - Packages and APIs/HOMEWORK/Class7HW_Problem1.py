# Jason is a huge Jacksonville Jaguars fan. The team isn't doing great now, but he has faith: "All we need is a defense, and an offense,
# and some rule changes!"

# Expected Output
# How are the Jags doing?
# We have offense: True
# We have defense: True
# We have some rule changes: True
# We're going to the Super Bowl!
import os
os.system("clear")

offense = False
defense = False
rule_changes = False

def get_offense():
    offense = True
    return offense

def get_defense():
    defense = True
    return defense

def get_rule_changes():
    rule_changes = True
    return rule_changes

if not offense and not defense:
    rule_changes = get_rule_changes()
    offense = get_offense()
    defense = get_defense()

print("How are the Jags doing?\n")
print("We have offense:", offense)
print("We have defense:", defense)
print("We have some rule changes:", rule_changes)

if offense and defense and rule_changes:
    print("We're going to the Super Bowl!")
else:
    print("I can't predict the future, but no, the Jaguars will never win the Super Bowl.")