# 🧹 limpiador-csv-ia

Herramienta desarrollada en Python 3 y pandas para limpiar y organizar archivos CSV de ventas de forma automática, mejorando la calidad y consistencia de los datos.

## 📌 Descripción

**limpiador-csv-ia** permite procesar archivos CSV de ventas que contienen datos desordenados o inconsistentes. El programa normaliza la información, elimina registros duplicados y detecta valores faltantes para obtener un archivo limpio y listo para su análisis.

El resultado del procesamiento se guarda automáticamente en `ventas_limpias.csv`.

## ⚙️ Funciones principales

- **Unificación de clientes:** normaliza los nombres de los clientes para mantener un formato consistente.
- **Conversión de precios:** transforma los precios al formato numérico correcto.
- **Conversión de fechas:** estandariza las fechas para facilitar su interpretación y análisis.
- **Eliminación de duplicados:** identifica y elimina filas repetidas.
- **Detección de datos faltantes:** muestra la cantidad de valores ausentes en el archivo.
- **Exportación de resultados:** genera un nuevo archivo llamado `ventas_limpias.csv` con los datos procesados.

## 🛠️ Tecnologías utilizadas

- Python 3
- pandas

## 📋 Requisitos

Para ejecutar el proyecto necesitas:

- Python 3 instalado.
- pip (gestor de paquetes de Python).
- Los archivos del proyecto.

## 📥 Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/USUARIO/limpiador-csv-ia.git
   ```

2. Ingresa a la carpeta del proyecto:

   ```bash
   cd limpiador-csv-ia
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Cómo usarlo

Ejecuta el siguiente comando desde la terminal, dentro de la carpeta del proyecto:

```bash
python limpiar_ventas.py ventas_practica.csv
```

El programa procesará el archivo CSV, realizará las tareas de limpieza y generará el archivo:

```text
ventas_limpias.csv
```

## 📂 Estructura del proyecto

```text
limpiador-csv-ia/
│
├── limpiar_ventas.py
├── ventas_practica.csv
├── requirements.txt
└── README.md
```

## 📊 Ejemplo del resultado

**Antes de la limpieza:**

| Cliente | Precio | Fecha |
|---|---:|---|
| juan perez | $1.500,00 | 15/02/2025 |
| Juan Perez | 1500 | 2025-02-15 |
| MARIA GOMEZ | $2.000,50 | 20/02/2025 |

**Después de la limpieza (ejemplo ilustrativo):**

| Cliente | Precio | Fecha |
|---|---:|---|
| Juan Perez | 1500.00 | 2025-02-15 |
| Maria Gomez | 2000.50 | 2025-02-20 |

Los registros duplicados se eliminan y los datos quedan estandarizados para su posterior análisis.

## 📄 Licencia

Este proyecto está disponible para fines educativos y de práctica. 
