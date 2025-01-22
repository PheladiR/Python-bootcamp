print("Welcome to the tip calculator!")
total_bill= float(input("What was the total bill?: R"))
tip= float(input("What percentage tip would you like to give? e.g 10 20 30: " ))
number_of_people= float(input("How many people split the bill?: "))

bill_with_tip= total_bill+ tip / 100 * total_bill

bill_per_person = bill_with_tip/number_of_people
print(f"each person should pay R {round(bill_per_person,2)}")