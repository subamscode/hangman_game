word="python"
guessed=""
chances=5

print("Welcome to Hangman Game")
print("You have 5 chances to guess the word")

while chances>0:
    display=""

    for letter in word:
        if letter in guessed:
            display+=letter
        else:
            display+="_"
    print("Word:" ,display)

    if display==word:
        print("You Win!")
        break
    guess=input("Guess a letter: ").lower()
    guessed+=guess

    if guess not in word:
        chances-=1
        print("Wrong guess. You have",chances,"chances left")
        
    if chances==0:
        print("You lose! The word was",word)
            