import os
import sys

errors = []

if not os.path.exists("src/index.html"):
    errors.append("No se encontró src/index.html")

if not os.path.exists("src/styles.css"):
    errors.append("No se encontró src/styles.css")

if not os.path.exists("README.md") or os.path.getsize("README.md") == 0:
    errors.append("README.md no existe o está vacío")

if errors:
    print("Errores encontrados:")
    for error in errors:
        print("-", error)
    sys.exit(1)
else:
    print("Proyecto validado correctamente")