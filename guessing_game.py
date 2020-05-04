my_secret = "python"
guess = ""
count = 0
count_limit = 3
game_over = False

while guess != my_secret and not(game_over):
    if count < count_limit:
        guess = input("Enter the secret word: ")
        count += 1
    else:
        game_over = True

if game_over:
    print("out of guesses, you lose!")
else:
    print("you win!")
