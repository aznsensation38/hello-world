import math

 #Use level of service (LOS) to find tip rate where 10 is 30%, 5 is 15%, 0 is 0%.  LOS is divided into equal 1/3 divisions.
def tip_rate(level_of_service):
    tip_rate = (level_of_service / (1/3)) / 100
    return tip_rate

 # Calculates the total tip amount based on the tip_rate and pre-tax bill amount.
def total_tip_amount(bill_amount, tip_rate):
    total_tip_amount = bill_amount * tip_rate
    return total_tip_amount

# Calculate the total bill with tax pre tip
def total_bill_with_tax_minus_tip(bill_amount, tax_rate): 
    total_bill_with_tax_minus_tip = (bill_amount * tax_rate) + bill_amount
    return total_bill_with_tax_minus_tip

# Here the Inputs are defined per the assignment
bill_amount = float(input("Restaurant bill (without tax or tip): "))
tax_rate = float(input("Sales tax rate (in decimal format): "))
level_of_service = int(input("Level of service (as an integer): "))
number_of_friends = int(input("Number of friends (as an integer): "))

# Here are the function calls to calculate the total tip based on the level_of_service
rate_of_tip = tip_rate(level_of_service)
total_tip = total_tip_amount(bill_amount, rate_of_tip)

# 1) Calculate the amount each friend should pay toward the bill (with tax)
split_total_with_tax_noTip = total_bill_with_tax_minus_tip(bill_amount, tax_rate) / number_of_friends

# 2) Calculate what each friend should leave in tip, pre-tax
splitTip = total_tip / number_of_friends

# 4) Calcualte the total bill with tax and tip
total_bill = total_tip  + total_bill_with_tax_minus_tip(bill_amount, tax_rate)

# 3) Calculate the amount each diner should  pay, cinluding bill, sales tax, and tip
split_total_with_tax_tip = total_bill / number_of_friends


# Here are the prints/outputs from the calculations
print("Bill (with tax) per person: " + str(split_total_with_tax_noTip)) 
print("Tip per person: " + str(splitTip))
print("Total per person: " + str(split_total_with_tax_tip)) 
print("Total bill including tax and tip: " + str(round(total_bill, 2))) 