#lists ou arrays 

friends = ["Ines", "Ricardo","Marcela","Chiquinho"]

print(friends)

#aceder a elementos dentro de uma array
#tal como outras linguagens as listas ou arrays são acedidas pelo index
#curiosidade
print("O Paixão é o " + friends[1])

print(friends[2:]) 
#vai imprimir os valores depois do 2 registo para a frente
print("são um casal") 

print(friends[0:2]) #imprime desde o primeiro até ao terceiro mas não inclui o terceiro
print("têm uma filha")

#como alterar um elemento de uma array
#troquei Ricardo por Paixão
friends[1] = "Paixão" 
print(friends)