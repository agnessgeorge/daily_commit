deposits = []
withdraws = []
full_log = []
d = 0
w = 0
account_balance = 0


def balance():
    total_deposits = 0
    total_withdraws = 0

    for a in deposits:
        total_deposits = total_deposits + int(a)
    for b in withdraws:
        total_withdraws = total_withdraws + int(b)
    bal = total_deposits - total_withdraws

    print bal


while True:
    answer = raw_input("do you want to add to transaction log(yes/no)?: ")
    if answer == "yes":

        log = raw_input("input the log here:")
        log_split = log.split(' ')

        for thisElement, nextElement in zip(log_split, log_split[1:] + log_split[: 1]):
            if thisElement == "d" or thisElement == "D":
                deposits.append(nextElement)
            elif thisElement == "w" or thisElement == "W":
                withdraws.append(nextElement)

    elif answer == "no":
        print("Your Account Balance is:")
        balance()
        print("thank you for banking with us!")
        break
    else:
        print("invalid input")
