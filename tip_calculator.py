print("Welcome to tip calculator using python")
total_bill = float(input("What was the total bill "))
tip_percentage = int(input("what percentage of tip you like to give? 10,12 or 15? "))
people_no = int(input("How many people to split the bill? "))
pay = (total_bill + total_bill*tip_percentage/100 )/people_no
print(f"Each person should pay: {round(pay,2)}")
#or you can write 
#print("Each person should pay:",round(pay,2))
