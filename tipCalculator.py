print("Welcome to the tip calculator!")

#Bill to pay
bill = float(input("what whas the total bill?: "))

#Tip percentage
tip = int(input("How much tip you like to give? 10,12, or 15?: "))

#amount of people to split
people = int(input("How many people to split the bill?"))

#Final Result
res = (bill*((tip/100+1)))/people

#Printing formatted result
print(f"Each person should pay: ${round(res,2)}")