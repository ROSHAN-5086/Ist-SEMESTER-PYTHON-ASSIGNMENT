#program to find income tax
#taking input from the user
income=float(input("Enter your Gross Income:"))
dependent=int(input("Enter number of dependent:"))
tax=(income-10000-(dependent*3000))*(0.2) #tax formula
#printing the tax
if tax>0:
    print("Your taxable amount is",tax)
else:
    print("You don't need to pay tax")
