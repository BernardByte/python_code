
#simple calculator that takes just two arguments with operator

ope=["+","-","*","/"]
inp=input("Enter numbers and operators to calculate:\n")

for i in inp:
    if i in ope:
        c=i
        a,b=inp.split(c)
        print('\n',a,b,'\n')
        a,b=int(a),int(a)

if c:
    if c == "+":
        print(a+b)
    elif c == "-":
        print(a-b)
    elif c == "*":
        print(a*b)
    elif c == "/":
        print(a/b)
else:
  print("something went wrong.")
