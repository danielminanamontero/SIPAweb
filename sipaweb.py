"""
SIPAweb Builder v1.3
--------------------
Motor de generación estática con auditoría de integridad SHA-256.
Especializado en la gestión de Identidad Digital (Hito 2A).
"""

import markdown
from jinja2 import Environment, FileSystemLoader
import os
import hashlib
import json
import shutil
from datetime import datetime

class SipaModule:
    """
    CLASE BASE BOLARDO: Gestión de Integridad y Provisión.
    Vigila la constancia de los archivos mediante hashing.
    """
    def __init__(self, page_name, base_path):
        self.page_name = page_name
        self.base_path = base_path
        self.manifest_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "manifest.json")
        self.file_path = os.path.join(self.base_path, f"{page_name}.md")
        self.folder_path = os.path.join(self.base_path, page_name)

    def _get_hash(self, data):
        """Genera firma SHA-256."""
        return hashlib.sha256(data).hexdigest()

    def calculate_hashes(self):
        """Calcula hashes para el archivo principal y la carpeta de bloques."""
        f_hash = None
        if os.path.exists(self.file_path):
            with open(self.file_path, "rb") as f: f_hash = self._get_hash(f.read())
        
        d_hash = None
        if os.path.exists(self.folder_path):
            hashes = []
            for root, _, files in os.walk(self.folder_path):
                for f in sorted(files):
                    if f.endswith(".md"):
                        with open(os.path.join(root, f), "rb") as bf:
                            hashes.append(self._get_hash(bf.read()))
            if hashes: d_hash = self._get_hash("".join(hashes).encode())
        
        return f_hash, d_hash

    def verify_integrity(self):
        """Compara el estado actual con el registro en manifest.json."""
        try:
            if not os.path.exists(self.manifest_path): return False, "NUEVO_ENTORNO"
            with open(self.manifest_path, "r") as f: manifest = json.load(f)
            record = manifest.get(self.page_name, {})
            curr_f, curr_d = self.calculate_hashes()
            if record.get("file_hash") != curr_f: return False, "FILE_CHANGED"
            if record.get("dir_hash") != curr_d: return False, "DIR_CHANGED"
            return True, "OK"
        except: return False, "ERROR"

    def update_manifest(self):
        """PASO CRÍTICO: Actualiza el .json con los nuevos hashes tras el build."""
        manifest = {}
        if os.path.exists(self.manifest_path):
            with open(self.manifest_path, "r") as f: manifest = json.load(f)
        f_h, d_h = self.calculate_hashes()
        manifest[self.page_name] = {"file_hash": f_h, "dir_hash": d_h, "last": datetime.now().isoformat()}
        with open(self.manifest_path, "w") as f: json.dump(manifest, f, indent=4)

class SipaFileIndex(SipaModule):
    """
    CLASE ESPECÍFICA: Creadora de contenido para el Index.
    Mantiene tu lógica de provisión de bloques Bento.
    """
    def provision(self):
        """Si no existen los ficheros, los crea con el estándar SIPA (Recuperado)."""
        # 1. Crear el index.md principal (Tu estructura original)
        if not os.path.exists(self.file_path):
            os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
            content = (
                "---\n"
                "titulo: SIPA Identity\n"
                "nombre_sito: Nombre del Sitio\n"
                "rol: FullStack & Cybersecurity\n"
                "subtitulo: SIPA Identity\n"
                "experiencia: +20 años\n"
                "perfil_a: Mimod Bland\n"
                "perfil_b: Tovid Dfrei\n"
                "estado: Protegido\n"
                "tag: Core\n"
                "---\n"
                "# Bienvenido a SIPAweb\n\n"
                "Este es el núcleo de tu identidad digital generado automáticamente."
            )
            with open(self.file_path, "w", encoding="utf-8") as f: f.write(content)

        # 2. Crear carpeta de bloques y ejemplo de seguridad (Tu estructura original)
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path, exist_ok=True)
            bloque_path = os.path.join(self.folder_path, "01_seguridad.md")
            bloque_content = (
                "---\n"
                "id: bloque_nombre\n"
                "icono: ph-shield-check\n"
                "titulo: FHS Cybersecurity\n"
                "enlace: '#'\n"
                "orden: 1\n"
                "estado: Auditado\n"
                "tag: Seguridad\n"
                "---\n"
                "# BLOQUE NOMBRE\n\n"
                "Implementación de integridad basada en hashing SHA-256."
            )
            with open(bloque_path, "w", encoding="utf-8") as f: f.write(bloque_content)

class SipaWebBuilder:
    """
    ORQUESTADOR: Provisión de activos core, lectura de MD y renderizado.
    """
    def __init__(self, usuario="Daniel"):
        self.raiz = os.path.dirname(os.path.abspath(__file__))
        self.static = os.path.join(self.raiz, "templates", "static")
        self.templates = os.path.join(self.raiz, "templates")
        
        # Sincronización de activos (base.html y custom.css)
        self.asegurar_activos_core()
        
        self.env = Environment(loader=FileSystemLoader(self.templates))
        self.index_manager = SipaFileIndex("index", self.static)

    def asegurar_activos_core(self):
        """
        Sincroniza activos desde core/assets a sus destinos de producción.
        Detecta subcarpetas en el origen para evitar errores de 'File Not Found'.
        """
        # Mapeo: (Subruta_Origen, Nombre_Fichero, Carpeta_Destino)
        activos = [
            ("", "base.html", self.templates),
            ("", "custom.css", os.path.join(self.raiz, "css")),
            ("img", "avatargithub.png", os.path.join(self.raiz, "img")) # Subcarpeta 'img'
        ]
        
        for subfolder, nombre, destino_folder in activos:
            # Construimos la ruta de origen entrando en la subcarpeta si existe
            origen = os.path.join(self.raiz, "core", "assets", subfolder, nombre)
            destino = os.path.join(destino_folder, nombre)
            
            if os.path.exists(origen):
                os.makedirs(destino_folder, exist_ok=True)
                shutil.copy2(origen, destino)
                # print(f"[*] Sincronizado: {nombre} -> {destino_folder}")
            else:
                print(f"[X] ERROR: No se encuentra el origen real: {origen}")

    def leer_markdown_nativo(self, ruta_relativa):
        """Lector de Markdown con separación de Frontmatter (Tu método funcional)."""
        ruta_completa = os.path.join(self.static, ruta_relativa)
        try:
            with open(ruta_completa, 'r', encoding='utf-8') as f:
                contenido = f.read()
            partes = contenido.split('---', 2)
            if len(partes) >= 3:
                meta_raw = partes[1].strip()
                metadatos = {l.split(":",1)[0].strip(): l.split(":",1)[1].strip().strip('"') 
                            for l in meta_raw.split('\n') if ":" in l}
                return metadatos, partes[2].strip()
            return {}, contenido
        except: return {}, ""

    def build(self):
        """Ciclo de construcción: Provisión -> Auditoría -> Renderizado."""
        print(f"--- SIPAweb Builder v1.3 | Producción Activa ---")
        self.index_manager.provision()
        ok, msg = self.index_manager.verify_integrity()
        print(f"[BOLARDO] Estatus: {msg}")

        # Procesar bloques Bento
        bloques_data = []
        if os.path.exists(self.index_manager.folder_path):
            for f in sorted(os.listdir(self.index_manager.folder_path)):
                if f.endswith(".md"):
                    meta_b, texto_b = self.leer_markdown_nativo(os.path.join("index", f))
                    if meta_b:
                        bloques_data.append({**meta_b, "contenido": markdown.markdown(texto_b)})

        # Procesar Index y Renderizar
        meta_main, cuerpo_md = self.leer_markdown_nativo("index.md")
        html_main = markdown.markdown(cuerpo_md, extensions=['extra', 'admonition'])

        try:
            template = self.env.get_template('base.html')
            html_final = template.render(**meta_main, contenido=html_main, bloques=bloques_data)
            with open(os.path.join(self.raiz, "index.html"), "w", encoding="utf-8") as f:
                f.write(html_final)
            
            self.index_manager.update_manifest()
            print(f"[!] ÉXITO: Generado y auditado con SHA-256.")
        except Exception as e:
            print(f"[X] Error en Renderizado: {e}")

if __name__ == "__main__":
    SipaWebBuilder().build()