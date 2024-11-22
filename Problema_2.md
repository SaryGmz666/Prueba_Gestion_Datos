# Problema 2

Desarrolla un Datamart anexando los scripts que emplearías y responde las siguientes preguntas:

1. ¿Qué es un Datamart explicado en tus palabras? Describe detalladamente cómo un Datamart difiere de un Data Warehouse y da ejemplos de casos de uso específicos para un Datamart considerando como ejemplo, un banco.

    **R: Un Datamart es un extracto especifico de una base de datos, la cual sirve para una área en especifico; en el caso de un banco podemos tomar el área de Emisor, esta área visualiza toda la transaccionalidad de sus tarjetas bancarias, tanto débito como crédito, entonces la Datamart seria la operativa de los tarjetahabientes.**

    **La principal diferencia entre una Datamart y un Data Warehouse es la información que contiene; una Data Warehouse es la base de datos centralizada, en el caso del banco seria todos los productos y áreas diversas que lo compongan.**
    
2. Desarrolla las tablas del Datamart considerando las siguientes Dimensiones/Catálogos y construyéndose en base a la información que crees estas pudieran contener: Clientes, Productos que oferta el Banco, Tipo de cambio, Historial de transacciones. Además, debes incluir:
    - Un diagrama ERD (Entity-Relationship Diagram) mostrando las relaciones entre todas las tablas.

    **R: Retomando el ejemplo anterior veremos la operativa Emisor, esta se compone por:**
    - ***Clientes:*** Los clientes se encuentran relacionados a un número de cuenta, la cual puede estar relacionado a una o varias tarjetas bancarias.
    - ***Productos:*** Vienen siendo los productos Débito o Crédito y sus respectivos Bines relacionados que catalogan diferentes tipos de cuentas como Nómina, Cheques, Oros, Platinum, Personas Morales, entre otros.
    - ***Historial de transacciones:*** Es tal cual la transaccionalidad del cliente en diversos comercios, tranferencias, ingresos monetarios, etc.
        
    Considerando estas tablas existen las siguientes tablas y relaciones.
        
    **Tablas:**

    La tabla clientes se componde con los siguientes campos
    


3. Describe las relaciones entre las tablas especificando el tipo de relación (una a muchas, muchas a muchas, etc.) y justificando por qué ese tipo de relación es adecuado para cada par de tablas. Incluye también:
    - Explicación de cómo estas relaciones ayudan a satisfacer necesidades específicas del área de un banco.

    - De ser posible ¿Plantearías una relación que facilitara la conexión entre tablas? Es decir, una tabla intermedia que pueda manejar los datos de manera más óptima.

4. Identifica las llaves primarias y foráneas de cada tabla explicando lo siguiente:
    - El razonamiento detrás de la selección de éstas llaves.

    - Cómo manejarías las situaciones de datos faltantes o inconsistentes en estas llaves.

5. Establece controles para alimentar las tablas asegurando información correcta, íntegra, precisa y confiable. Para cada tabla,sigue las instrucciones siguientes:
    - Describe las validaciones específicas que le harías a los datos.

    - Describe cómo regularías que éstas validaciones se lleven a cabo.

    - ¿Qué estrategias propones para evitar la pérdida de datos?

6. Desarrolla un análisis para determinar los riesgos posibles utilizando un lenguaje de programación.

7. Describe las características que debe tener un archivo de texto para ser importado en la base de datos y cómo automatizarias éste proceso.

8. Realiza validaciones en un lenguaje de programación que cumplan con los criterios que estableciste.