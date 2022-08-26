# Ex_Listas

# fruits = [item1, item2]
# fruits = ["Cherry", "Aplle","Pear"]
# print(fruits[0])

from os import stat


states_of_america = ["Delawaree", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
print(states_of_america[-2])

# Se escrever negativo como ex: print(states_of_america[-1]) -  ele pega do último da lista e segue retornando ao inicio.

# Para alterar um item da lista:
states_of_america [0] = "Delaware"
print (states_of_america[0])

# como acrescentar algo na lista:
states_of_america.append("Julianalandia")
print(states_of_america)

# acresentar uma lista:
states_of_america.extend(["Navarrolandia", "Julandia"])
print(states_of_america)