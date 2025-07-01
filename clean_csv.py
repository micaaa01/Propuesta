import csv
import sys
import os
#Validador y limpiador
#Un pequeño ejemplo de código podría ser el siguiente
INPUT_PATH = "data/sample.csv"
OUTPUT_PATH = "cleaned_data/data_clean.csv"
REPORT_PATH = "report/reporte_validacion.txt"

def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def clean_csv(input_path, output_path, report_path):
    with open(input_path, 'r', encoding='utf-8') as infile:
        reader = list(csv.reader(infile))
        headers = reader[0]
        rows = reader[1:]

    cleaned = []
    removed_rows = 0
    empty_cells = 0
    duplicates = set()
    unique_rows = []

    for row in rows:
        if len(row) != len(headers) or "" in row:
            removed_rows += 1
            empty_cells += row.count("")
            continue
        row_tuple = tuple(row)
        if row_tuple in duplicates:
            removed_rows += 1
            continue
        duplicates.add(row_tuple)
        unique_rows.append(row)

    # Escribir archivo limpio
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(headers)
        writer.writerows(unique_rows)

    # Generar reporte
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    with open(report_path, 'w', encoding='utf-8') as report:
        report.write(f"Archivo original: {input_path}\n")
        report.write(f"Total de filas originales: {len(rows)}\n")
        report.write(f"Filas eliminadas: {removed_rows}\n")
        report.write(f"Celdas vacías encontradas: {empty_cells}\n")
        report.write(f"Filas finales: {len(unique_rows)}\n")

    print(f"[✔] Limpieza completada. Archivo guardado en: {output_path}")
    print(f"[📝] Reporte generado en: {report_path}")

if __name__ == "__main__":
    clean_csv(INPUT_PATH, OUTPUT_PATH, REPORT_PATH)
