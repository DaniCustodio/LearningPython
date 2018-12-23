#A senha é considerada forte o suficiente se o seu comprimento for superior ou igual 
# a 10 caracteres, contenha pelo menos um caractere numérico, uma letra maiúscula 
# e uma letra minúscula. A senha contém apenas caracteres latinos ASCII ou dígitos.
def checkio(password):

    length_check = False
    number_check = False
    lower_check = False
    upper_check = False

    if len(password) >= 10:
        length_check = True
    for ch in password:
        if ch in '0123456789':
            number_check = True
        if ch in 'abcdefghiglmnopkrstuvxzkyw':
            lower_check = True
        if ch in 'abcdefghiglmnopkrstuvxzkyw'.upper():
            upper_check = True

    if length_check and number_check and lower_check and upper_check:
        return True
    else:
        return False

print(checkio('A1213pokl')) #== False
print(checkio('bAse730onE')) #== True
print(checkio('asasasasasasasaas')) #== False
print(checkio('QWERTYqwerty')) #== False
print(checkio('123456123456')) #== False
print(checkio('QwErTy911poqqqq')) #== True