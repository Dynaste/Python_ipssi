def verifier(currentPrice, realPrice):
    if int(currentPrice) == realPrice:
        print("Congratulations " + currentPrice + " is the good price !")
    else:
        while int(currentPrice) != realPrice:
            if int(currentPrice) < realPrice:
                print("It's more, enter new proposition:")
                currentPrice = input()
            else:
                print("It's less, enter new proposition:")
                currentPrice = input()
        if int(currentPrice) == realPrice:
            print("Congratulations " + currentPrice + " is the good price !")