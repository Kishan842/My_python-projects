print("\t\t\t\t\t\t----------------------------------")
print("\t\t\t\t\t\tWelcome to Apna bank of Churchgate")
print("\t\t\t\t\t\t----------------------------------")
Restart = 'Y'
User_chance = 3
Total_Balance = 950000

while User_chance > 0:
    User_pin = int(input("Please Enter Your Pin: "))
    if User_pin == 8090:
        print("\nYou Entered your pin Correctly\n")

        while Restart not in ('n', 'No', 'no', 'N'):
            print("\tPlease Press 1 For Your Total-Balance")
            print("\tPlease Press 2 To Make a Withdrawal")
            print("\tPlease Press 3 To Pay in")
            print("\tPlease Press 4 To Return Card")
            print("\tPlease Press 5 To Exit")
            option = int(input("\nWhat would you like to Choose: "))

            # Condition One
            if option == 1:
                print("Your Balance is $", Total_Balance)

                Restart = input("\nWould You like to go back Your Card (y/n): ")
                print("\n")
                if Restart.lower() in ('n', 'no'):
                    print("Thank You")
                    break

            # Condition Two
            elif option == 2:
                withdrawal = float(input("How Much Would You Like to Withdraw?: "))

                if withdrawal <= Total_Balance:
                    Total_Balance = Total_Balance - withdrawal
                    print("Transaction Successful. Your Updated Total_Balance is $", Total_Balance, "\n")

                    Restart = input("Would You like to go back Your Card (y/n): ")
                    print("\n")
                    if Restart.lower() in ('n', 'no'):
                        print("Thank You")
                    break
                else:
                    print("Invalid Amount, Please Re-try")

            # Condition Three
            elif option == 3:
                pay_in = float(input("\tHow Much Would You Like To Pay In : "))
                Total_Balance = Total_Balance + pay_in
                print("\n\tYour Total_Balance is Now $", Total_Balance)

                Restart = input("Would You like to go back Your Card (y/n): ")
                print("\n")
                if Restart.lower() in ('n', 'no'):
                    print("Thank You")
                break

            # Condition Four
            elif option == 4:
                print("\tPlease Wait While Your Card is Returned...")
                break

            # Condition Five
            elif option == 5:
                exit_choice = input("\tWould you like to Exit (Y/N): ")
                if exit_choice.lower() == "y":
                    exit()
                elif exit_choice.lower() == "n":
                    Restart = 'Y'
                    break
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")

            else:
                print("Please Enter a Correct Option Number.")
                break
    else:
        print("Incorrect password")
        User_chance -= 1
        if User_chance == 0:
            print("\nNo more tries")
            break
