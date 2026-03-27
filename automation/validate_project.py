import os
import sys
import cssutils
from pathlib import Path
import logging
from bs4 import BeautifulSoup

errors = []
directorio_base = Path(__file__).resolve()
directorio_raiz = directorio_base.parent.parent
ruta_css = directorio_base / "src"/ "styles.css"
ruta_html = directorio_base / "src" / "index.html"
cssutils.log.setLevel(logging.WARNING)

def validacionCss(ruta_archivo):
    print(f"Errores encontrados en : {ruta_archivo}")
    errores = []
    class erroresCapturados(logging.Handler):
        def emit(self,record):
            errores.append(record.getMessage())
    handler = erroresCapturados()
    cssutils.log.addHandler(handler)
    cssutils.log.setLevel(logging.DEBUG)
    try:
        parser = cssutils.CSSParser(validate=True)
        sheet = parser.parseFile(ruta_archivo)
        tieneFontFamily = False
        for rule in sheet:
            if rule.type == rule.STYLE_RULE:
                for property in rule.style:
                    if "font-family" in rule.style:
                        tieneFontFamily = True
                        break
        if tieneFontFamily:
            print("Si se encontro una regla Font-Family")
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
    return errores


if not os.path.exists("src/index.html"):
    errors.append("No se encontró src/index.html")

if not os.path.exists("src/styles.css"):
    errors.append("No se encontró src/styles.css")

if os.path.exists(ruta_css):
    erroresCss = validacionCss(ruta_css)
    errors.extend(erroresCss)

if not os.path.exists("README.md") or os.path.getsize("README.md") == 0:
    errors.append("README.md no existe o está vacío")

try:
        # Se intenta abrir y leer el contenido del HTML
        with open(ruta_html, 'r', encoding='utf-8') as html:
            contenido = html.read()
        
        # Se crea el objeto 'soup' para analizar el HTML
        soup = BeautifulSoup(contenido, 'html.parser')
        
        # Se buscan las etiquetas h1 y p. Estas se guardarán en una lista.
        etiquetas_h1 = soup.find_all('h1')
        etiquetas_p = soup.find_all('p')
        
        # LÓGICA DE VALIDACIÓN
        # Se verifica la longitud de las listas encontradas. Las variables declaradas tendrán valor 'false' en caso de que no haya al menos una etiqueta de ese tipo.
        tiene_h1 = len(etiquetas_h1) >= 1
        tiene_p = len(etiquetas_p) >= 1
        
        #Si el valor es 'true', la validación tiene éxito. De otra forma, mostrará el error e indicará fallo para el CI al terminar el proceso con código 1.
        if tiene_h1 and tiene_p:
            print("✅ Validación exitosa: El archivo cumple los requisitos.")
        else:
            print("❌ Error de validación: Faltan etiquetas obligatorias.")
            if not tiene_h1: print("   Falta al menos un <h1>")
            if not tiene_p: print("   Falta al menos un <p>")
except Exception as e:
    print("¡Ups! Hubo un error, pero no sabemos cuál es...")
    errors.append(str(e))


if errors:
    print("Errores encontrados:")
    for error in errors:
        print("-", error)
    sys.exit(1)
else:
    print("Proyecto validado correctamente")