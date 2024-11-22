USE SUELDOS_ESTUDIANTES
GO

---Inicio del inciso 2
--Creamos la variable donde guardamos el promedio salarial
DECLARE @PromedioSalarial DECIMAL(10,2);
SET @PromedioSalarial = (SELECT AVG(Salario) FROM Salario);

--Hacemos la consulta principal
SELECT 
    Estudiantes.Nombre, 
    Salario.Salario
FROM 
    Estudiantes
JOIN 
    Salario ON Estudiantes.ID = Salario.ID -- Agregamos el salario del estudiante 
WHERE 
    Salario > @PromedioSalarial
ORDER BY 
    Salario DESC; -- Ordeamos de forma descendente