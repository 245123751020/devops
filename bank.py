balance = 0

print("1. Deposit")
print("2. Withdraw")
print("3. Check Balance")

choice = int(input("Choose an option: "))

if choice == 1:
    amount = float(input("Enter deposit amount: "))
    balance += amount
    print("New balance:", balance)

elif choice == 2:
    amount = float(input("Enter withdrawal amount: "))
    if amount <= balance:
        balance -= amount
        print("New balance:", balance)
    else:
        print("Insufficient balance")

elif choice == 3:
    print("Current balance:", balance)

else:
    print("Invalid choice")

