# Agregar y quitar valores de una lista

Valores = [8,23,59]
Valores.append (69) # .append() se usa para argegar valores a una lista
Valores.append(6.6) # Solamente se puede agregar un valor a la vez


Nombres = ["Asimov","Momo","Agatha"]

#Se puede imprimir un solo valor de la lista utilizando el comando
#Para imprimir el tercer indice de la lista
print (Nombres [2])


Nombres.insert (2,"Pedro") # 'XXXXX'.insert() se usa para argegar valores a una lista en un indice específico
                           # Si ya hay un elemento foren la posición que  agregas el valor insertado reemplaza el valor dentro de la lsuta
                           # Solamente se puede agregar un valor a la vez

Valores.pop() # 'XXXXX'.pop() se usa para quitar el último valor de la lista
Nombres.pop(1)
# Se puede especificar el indice que se quiere quitar

# Se puede almacenar en una valirable los datos eliminados
removed = Valores.pop()
eliminado = Nombres.pop(1)

# Loop en listas usando FOR par imrprimir todos los valores de una lista
    
puntuaciones_finales = [17, 22,34,13]


for score in puntuaciones_finales:
	print(score)


'''
La variable antes de 'in' guarda los elementos de la lista
Puedes separar los elementos de la lista usando::
	print(todos)
	print('------')
'''

#En el loop se pueden hacer operaciones aritméticas agreando la operación en el 'print()'
print(todos*4)
print(todos+69)


# La función 'len()' nos sirve para saber cuantos elementos hay en una lista
# La función 'len()' se puede guardar en una variable
'''
Se puede usar la función 'len()' para crear una condicional
Ej:
         len(task)<5
         len(task)==89
         len(task)>1
'''

# Para imprimir el valor más grande de una lista se usa el comando 'max()'

scores = [8,96,9,31,48,32.3,78.99, -9]
print(max(scores))

# Para imprimir el valor más pequeño de una lista se usa el comando 'min()'
print(min(scores))


# Ambos comandos pueden ser guardados en una variable

num_minimo = min(scores)
num_maximo = max(scores)


# Para ordenar los valores del minimo al máximo se usa el comando 'XXXX'.sort()
scores.sort()
print(scores)


# Se puede usar .sort() para ordenar alfabéticamente listas que contienen strings

# Se puede usar print(sum('XXXX')) para sumar todos los elementos de una lista
# Se puede guardar en una variable

total = sum(scores)

'''
Se pueden combinar dos o más listas usando '+' {ES COMO USAR .append()}
Los valores de la otra lista se agregan al final
'''
print(lista_1 + list_2 + Lista_3)

# se pueden combinar listas con cualquier tipo de valor (int, flaot, bool, str, bool)

# Podemos contar las veces que se repite en un elemento dentro de una lista usando el comando 'XXXXX'.count()

otra_lista = [8,8,9,2,4,961,6,9,18,0,6,8.6]
print(otra_lista.count(8))

# Usar 'in' nos permite saber si existe o no un elemento dentro de una lista

print ("Momo" in Nombres) # ------ Da como ressultado un bool
