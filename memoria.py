#2 - Memoria
#Cada variável em Python é uma **referência** para um objeto na memória (heap). A lista não guarda os valores “dentro” dela de forma rígida: guarda ponteiros para os objetos.

a = [1, 2, 3]
b = a          # b aponta para a MESMA lista
b.append(4)
print(a)       # [1, 2, 3, 4]

c = a.copy()   # cópia rasa (nova lista, mesmos objetos)

x = [10] # define o valor de x como 10 
y = [10] # define o valor de y como 10 porem em outro endereço de memória

print(id(x) == id(y))  # Consulta se o endereço é o mesmo 

if x == y:              # Compara se os valores são iguais
    print("Iguais")
else:
    print("Valores diferentes")

z = [5]

if z == x:
    print("Iguais")
else:
    print("Valores diferentes")