def run():
    
    #Definimos los parametos, en el problema se consideran 2 parametos el monto solicitado y la edad del solicitante
    # donde se pondra como regla de negocio aperturar el credito si el cliente tiene una edad entre 25 y 60 años.
    
    #Para la cantidad disponible, supondremos que el banco tiene 2/3 de la cantidad total a solicitar
    
    creditos = {
        "credit1": {"monto": 50000, "edad": 18},
        "credit2": {"monto": 150000, "edad": 40},
        "credit3": {"monto": 32000, "edad": 22},
        "credit4": {"monto": 70000, "edad": 25},
        "credit5": {"monto": 12000, "edad": 47},
        "credit6": {"monto": 10000, "edad": 20},
        "credit7": {"monto": 32000, "edad": 58},
        "credit8": {"monto": 100000, "edad": 49},
        "credit9": {"monto": 13000, "edad": 63},
        "credit10": {"monto": 83000, "edad": 38},
        "credit11": {"monto": 50000, "edad": 52},
        "credit12": {"monto": 82000, "edad": 37}
    }
    
    capital = 2*sum(credito["monto"] for credito in creditos.values())/3
    
    #FUNCION PRINCIPAL
    def apertura_creditos(creditos, capital):  
        
        #Convertimos el diccionario en una lista para poder ordenar de menor a mayor con la funcion sorted
        creditos_ls = [(id_credito, credito) for id_credito, credito in creditos.items()]
        creditos_ord = sorted(creditos_ls, key=lambda x: x[1]["monto"])

        #Una vez ordenados, comenzamos a aperturar los creditos si cumplen con la regla de negocio impuesta al inicio
        creditos_aprob = []
        sum_creditos_aprob = 0
        
        for id_credito, detalles in creditos_ord:
            monto = detalles["monto"]
            edad = detalles["edad"]
    
            if (25 <= edad <= 60):
                if (sum_creditos_aprob + monto <= capital):
                    creditos_aprob.append((id_credito, detalles))
                    sum_creditos_aprob += monto 
 
        # Retornamos los créditos aprobados y la suma de los creditos aprobados
        print("\nLos creditos aprobados son:")
        for id_credito, detalles in creditos_aprob:
            print(f"{id_credito}: Monto: {detalles['monto']}, Edad: {detalles['edad']}")
        
        print(f"\nLa suma total de los montos aprobados es: {sum_creditos_aprob} y el capital bancario es {capital}")
    
    #Se llama la funcion
    apertura_creditos(creditos, capital)

if __name__=='__main__':
    run()