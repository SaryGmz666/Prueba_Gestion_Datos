-- Creacion de base de datos, tablas y relaciones
CREATE DATABASE SUELDOS_ESTUDIANTES
GO

USE SUELDOS_ESTUDIANTES

CREATE TABLE Estudiantes(
	ID INT IDENTITY(1,1) PRIMARY KEY,
    Nombre VARCHAR(50) not NULL
);

CREATE TABLE Amigos(
    ID INT NOT NULL,
    Amigo_ID INT NOT NULL,
    PRIMARY KEY (ID, Amigo_ID),
    FOREIGN KEY (ID) REFERENCES Estudiantes(ID),
    FOREIGN KEY (Amigo_ID) REFERENCES Estudiantes(ID)
);

CREATE TABLE Salario(
    ID INT PRIMARY KEY,
    Salario FLOAT NOT NULL,
    FOREIGN KEY (ID) REFERENCES Estudiantes(ID)
);

--- Ingreso de datos ---
INSERT INTO Estudiantes (Nombre)
VALUES
('Manuel'),
('Tania'),
('Pedro'),
('Ana'),
('Luis'),
('Marta'),
('Jorge'),
('Clara'),
('Pablo'),
('Sara'),
('David'),
('Laura'),
('Mario'),
('Silvia'),
('Carlos'),
('Isabel'),
('Antonio'),
('Elena'),
('Francisco'),
('Sofia');

--SELECT * FROM Estudiantes;
GO

INSERT INTO Amigos(ID, Amigo_ID)
VALUES
(1,1),
(2,20),
(3,3),
(4,12),
(5,4),
(6,5),
(7,1),
(8,13),
(9,6),
(10,12),
(11,17),
(12,18),
(13,19),
(14,8),
(15,9),
(16,15),
(17,10),
(18,7),
(19,10),
(20,11);

--SELECT * FROM Amigos

INSERT INTO Salario(ID, Salario)
VALUES
(1,15200.1), -- Se edita desde el ingreso para que no marque error
(2,10060.2),
(3,11500.5),
(4,12120),
(5,13200.75),
(6,9500.4),
(7,14500),
(8,10300.3),
(9,16000),
(10,8500.5),
(11,9000),
(12,17000.75),
(13,11000.2),
(14,12500.4),
(15,13500.1),
(16,9200.6),
(17,10100.8),
(18,11200.9),
(19,14000.25),
(20,14500.5);

--SELECT * FROM Salario;