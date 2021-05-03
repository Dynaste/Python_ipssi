
word = "hello"
word_display = "XXXXX"
word_display = list(word_display)
attempt = 0
guess_word = ""


while attempt <= 6 and guess_word != word:
    print("Attempt number "+ str(attempt) + ", word: " + str(word_display))
    guess_word = input("Enter a word: ")
    attempt = attempt + 1
    word_index = []

    if guess_word != word:
        for l in guess_word:
            for i in range(len(word)):
                if (word[i] == l):
                    word_index.append(i)
                    for n in word_index:  
                        word_display[n] = l
    else:
        print("Congratulation, you guess the word")


    if attempt == 7:
        print("You loose, try again :)")