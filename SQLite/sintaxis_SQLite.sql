/*
Ejemplos de sintaxis basica de SQL con SQLite
*/


-- Crear una tabla
CREATE TABLE nombre_de_tabla (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    columna1 TIPO,
    columna2 TIPO,
    ...
);

-- Insertar datos en la tabla
INSERT INTO nombre_de_tabla (columna1, columna2, ...)
VALUES (valor1, valor2, ...);

-- Seleccionar todos los registros
SELECT * FROM nombre_de_tabla;

-- Seleccionar con condición
SELECT columna1, columna2
FROM nombre_de_tabla
WHERE condición;

-- Actualizar uno o varios campos
UPDATE nombre_de_tabla
SET columna1 = valor1, columna2 = valor2
WHERE condición;

-- Eliminar registros
DELETE FROM nombre_de_tabla
WHERE condición;

-- Ordenar resultados
SELECT * FROM nombre_de_tabla
ORDER BY columna1 ASC;   -- También puede ser DESC para descendente

-- Buscar texto parcialmente (como 'contiene')
SELECT * FROM nombre_de_tabla
WHERE columna1 LIKE '%texto%';

-- Limitar cantidad de resultados
SELECT * FROM nombre_de_tabla
LIMIT 10;

-- Contar registros
SELECT COUNT(*) FROM nombre_de_tabla;

-- Cambiar nombre de una tabla
ALTER TABLE nombre_de_tabla RENAME TO nuevo_nombre;

-- Agregar una nueva columna
ALTER TABLE nombre_de_tabla ADD COLUMN nueva_columna TIPO;

-- Borrar todos los datos (sin eliminar la tabla)
DELETE FROM nombre_de_tabla;

-- Eliminar una tabla completamente
DROP TABLE nombre_de_tabla;
