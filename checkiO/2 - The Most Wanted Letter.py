def checkio(word):
    letter = ''
    quantity = 0

    word = word.lower()
    
    for l in word:
        if l in 'abcdefghiglmnopkrstuvxzkyw' and word.count(l) > quantity:
            letter = l
            quantity = word.count(l)
        elif l in 'abcdefghiglmnopkrstuvxzkyw' and word.count(l) == quantity:
            if l < letter:
                letter = l
    return letter

import string


print(checkio("Hello World!"))   #== "l"
print(checkio("How do you do?")) #== "o"
print(checkio("One"))            #== "e"
print(checkio("Oops!"))          #== "o"
print(checkio("AAaooo!!!!"))     #== "a"
print(checkio("abe"))            #== "a"