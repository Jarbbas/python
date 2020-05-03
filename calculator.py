num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
#inputs no python são reconhecidos como strings, por isso temos que converter para inteiros
#no entanto assim só aceita inteiros, por isso é mais seguro converter para float
#no python tal como o C e java temos que dizer qual o tipo das variaveis são
result = float(num1) + float(num2) 
print(result)
