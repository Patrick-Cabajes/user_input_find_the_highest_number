#ask user to input 5 variables
var1 = float(input("Enter first variable: "))
var2 = float(input("Enter second variable: "))
var3 = float(input("Enter third variable: "))
var4 = float(input("Enter fourth variable: "))
var5 = float(input("Enter fifth variable: "))

#compare the variables
#compare var1 to var2
if var1 >= var2:
    highest = var1
else:
    highest = var2

#compare var2 to var3
if var2 >= var3:
    highest = var2
else:
    highest = var3

#compare var3 to var4
if var3 >= var4:
    highest = var3
else:
    highest = var4

#compare var4 to var5
if var4 >= var5:
    highest = var4
else:
    highest = var5 

#print the highest variable
print(f'The highest variable is: {highest}')