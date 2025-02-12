num = int(input("Ingrese un número: "))
romano = ""

if num <= 3:
    romano = num*"I"
elif num == 4:
    romano = "IV"
elif num >= 5 and num <= 8:
    romano = "V"+(num-5)*"I"
elif num == 9:
    romano = "IX"
    
print(romano)
    
