income = float(input("Enter the annual income: "))

if (income<85528):
    tax=(income*18/100)-556.2
else:
    tax= (14,839.2+((income-85528)*32/100))   
if (tax<=0):
    tax=0
                  
tax = round(tax, 0)
                  
                  
print("The tax is:", tax, "thalers")
