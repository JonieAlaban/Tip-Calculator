#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the tip calculator")
bill = input("Whats is your total bill? \n")
tip = input("How much tip do you want to give? 10, 12 or 15 \n")
num_people = input("How many people to split the bill? \n")

#Each person should pay (150.00 / 5) * 1.12 = 33.6

each_person_pay = (float(bill)/int(num_people)) * (1 + int(tip)/100)    

print(float(each_person_pay))

#Format the result to 2 decimal places = 33.15060

