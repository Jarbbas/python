#a palavra reservada def é usada para functions no python
#o código é identado e é assim que defenimos o que está contido dentro da função
#boas práticas não obrigam, mas recomendar lowercase e underscore tal como as variaveis
def say_hi():
    name = input("What's your name: ")
    print("Hello ")
    return name

#esta função vai receber 3 parametros
#name que vem da função anterior
# e outras duas que são declaradas quando chamamos a função
# e no caso do age é um inteiro logo para imprimir tenho que converter age para string
def tell_age(name, girlfriend, age):
    print(name + " és o namorado da " + girlfriend + " e namoram há " + str(age) + " anos")


print("inicio")

#para chamar uma função é como as restantes linguagens
#say_hi() chama só a função say_hi

#mas este chama retorna o valor e reutiliza
tell_age(say_hi(),"Carla", 4)

print("fim")

#apesar do python ler o código do topo para o fim, no caso das
#das funções o pyhton é capaz de voltar atrás
#para ler e chamar a função
