#variaveis para validação
my_secret = "python"
guess = ""
count = 0
count_limit = 3
game_over = False


#condição while enquanto a variavel guess não for igual à palavra my_secret
# e a condição game_over for True
#vai incrementando as tentantivas no count e enquanto não exceder as 3 tentantivas
#permite pedir mais uma tentativa, caso exceda as 3 tentativas sai do loop e valida
#se ganhamos ou perdemos atraves do valor do game_over

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
