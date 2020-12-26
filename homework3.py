import random
import sys


def playGame():
    words = ['python', 'java', 'javascript', 'kotlin', 'go', 'swift',
             'abap', 'php', 'ruby', 'dart', 'scala', 'haskell', 'julia', 'matlab',
             'pascal', 'pearl', 'rust', 'sql']
    word = random.choice(words)
    print(word)
    count = 5
    guesses = []
    x = len(word)
    temp = list('_'*x)

    while count > 0:
        guess = input('Guess a letter: ')
        if len(guess) > 1:
            print("Please enter a just letter")
            continue
        elif guess not in word:
            count -= 1
            if count == 0:
                print(f"Game Over!! Word is: {word}")
                menu()
            print(f" Wrong guess, {count} tries left.")
        else:
            for i in range(len(word)):
                if guess == word[i]:
                    temp[i] = guess
                    print(' '.join(temp), end='\n')
                    if guess in guesses:
                        print("Please enter different letter")
                    else:
                        guesses.append(guess)
                        print("xxx",guesses)

                    if '_' not in temp:
                        print(f"Congratulations!!!")
                        menu()


def menu():
    choice = True
    print(""" --Main Menu--
    1. Play Game 
    2. Exit """)
    choice = input()
    if choice == "1":
        print("Let's guess the word (hint:programming language)")
        playGame()
    elif choice == "2":
        sys.exit()
    else:
        print("Not valid choice try again!!")


def main():
    name = input("Please enter your name: ")
    print(f"---Hi {name}, Welcome to the Hangman game---")
    menu()


if __name__ == "__main__":
    main()
