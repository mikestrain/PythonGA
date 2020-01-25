#What's R2D2 Saying - Translation Program
# 
# ​# R2D2s BeepBoopBops language to EnglishLetter RosettaStone implemented as a tuple
R2D2sBeepBoopBopsTotalNumToEnglishLetterRosettaStone = (' ', 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
#  R2D2's "Letter" by "Letter" Vocalization implemented as dicitonary withn a dictionary
R2D2sBeepBoopBopsVocalization = {1:{'Beep':2, 'Boop':6},
                                2:{'Boop':5},
                                3:{'Beep':9, 'Boop':3},
                                4:{'Beep':4, 'Boop':8},
                                5:{'Beep':10, 'Boop':5},
                                6:{'Bop':0},
                                7:{'Beep':11, 'Boop':12},
                                8:{'Beep':10, 'Boop':5},  #Corrected J to O
                                9:{'Beep':1, 'Boop':17},
                                10:{'Beep':5, 'Boop':7},
                                11:{'Beep':4}}
# Total of Beep, Boop & Bop values which translates to the numeric value associated with a letter of the Engish alphabet
totalBeepBoopBobs = 0

R2D2sBeepBoopBopsToEnglishTranslation = ''

print('R2D2 said...')
for vocalizationKey, vocalizationValue in R2D2sBeepBoopBopsVocalization.items():
    for BeepBoopBopKey, BeepBoopBopValue in vocalizationValue.items():
        print((str(BeepBoopBopKey) + ' ') * BeepBoopBopValue)
        if BeepBoopBopKey == 'Bop':
            print("Bop")
        totalBeepBoopBobs = totalBeepBoopBobs + BeepBoopBopValue
    print(totalBeepBoopBobs)
    R2D2sBeepBoopBopsToEnglishTranslation = R2D2sBeepBoopBopsToEnglishTranslation + R2D2sBeepBoopBopsTotalNumToEnglishLetterRosettaStone[totalBeepBoopBobs]
    totalBeepBoopBobs = 0

# Print R2D2's English translation of BeepBoopBob uttterance
print(' ')
print('English translation:  ' + R2D2sBeepBoopBopsToEnglishTranslation.title())