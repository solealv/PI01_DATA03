USE pi_i;

# Tabla circuit
SELECT * FROM circuit; -- devuelve 77 registros

SELECT DISTINCT *
from circuit; -- devuelve 77 registros, no hay registros duplicados

SELECT DISTINCT circuitId
from circuit; -- devuelve 77 registros, no hay Id duplicados (este campo sera la PK de esta tabla mas adelante)

ALTER TABLE `circuit` CHANGE `circuitId` `circuitId` INT NOT NULL;
ALTER TABLE `circuit` CHANGE `circuitRef` `circuitRef` VARCHAR(100) NOT NULL;
ALTER TABLE `circuit` CHANGE `name` `name` VARCHAR(100) NOT NULL;
ALTER TABLE `circuit` CHANGE `location` `location` VARCHAR(100) NOT NULL;
ALTER TABLE `circuit` CHANGE `country` `country` VARCHAR(100) NOT NULL;
ALTER TABLE `circuit` CHANGE `lat` `lat` DECIMAL(9,5) NOT NULL;
ALTER TABLE `circuit` CHANGE `lng` `lng` DECIMAL(9,5) NOT NULL;
ALTER TABLE `circuit` CHANGE `alt` `alt` DECIMAL(9,5) NOT NULL;

# Tabla constructor
SELECT * FROM constructor; -- Devuelve 211 registros

SELECT DISTINCT * FROM constructor; -- Devuelve 211 registros, no hay registros duplicados

SELECT DISTINCT constructorId 
FROM constructor; -- Devuelve 211 registros, no hay Id duplicados

ALTER TABLE `constructor` CHANGE `constructorId` `constructorId` INT NOT NULL;
ALTER TABLE `constructor` CHANGE `constructorRef` `constructorRef` VARCHAR(100) NOT NULL;
ALTER TABLE `constructor` CHANGE `name` `name` VARCHAR(100) NOT NULL;
ALTER TABLE `constructor` CHANGE `nationality` `nationality` VARCHAR(100) NOT NULL;

# Tabla driver
SELECT * FROM driver; -- Devuelve 853 registros

SELECT DISTINCT * FROM driver; -- Devuelve 853 registros, no hay registros duplicados

SELECT DISTINCT driverId 
FROM driver; -- Devuelve 853 registros, no hay Id duplicados

SELECT DISTINCT number 
FROM driver
ORDER BY number ; -- Aparecen los caracteres \N para los conductores que no tienen numeros asignados 

-- Cambio el nombre del campo `number` a `num` por ser "number" una palabra reservada 
ALTER TABLE `driver` CHANGE `number` `num` TEXT;

SELECT DISTINCT num
FROM driver
ORDER BY num;
 

-- Imputar valor 0 a los registros con \N en el campo `number`
-- de esta manera se puede cambiar el tipo de dato en el campo a integer

SELECT num
FROM driver
WHERE num NOT IN ('10', '11', '12', '13', '14', '16', '17', '18', '19', '2', '20', '21', '22', '23', '25', '26', '27', '', '28', '3', '30', '31', '33', '35', '4', '44', '45', '5', '51', '53', '55', '6', '63', '7', '77', '8', '88', '89', '9', '94', '98', '99');

/* no podia filtrar con un simple WHERE num = '\N' 
   no me filtraba el valor*/

UPDATE driver SET num = '0' 
WHERE num NOT IN ('10', '11', '12', '13', '14', '16', '17', '18', '19', '2', '20', '21', '22', '23', '25', '26', '27', '', '28', '3', '30', '31', '33', '35', '4', '44', '45', '5', '51', '53', '55', '6', '63', '7', '77', '8', '88', '89', '9', '94', '98', '99'); 

-- valores actualizados
SELECT num
FROM driver;

ALTER TABLE `driver` CHANGE `driverId` `driverId` INT NOT NULL;
ALTER TABLE `driver` CHANGE `driverRef` `driverRef` VARCHAR(100) NOT NULL;
ALTER TABLE `driver` CHANGE `num` `num` INT NOT NULL;
ALTER TABLE `driver` CHANGE `code` `code` VARCHAR(10) NOT NULL;
ALTER TABLE `driver` CHANGE `name` `name` VARCHAR(100) NOT NULL;
ALTER TABLE `driver` CHANGE `dob` `dob` DATE NOT NULL;
ALTER TABLE `driver` CHANGE `nationality` `nationality` VARCHAR(100) NOT NULL;

# Tabla pit_stop
SELECT * FROM pit_stop; -- Devuelve 8030 registros

SELECT DISTINCT * FROM pit_stop; -- Devuelve 8030 registros, no hay registros duplicados

ALTER TABLE `pit_stop` CHANGE `raceId` `raceId` INT NOT NULL;
ALTER TABLE `pit_stop` CHANGE `driverId` `driverId` INT NOT NULL;
ALTER TABLE `pit_stop` CHANGE `stop` `stop` INT NOT NULL;
ALTER TABLE `pit_stop` CHANGE `lap` `lap` INT NOT NULL;
ALTER TABLE `pit_stop` CHANGE `time` `time` TIME NOT NULL;
ALTER TABLE `pit_stop` CHANGE `duration` `duration` DECIMAL(5,3) NOT NULL;

# Tabla race
SELECT * FROM race; -- Devuelve 1058 registros

SELECT DISTINCT * FROM race; -- Devuelve 1058 registros, no hay registros duplicados

SELECT DISTINCT raceId FROM race; -- Devuelve 1058 registros, no hay Id duplicados

ALTER TABLE `race` CHANGE `raceId` `raceId` INT NOT NULL;
ALTER TABLE `race` CHANGE `year` `year` INT NOT NULL;
ALTER TABLE `race` CHANGE `round` `round` INT NOT NULL;
ALTER TABLE `race` CHANGE `circuitId` `circuitId` INT NOT NULL;
ALTER TABLE `race` CHANGE `name` `name` VARCHAR(100) NOT NULL;
ALTER TABLE `race` CHANGE `date` `date` DATE NOT NULL;
ALTER TABLE `race` CHANGE `time` `time` TIME NOT NULL; -- Hay valores '\N' en el campo, se imputaran estos a 00:00:00

SELECT DISTINCT time
FROM race
ORDER BY time;

SELECT time
FROM race
WHERE time NOT IN ('03:00:00', '04:30:00', '05:00:00', '05:10:00', '06:00:00', '06:10:00', '07:00:00', '08:00:00', '09:00:00', '09:30:00', '10:10:00', '11:00:00', '11:10:00', '11:30:00', '12:00:00', '12:10:00', '13:00:00', '13:10:00', '14:00:00', '14:10:00', '14:30:00', '15:00:00', '15:10:00', '16:00:00', '17:00:00', '17:10:00', '18:00:00', '18:10:00', '19:00:00', '19:10:00', '20:00:00');

UPDATE race SET time = '00:00:00' 
WHERE time NOT IN ('03:00:00', '04:30:00', '05:00:00', '05:10:00', '06:00:00', '06:10:00', '07:00:00', '08:00:00', '09:00:00', '09:30:00', '10:10:00', '11:00:00', '11:10:00', '11:30:00', '12:00:00', '12:10:00', '13:00:00', '13:10:00', '14:00:00', '14:10:00', '14:30:00', '15:00:00', '15:10:00', '16:00:00', '17:00:00', '17:10:00', '18:00:00', '18:10:00', '19:00:00', '19:10:00', '20:00:00');

ALTER TABLE `race` CHANGE `time` `time` TIME NOT NULL;

# Tabla result
SELECT * FROM result; -- Devuelve 24960 registros

SELECT DISTINCT * FROM result; -- Devuelve 24960 registros, no hay registros duplicados

SELECT DISTINCT resultId FROM result; -- Devuelve 24960 registros, no hay Id duplicados

ALTER TABLE `result` CHANGE `resultId` `resultId` INT NOT NULL;
ALTER TABLE `result` CHANGE `raceId` `raceId` INT NOT NULL;
ALTER TABLE `result` CHANGE `driverId` `driverId` INT NOT NULL;
ALTER TABLE `result` CHANGE `constructorId` `constructorId` INT NOT NULL;
ALTER TABLE `result` CHANGE `number` `number` INT NOT NULL;
ALTER TABLE `result` CHANGE `grid` `grid` INT NOT NULL;
ALTER TABLE `result` CHANGE `position` `position` INT NOT NULL; -- Hay valores '\N' en el campo, se imputaran estos a 0

SELECT DISTINCT position
FROM result
ORDER BY position;

SELECT DISTINCT position 
FROM result
WHERE position NOT IN ('1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '3', '30', '31', '32', '33', '4', '5', '6', '7', '8', '9');

UPDATE result
SET position = '0'
WHERE position NOT IN ('1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '3', '30', '31', '32', '33', '4', '5', '6', '7', '8', '9');

ALTER TABLE `result` CHANGE `position` `position` INT NOT NULL;
ALTER TABLE `result` CHANGE `positionOrder` `positionOrder` INT NOT NULL;
ALTER TABLE `result` CHANGE `position` `position` INT NOT NULL;
ALTER TABLE `result` CHANGE `points` `points` DECIMAL(6,2) NOT NULL;
ALTER TABLE `result` CHANGE `laps` `laps` INT NOT NULL;
ALTER TABLE `result` CHANGE `statusId` `statusId` INT NOT NULL;

# Asignacion de PRIMARY KEY en las tablas
ALTER TABLE `circuit` ADD PRIMARY KEY(`circuitId`);
ALTER TABLE `constructor` ADD PRIMARY KEY(`constructorId`);
ALTER TABLE `driver` ADD PRIMARY KEY(`driverId`);
ALTER TABLE `race` ADD PRIMARY KEY(`raceId`);
ALTER TABLE `result` ADD PRIMARY KEY(`resultId`);

# Asignacion de FOREGIN KEY en las tablas
ALTER TABLE `pit_stop` ADD FOREIGN KEY(raceId) REFERENCES race (raceId);
ALTER TABLE `pit_stop` ADD FOREIGN KEY(driverId) REFERENCES driver (driverId);
ALTER TABLE `race` ADD FOREIGN KEY(circuitId) REFERENCES circuit (circuitId);
ALTER TABLE `result` ADD FOREIGN KEY(raceId) REFERENCES race (raceId);
ALTER TABLE `result` ADD FOREIGN KEY(driverId) REFERENCES driver (driverId);
ALTER TABLE `result` ADD FOREIGN KEY(constructorId) REFERENCES constructor (constructorId);




