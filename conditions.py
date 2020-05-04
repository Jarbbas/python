
is_male = True
is_tall = True

#condições em pyhton usam a mesma sintax que as funções o código tem que estar identado e logo abaixo do definição
#tal como em outras linguagens podemos recorer às comparaçóes "and" , "or" e no caso da negação "not()" temos que por um paretensis
# no caso do else if a sintax é "elif"

if is_male and is_tall:
    print("Gratz it's a boy and he is tall")
elif is_male and not(is_tall):
    print("it's a small boy")
elif not(is_male) and is_tall:
    print("it's a girl and a tall one")
else:
    print("it's a girl")

num1 = input("Enter an number: ")
num2 = input("Enter a second number: ")
num3 = input("Enter a third number: ")

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(num1,num2,num3))
