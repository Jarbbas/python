#ciclos for no caso no puthon é diferente do que php ou javascript
#este exemplo vai correr a sting e vai devolver cada letra da string
#letter é uma função nativa do python

for letter in "amor eu gosto de ti":
    print(letter)

#array friends
family = ["Emanuel", "Carla", "Camila"]
#neste caso o ciclo for vai correr todos os elementos da array
#podemos denominar qualquer nome para a variavel que vai correr o loop dentro da array
for familymenber in family:
    print(familymenber)

#exemplo mais concencional onde o ciclo vai correr as 9 vezes e começando com o elemento 0
for index in range(10):
    print(index)

#exemplo de um mais ciclo for onde segue o range e imprime quando passar pela 3º iteração
for index in range(5):
    if index == 3:
        print("forth iteration")
    else:
        print("Not")
