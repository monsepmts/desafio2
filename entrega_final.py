import random
N=int(input("Ingrese cuantos contenedores máximo puede tener la pila: "))
M=int(input("Ingrese cuantas pilas máximo serán: "))
orden=(input("Establesca si el llenado de contenedores será al azar o personalizado. Ingrese la letra A para azar y la P para personalizado: "))
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
        for i in range(N):
            for j in range(M):
                if puerto[i][j]==c:
                    print("Encontrado ",puerto[i][j],"en la pila ",i,"columna ",j)
         
    if a==3:
        if orden=="A":
            numero_c=int(input("Ingrese el número del contenedor: "))
            nombre_e=input("Ingrese el nombre de la empresa: ")
            c=numero_c,nombre_e
            nombre_e=(input("Ingrese el nombre de la empresa: "))
            c=numero_c,nombre_e
            fila_n=random.randint(2,(N-1))
            fila_m=random.randint(0,(M-1))
            while puerto[i][j]!=0:
                fila_n=random.randint(2,(N-1))
                fila_m=random.randint(0,(M-1))
                puerto[i][j]=c
            
                    
                for i in range(N):
                    for j in range(M):
                        print("|",puerto[i][j],"|",end="")
                    print("")
            
        else:
            numero_c=int(input("Ingrese el número del contenedor: "))
            nombre_e=input("Ingrese el nombre de la empresa: ")
            
        puerto[N-1][M-1]=int(numero_c),str(nombre_e)
        
            
        
        for i in range(N):
            for j in range(M):
                print("|",puerto[i][j],"|",end="")
            print("")
    if a==4:
        numero_c=int(input("Ingrese el número del contenedor: "))
        nombre_e=input("Ingrese el nombre de la empresa: ")
        c=numero_c,nombre_e
        for i in range(N):
            for j in range(M):
                if puerto[i][j]==c:
                    print("Encontrado ",puerto[i][j],"en la pila ",i,"columna ",j)
        
        

    a=int(input("Ingrese el número de la acción que desea realizar: "))
        
