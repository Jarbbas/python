from math import * #importa da biblioteca toda de funções matemáticas

#numeros inteiros

number1 = 1
number2 = 2
number3 = 3
add_number = (number1 + number2)
sub_number = (number2 - number3)
print(add_number)
print(sub_number)

#tambem podemos usar as funções diretamente no print

print(1 + 1)
print (30 % 2)

#também podemos converter numeros em strings
#atenção que strings e number são tipos de dados diferentes logo não podem ser concatenados
#temos que converter primeiro
print("o meu número favorito é o número " + str(number3))

my_number = -5
print(abs(my_number)) #devolve o valor absoluto do valor
print(pow(4, 6)) #função pow
print(max(4, 6)) #devolve o valor máximo
print(min(4,6)) #devolve o valor minimo
print(round(4.6)) #arredonda o valor
print(floor(3.7)) #devolver o valor mais pequeno
print(ceil(4.5)) #devolver o valor maior
print(sqrt(36)) #raiz 

