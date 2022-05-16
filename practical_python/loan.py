money_owed = float(input("how much money do you owe, in dollars?\n"))
apr = float(input("what is the annual percentage rate?\n"))
payment = float(input("what will your monthly payments be?\n"))
months = int(input("how many months do you want to see the results for?\n"))

#divide apr by 100 to make it a percent, then divide by 12 to make it monthly
monthly_rate = apr/100/12

for i in range(months):
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid

    if (money_owed - payment < 0):
        print("The last payment is", money_owed)
        print("You paid off the loan in", i+1, "months")
        break

    money_owed = money_owed - payment

    print("Paid", payment, "of which", interest_paid, "was interest", end=' ')
    print("Now I owe", money_owed)
