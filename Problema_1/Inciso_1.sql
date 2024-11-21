USE SUELDOS_ESTUDIANTES
GO

--Antes de comenzar con el código realizaremos modificaciones en la tabla Amigos, por ejemplo la fila 1 
--menciona que el estudiante 1 es amigo del estudiante 1 y no es racional.

UPDATE Amigos SET Amigo_ID = 2 WHERE ID = 1;
UPDATE Amigos SET Amigo_ID = 14 WHERE ID = 3;
SELECT * FROM Amigos;
GO

-- Inicio del problema inciso 1
SELECT 
    Estudiantes.Nombre, 
    SalarioAmigo.Salario AS Salario_Amigo -- Modificamos el nombre para no crear confusiones
FROM 
    Estudiantes
JOIN 
    Salario ON Estudiantes.ID = Salario.ID -- Le agregamos el salario del estudiante 
JOIN 
    Amigos ON Estudiantes.ID = Amigos.ID -- Conectamos a cada estudiante con sus amigos
JOIN 
    Salario AS SalarioAmigo ON Amigos.Amigo_ID = SalarioAmigo.ID --Agregamos el salario del amigo
WHERE 
    SalarioAmigo.Salario > Salario.Salario --Realizamos las comparaciones y solo tomamos aquellos casos donde el amigo tiene un salario mayor
ORDER BY 
    SalarioAmigo.Salario DESC; -- Ordeamos