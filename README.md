# Propuesta Proyecto

# CSV Cleaner: Validador y limpiador automático de archivos CSV

Este proyecto permite validar y limpiar automáticamente archivos CSV, eliminando filas con errores comunes (campos vacíos, duplicados, filas incompletas) y generando un reporte de limpieza.

## ¿Qué hace?
- Detecta y elimina filas incompletas o con celdas vacías.
- Elimina filas duplicadas.
- Genera un archivo limpio (`data_clean.csv`).
- Crea un reporte de validación (`reporte_validacion.txt`).

## Cómo usar

### Localmente:
```bash
bash run_cleaner.sh

### Estructura
csv-cleaner/
├── data/
│   └── sample.csv
├── cleaned_data/
│   └── (aquí se guardará el archivo limpio)
├── run_cleaner.sh
├── clean_csv.py
├── Dockerfile
├── README.md
└── report/
    └── reporte_validacion.txt
