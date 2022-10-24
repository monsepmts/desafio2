M=int(input("Ingrese cuantos contenedores máximo puede tener la pila: "))
N=int(input("Ingrese cuantas pilas máximo serán: "))
puerto=[]
for i in range(N):
    puerto.append([])
    for j in range(M):
        puerto[i].append(None)
        
for i in range(N):
    for j in range(M):
        print("|",puerto[i][j],"|",end="")
    print("")
print("")

print(" Menú ")
print("Ingrese el número 1 si desea imprimir el estado del puerto seco.") 
print("Ingrese el número 2 si desea ubicar algún contenedor.")
print("Ingrese el número 3 si desea incluir un nuevo contenedor.")
print("Ingrese el número 4 si desea retirar un contenedor.")
print("Ingrese el número -1 si desea cerrar la jordana de trabajo.")
a=int(input("Ingrese el número de la acción que desea realizar: "))
while a!=-1:
    if a==1:
        for i in range(N):
            for j in range(M):
                print("|",puerto[i][j],"|",end="")
            print("")
        print("")
        
    if a==2:
        numero_c=int(input("Ingrese el número del contenedor: "))
        nombre_e=input("Ingrese el nombre de la empresa: ")
        c=numero_c,nombre_e
        try:
            posicion = puerto.index(c)
            print("El contenedor se encuentra en la posición: ", posicion)
                
        except ValueError:
            print("El contenedor no se encuentra en el puerto.")
            
            
    if a==3:
         numero_c=int(input("Ingrese el número del contenedor: "))
         nombre_e=input("Ingrese el nombre de la empresa: ")
         fila=int(input("Ingrese el número de la fila donde quiere colocar el contenedor: "))
         columna=int(input("Ingrese el número de la columna donde quiere poner el contenedor: "))
         
         puerto[fila][columna]=int(numero_c),str(nombre_e)
         
         for i in range(N):
             for j in range(M):
                 print("|",puerto[i][j],"|",end="")
             print("")
    a=int(input("Ingrese el número de la acción que desea realizar: "))
