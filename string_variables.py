#variaveis strings no python
character_name = "Emanuel" 
character_age = "35"
character_hobbies = "programar"

#podemos usar o simbolo + para concatenar as strings
print("A personagem da nossa historia chama-se " + character_name + ".")
print("ele tem " + character_age + " anos")
print("e gosta de " + character_hobbies )

phrase = "Hello world"
print(phrase.upper()) #podemos chamar funções especificas atraves do .
print(phrase[0]) #imprimi a primeira letra, nesta caso "o" tal como muitas linguas começa o index a zero
print(phrase.index("w")) #a função index devolve o valor da posição 
print(len(phrase)) #tamanho da string
print(phrase.replace("Hello", "olá"))
