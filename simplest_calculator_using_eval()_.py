# Autor : Muhammad imran
#using python's built-in eval() function
#----------------------------------------
try:
    string = input('Enter values and operator to calculate answer : \n')
    print(eval(string))
except:
    print('please enter proper values and operator.')