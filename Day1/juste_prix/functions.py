def verifier(currentPrice, realPrice, score):
    if int(currentPrice) == realPrice:
        print("Congratulations " + currentPrice + " is the good price !")
        print("Final score: " + str(score))
    else:
        while int(currentPrice) != realPrice:
            if int(currentPrice) < realPrice:
                print("It's more, enter new proposition:")
                score = score - 1
                print("Current score: " + str(score))
                currentPrice = input()
            else:
                print("It's less, enter new proposition:")
                score = score - 1
                print("Current score: " + str(score))
                currentPrice = input()
        if int(currentPrice) == realPrice:
            print("Congratulations " + currentPrice + " is the good price !")
            print("Final score: " + str(score))