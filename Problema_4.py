def run():
    productos_1 = {
        'p1':[(10,1.5), (3,1.4), (5,1.6)],
        'p2':[(7,2.1), (2,2.0), (1,2.2), ("NA","NA")],
        'p3':[(12,1.7), (8,1.6), (3,1.8)]
    }
    
    #Funcion precio total
    def costos(productos): 
        #Comenzamos con un ciclo para calcular los costos de cada pi, inicializamos en 0 e imprimos el costo para ese pi   
        for producto, datos in productos.items():
            costo_total = 0  
            for cant, costo_uni in datos:
                if cant == "NA" or costo_uni == "NA": #se agrega esta condicion para ignorar los valores nulos
                    continue  
                costo_total += cant * costo_uni

            print(f"Costo total para el producto {producto}: {costo_total}")
    
    #Se manda llamar la funcion    
    costos(productos_1)
    
    elementos ={
        'e1':{"v1":8, "v2": 7, "v3": 6},
        'e2':{"v1":9, "v2": 6, "v3": 7},
        'e3':{"v1":7, "v2": 8, "v3": 8}
    }
    
    #Funcion promedio mas alto
    def promedio_alto_ord(elem): 
        promedios=[]
        
        #Comenzamos con un ciclo para calcular los promedios de cada ei
        for elemento, valores in elem.items():
            promedio = sum(valores.values())/len(valores)
            promedios.append(promedio) 
        
        prom_max = max(promedios)
        indice_max = promedios.index(prom_max)
        print(f"\nEl elemento con el promedio más alto es el e{indice_max+1} con un promedio de {promedios[indice_max]}")
        #se agrega un +1 porque comienza en 0    

        #Una vez encontrado el promedio mas alto continuamos con el ordenamiento del diccionario por promedio ascendiente
        prom_ord = sorted(promedios, reverse=True)
        elementos_ord ={}
        
        for prom in prom_ord:
            indice = promedios.index(prom)
            clave = list(elem.keys())[indice]
            elementos_ord[clave] = elem[clave]
            
        #Ya ordenados por separado imprimimos el resultado del ordenamiento 
        print("\nDiccionario ordenado por promedio es:")
        for elemento, valores in elementos_ord.items():
            print(f"{elemento}: {valores}")    
        
        
    #Se manda llamar la funcion    
    promedio_alto_ord(elementos)
 

if __name__=='__main__':
    run()