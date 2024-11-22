def run():
    
    #Funcion para el ingreso de datos al arreglo
    def ingreso_enteros():
        # Comenzamos con una lista vacia para almacenar los valores
        numeros = []
    
        # Se solicita la longuitud del arreglo, como buscamos subarreglos continuos se ocupan como minimo 3 valores
        while True:
            try:
                longitud = int(input("¿Cual es la longitud del arreglo? (Debe ser al menos 3): "))
                if longitud < 3:
                    print("¡La longitud minima del arreglo es 3!")
                else:
                    break
            except ValueError:
                print("¡Por favor, ingresa un numero entero valido para la longitud!")
    
        # Ciclo para ingresar los enteros
        while len(numeros) < longitud:
            try:
                numero = int(input(f"Ingresa un numero entero: "))
                numeros.append(numero)
            except ValueError:
                print("¡Por favor, ingresa un numero entero valido!")
    
        print("\nLos numeros ingresados son:", numeros)
        return numeros
    
    a_dado = [-2,1,-3,4,-1,2,1,-5,4]
    
    #FUNCION PRINCIPAL
    def sub_arreglo_max(arreglo):
        res_max =[]
        largo = len(arreglo)
        for iter in range(largo):
             if(iter == 0):res_max.append(arreglo[iter])
             if(iter != 0):
                 res_max.append(max(arreglo[iter],res_max[iter-1]+arreglo[iter]))
        #Una vez creado el arreglo con los resultados de la función se selecciona la sum_max
        sum_max = max(res_max)
        #Idetificamos en que indice esta la sum_max
        posicion= res_max.index(sum_max)
 
        aux = 0
        resultado =[]
        for iter in range(posicion):
            resultado.append(arreglo[posicion - iter])
            aux += arreglo[posicion - iter]
            if(aux == sum_max): break
        
        return print("El subarreglo con la suma maxima es: ", resultado[::-1])
    
    sub_arreglo_max(ingreso_enteros())    
            
if __name__=='__main__':
    run()