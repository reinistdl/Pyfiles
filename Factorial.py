print ("Input number")
number = None
while(isinstance(number,int)!=True):
    my_input = input()
    try:
        number = int(my_input)
    except:
        print ("input number dumbfuck!")
resultats = 1
while(number>1):
    resultats=resultats*number
    number=number-1
print("Result: " +str(my_input) + "! =" + str(resultats))
