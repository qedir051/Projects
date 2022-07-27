print("Welcome to the tip calculator!\n")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
each_money = (total_bill / people) * (1 + tip / 100)
each_money_final = round(each_money, 2)
each_money_final= "{:.2f}".format(each_money)
print(f"Each person should pay: $ {each_money_final}")