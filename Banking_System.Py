print("Welcome to Axis bank of Churchgate")
restart = 'Y'
chance = 3
balance = 950000

while chance > 0:
    pin = int(input("Please Enter Your Pin: "))
    if pin == 8424:
        print("You Entered your pin Correctly")
        while restart not in ('n', 'No', 'no', 'N'):
            print("Please Press 1 For Your Balance")
            print("Please Press 2 To Make a Withdrawal")
            print("Please Press 3 To Pay in")
            print("Please Press 4 To Return Card")
            option = int(input("What would you like to Choose: "))
            # Condition One
            if option == 1:
                print("Your Balance is $", balance,)
                restart = input("Would You like to go back: ")
                if restart in ('n','No', 'no', 'N'):
                    print("Thank You")
                    break
            # Condition Two
            elif option == 2:
                withdrawal = float(input("How Much Would You Like to Withdraw? \n$20\n$40\n$60\n$80\n"))

                if withdrawal in [20, 40, 60, 80]:
                    balance = balance - withdrawal
                    print("Transaction Successful. Your Updated Balance is $", balance,)
                    restart = input("Would You like to go back? ")
                    if restart in ('n','No', 'no', 'N'):
                        print("Thank You")
                    break
                else:
                    print("Invalid Amount, Please Re-try")
            # Condition Three
            elif option == 3:
                pay_in = float(input("How Much Would You Like To Pay In: $"))
                balance = balance + pay_in
                print("\nYour Balance is Now $", balance)
                restart = input("Would You like to go back? ")
                if restart in ('n','No', 'no', 'N'):
                    print("Thank You")
                break
            # Condition Four
            elif option == 4:
                print("Please Wait While Your Card is Returned...")
                break
            else:
                print("Please Enter a Correct Option Number.")
    else:
        print("Incorrect password")
        chance = chance - 1
        if chance == 0:
            print("\tNo more tries")
