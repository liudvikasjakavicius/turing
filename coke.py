# Variable
amount_due = 50
# Loop until the outstanding_balance is greater than 0
while amount_due > 0:
    # Print the outstanding balance
    print("Amount Due:", amount_due)
# Ask the user to insert a coin
    coin = int(input("Insert Coin: "))
# Check if the coin is 25, 10, or 5 cents
    if coin in [25, 10, 5]:
        amount_due -= coin  # Corrected the subtraction
# Calculate change owed and print
print("Change Owed:", -amount_due)