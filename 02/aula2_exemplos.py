# ARREDONDAR
print(round(8/3))

#se quero especificar o quanto de casas decimais, ex de duas casas:
print (round(8/3,2))

#se quero especificar o quanto de casas decimais, ex de três casas:
print (round(8/3,3))

#Pavimentos, divisão sempre retorna em float, se utilizar // retorna em int, ex:
print(type(4 // 2))

#utilizando variável, de forma direta, ex: /:
result = 4/2
result /=2
result=int(result)
print(result)

#Resultado e mais um,ex: (+= ,-=  , *=  , /= ):
score=0
score+= 1
score+= 1
print(score)

#f-String :  para converter types numa concatenação: (f"...{...}"),  ex:
#int:
score= 0
#float
height = 1.8
#Bolean
isWinning = True

print(f"Your score is {score}, you height is {height}, you are winning is {isWinning}. ")
