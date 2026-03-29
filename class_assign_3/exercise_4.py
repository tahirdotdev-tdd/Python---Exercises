init_balance = 1000


in_amount = int(input("Enter the amount you want to add (only 500): "))

if in_amount == 500:
    init_balance += 500
    print(init_balance)


usr_chc = int(input("Do you want to apply interest rate? (1 or 2): "))

if usr_chc == 1:
    init_balance *= 1.05
    interest = init_balance
    print("With interest: ", interest)
    print("Your final balance is : ", "$", interest)
else:
    print("Error!")