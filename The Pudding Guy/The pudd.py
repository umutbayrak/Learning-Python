# Let's take the inputs first

total_purchased_item = int(input("Please enter the total number of items purchased products: "))
cost_per_product = float(input("Please enter the cost per product: "))
number_of_UPC = int(input("Please enter the number of UPCs needed for a frequent-flyer coupon: "))
number_of_miles_earned = int(input("Please enter the number of miles earned per frequent-flyer coupon: "))

# Calculation steps for money spent and total miles earned
# Used // operation to get the quotient because the rule is valid for every 10 UPCs

money_spent = float(total_purchased_item * cost_per_product)
frequent_flyer = total_purchased_item // number_of_UPC
total_miles_earned = frequent_flyer * number_of_miles_earned

print(f'Phillips spent ${money_spent} for {total_miles_earned} frequent-flyer miles.')
