num1 = float(input("Enter the frist number: ")) #input com conversão para float para garantir numeros e não strings
operator = input("Enter the operation: ") #pede o operador para a operação a realizar
num2 = float(input("Enter the second number: ")) #input com conversão para float para garantir numeros e não strings

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 - num2)
else:
    print("invalid operation input")
