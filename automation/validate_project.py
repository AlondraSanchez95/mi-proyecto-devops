import os
import sys
import cssutils
from pathlib import Path
import logging

errors = []
directorio_base = Path(__file__).resolve().parent
ruta_css = directorio_base / "styles.css"
cssutils.log.setLevel(logging.WARNING)

def validacionCss(ruta_archivo):
    print(f"Errores encontrados en : {ruta_archivo}")
    errores = []
    class erroresCapturados(logging.Handler):
        def emit(self,record):
            errores.append(record.getMessage())
    handler = erroresCapturados()
    cssutils.log.addHandler(handler)
    try:
        sheet = cssutils.parseFile(ruta_archivo)
        sheet.validate()
        if not errores:
            print("Sin ningun error :)")
        else:
            print(f"Se encontraron {len(errores)} problemas :(")
            for err in errores:
                print(err)
    except Exception as e:
        print(f"Error al intentar abrir el archivo {e}")
    finally:
        cssutils.log.removeHandler(handler)

if not os.path.exists("src/index.html"):
    errors.append("No se encontró src/index.html")

if not os.path.exists("src/styles.css"):
    errors.append("No se encontró src/styles.css")

if not os.path.exists("README.md") or os.path.getsize("README.md") == 0:
    errors.append("README.md no existe o está vacío")

if html.count("<h1>") < 1:
    errors.append("index.html debe contener un h1")

if html.count("<p>") < 1:
    errors.append("index.html debe contener al menos un párrafo")

validacionCss(ruta_css)
if errors:
    print("Errores encontrados:")
    for error in errors:
        print("-", error)
    sys.exit(1)
else:
    print("Proyecto validado correctamente")