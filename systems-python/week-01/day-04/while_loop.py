
secret_number = 7
guess_count = 0
guess_limit = 5


while guess_count< guess_limit:
    guess  = int(input('Guess: '))
    guess_count = guess_count+1
    if guess == secret_number:
        print("You guessed right!")
        break

else:
    print("You failed to guess the right number")
    