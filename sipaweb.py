"""
# Archivo: sipaweb.py  -- main, punto de acceso a sipaweb
# Autor: Daniel Miñana Montero
# Versión: Prototipo
# Descripción: sipaweb como gestor de la publicación online de la 
# web personal del autor, se ha seleccionado github pages.
# Este script actúa como el 'conector' principal de SIPAweb. 
# Su función inicial es procesar la lógica de presentación y 
# preparar la integración con SIPA_PROJECT.
"""

import markdown
from jinja2 import Environment, FileSystemLoader
import os

class SipaWebBuilder:
    """
    Clase maestra encargada de orquestar la generación del sitio SIPAweb.
    
    Esta clase gestiona las rutas, la carga de datos y la transformación
    de archivos Markdown en una estructura web profesional.
    """

    def __init__(self, usuario="Daniel"):
        """
        Inicializa la instancia del constructor.

        Args:
            usuario (str): Nombre del propietario del proyecto.
        """
        self.usuario = usuario
        self.version = "1.0.0"
        self.raiz_proyecto = os.path.dirname(os.path.abspath(__file__))

        # CAMBIO CLAVE: Nueva ruta para el contenido de la landing page
        self.ruta_static_content = os.path.join(self.raiz_proyecto, "templates", "static")
        self.ruta_templates = os.path.join(self.raiz_proyecto, "templates")

        # Inicializar Jinja2
        self.env = Environment(loader=FileSystemLoader(self.ruta_templates))
        
    def leer_markdown_nativo(self, nombre_fichero):
        """
        Lee un archivo Markdown y separa el Frontmatter del contenido.
        """
        ruta_completa = os.path.join(self.ruta_static_content, nombre_fichero)
        
        try:
            with open(ruta_completa, 'r', encoding='utf-8') as f:
                contenido_total = f.read()

            # Dividimos usando los '---' como separadores
            # El 2 indica que solo rompa en las primeras dos ocurrencias
            partes = contenido_total.split('---', 2)

            if len(partes) >= 3:
                # Metadatos están en partes[1], el cuerpo en partes[2]
                meta_raw = partes[1].strip()
                cuerpo = partes[2].strip()
                
                # Convertimos el bloque de texto meta en un diccionario
                metadatos = {}
                for linea in meta_raw.split('\n'):
                    if ":" in linea:
                        clave, valor = linea.split(":", 1)
                        # Limpiamos posibles comillas de los valores en el YAML
                        metadatos[clave.strip()] = valor.strip().strip('"').strip("'")
                
                return metadatos, cuerpo
            else:
                return {}, contenido_total # No hay frontmatter

        except FileNotFoundError:
            return None, "Error: Archivo no encontrado {ruta_completa}."

    def renderizar_index(self, metadatos, cuerpo_html):
        """
        Une los datos con la plantilla base.html y genera el index.html final.
        """
        template = self.env.get_template('base.html')
        # Añadimos el usuario por defecto si no viene en los meta
        if 'usuario' not in metadatos:
            metadatos['usuario'] = self.usuario
        return template.render(**metadatos, contenido=cuerpo_html)

    def generar_sitio(self, nombre_md="index.md"):
        """
        Orquesta la lectura, transformación y escritura del sitio.
        """
        # 1. Leer datos nativos
        meta, cuerpo_md = self.leer_markdown_nativo(nombre_md)

        if meta is None:
            return cuerpo_md # Retorna el error de archivo no encontrado
        
        # 2. Convertir cuerpo Markdown a HTML real
        # Vitaminamos el HTML con las extensiones que instalamos
        cuerpo_html = markdown.markdown(cuerpo_md, extensions=[
            'extra', 
            'admonition', 
            'codehilite', 
            'pymdownx.magiclink'
        ])
        
        # 3. Renderizar con Jinja2
        html_final = self.renderizar_index(meta, cuerpo_html)
        
        # 4. Escritura física del archivo
        ruta_index = os.path.join(self.raiz_proyecto, "index.html")
        with open(ruta_index, "w", encoding="utf-8") as f:
            f.write(html_final)
        
        return f"Éxito: {ruta_index} generado correctamente desde {nombre_md} ."

# Bloque de ejecución principal
# Bloque de ejecución principal
if __name__ == "__main__":
    print("--- SIPAweb Builder: Iniciando Orquestación ---")
    
    # 1. Instancia única
    app = SipaWebBuilder("Daniel")
    
    # 2. Intentamos leer el archivo estratégico
    # IMPORTANTE: Asegúrate de que el archivo esté en /SIPAweb/templates/static/index.md
    meta, texto = app.leer_markdown_nativo("index.md")
    
    if meta:
        print(f"[*] Lectura Correcta: {meta.get('titulo')}")
        
        # 3. Generación del sitio
        estado = app.generar_sitio("index.md")
        print(f"[!] {estado}")
    else:
        # Si entra aquí, el error impreso en 'texto' nos dirá la RUTA EXACTA que falló
        print(f"[X] Error en lectura: {texto}")
    
    print("--- Sesión finalizada con éxito ---")