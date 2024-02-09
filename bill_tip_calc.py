print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# total = bill * (1 + tip / 100)
total = tip / 100 * bill + bill
total_per_person = "{:.2f}".format(total / people)

# print(total)
# print(total_per_person)
print(f"Each person should pay: ${total_per_person}")
