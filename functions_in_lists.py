lucky_numbers = [29, 32, 54, 90, 5, 10]
friends = ["Ines", "Ricardo","Marcela","Chiquinho"]

#copia uma lista
friends2 = friends.copy()
lucky_numbers2 = lucky_numbers.copy()
#function sort() ordena a lista alfabéticamente, vai dar o erro com a lista friends porque juntamos as duas listas e uma tem inteiros
friends2.sort()
#inverte o sentido da lista, não ordena
lucky_numbers2.reverse()

print(friends2)
print(lucky_numbers2)
#função extends vai "juntar duas listas"
friends.extend(lucky_numbers)
#tambem podemos usar a append para juntar mais um elemento à lista
friends.append("Emanuel")
#também podemos recorer à função insert e defenir a posição onde queremos inserir na lista
friends.insert(2,"Aurora")
#remove function remove um elemento da lista
friends.remove(90)
#a function "clear()" - "apaga a lista"
# e a function pop() retira o ultimo elemento da lista


print(friends)
#podemos recorrer à function index() para encontrar um elemento, pois devolve a posição
print(friends.index("Aurora"))