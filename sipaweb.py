import markdown
from jinja2 import Environment, FileSystemLoader
import os
import hashlib
import json
import shutil
from datetime import datetime

class SipaModule:
    """CLASE BASE SENTINEL: Gestión de Integridad y Provisión."""
    def __init__(self, page_name, base_path):
        self.page_name = page_name
        self.base_path = base_path
        self.manifest_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "manifest.json")
        self.file_path = os.path.join(self.base_path, f"{page_name}.md")
        self.folder_path = os.path.join(self.base_path, page_name)

    def _get_hash(self, data):
        return hashlib.sha256(data).hexdigest()

    def calculate_hashes(self):
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
        manifest = {}
        if os.path.exists(self.manifest_path):
            with open(self.manifest_path, "r") as f: manifest = json.load(f)
        f_h, d_h = self.calculate_hashes()
        manifest[self.page_name] = {"file_hash": f_h, "dir_hash": d_h, "last": datetime.now().isoformat()}
        with open(self.manifest_path, "w") as f: json.dump(manifest, f, indent=4)

class SipaFileIndex(SipaModule):
    """CLASE ESPECÍFICA: Creadora de contenido para el Index."""
    def provision(self):
        """Si no existen los ficheros, los crea con el estándar SIPA."""
        # 1. Crear el index.md principal
        if not os.path.exists(self.file_path):
            os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
            content = (
                "---\n"
                "titulo: SIPA Identity\n"
                "rol: FullStack & Cybersecurity\n"
                "subtitulo: SIPA Identity\n"
                "experiencia: +20 años\n"
                "perfil_a: Mimod Bland\n"
                "perfil_b: Tovid Dfrei\n"
                "estado: Protegido\n"
                "tag: Core\n"
                "---\n"
                "# Bienvenido a SIPAweb\n"
                "\n"
                "Este es el núcleo de tu identidad digital generado automáticamente."
            )
            with open(self.file_path, "w", encoding="utf-8") as f: f.write(content)
            print(f"[*] Creado: {self.file_path}")

        # 2. Crear carpeta de bloques y un bloque de ejemplo
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
                "# BLOQUE NOMBRE\n"
                "\n"
                "Implementación de integridad basada en hashing SHA-256."
            )
            with open(bloque_path, "w", encoding="utf-8") as f: f.write(bloque_content)
            print(f"[*] Creado bloque: {bloque_path}")

class SipaWebBuilder:
    def __init__(self, usuario="Daniel"):
        self.usuario = usuario
        self.raiz = os.path.dirname(os.path.abspath(__file__))
        self.static = os.path.join(self.raiz, "templates", "static")
        self.templates = os.path.join(self.raiz, "templates")
        
        # 1. Asegurar base.html desde Core/Assets
        self.asegurar_base_html()
        
        # 2. Inicializar Entorno
        self.env = Environment(loader=FileSystemLoader(self.templates))
        self.index_manager = SipaFileIndex("index", self.static)

    def asegurar_base_html(self):
        """Si no existe base.html en templates, lo restaura desde core/assets."""
        destino = os.path.join(self.templates, "base.html")
        origen = os.path.join(self.raiz, "core", "assets", "base.html")
        if not os.path.exists(destino):
            try:
                os.makedirs(self.templates, exist_ok=True)
                shutil.copy2(origen, destino)
                print("[*] Provisión: base.html restaurado desde core/assets/")
            except Exception as e:
                print(f"[X] Error crítico: No se pudo proveer base.html: {e}")

    def leer_markdown_nativo(self, ruta_relativa):
        """Lector de Markdown con separación de Frontmatter."""
        ruta_completa = os.path.join(self.static, ruta_relativa)
        try:
            with open(ruta_completa, 'r', encoding='utf-8') as f:
                contenido = f.read()
            partes = contenido.split('---', 2)
            if len(partes) >= 3:
                meta_raw = partes[1].strip()
                cuerpo = partes[2].strip()
                metadatos = {l.split(":",1)[0].strip(): l.split(":",1)[1].strip().strip('"') 
                            for l in meta_raw.split('\n') if ":" in l}
                return metadatos, cuerpo
            return {}, contenido
        except Exception as e:
            return None, str(e)

    def build(self):
        print(f"--- SIPAweb Builder v1.3 | Producción Activa ---")
        
        # A. Provisión y Auditoría
        self.index_manager.provision()
        ok, msg = self.index_manager.verify_integrity()
        print(f"[BOLARDO] Estatus: {msg}")

        # B. Carga de Bloques (Dinamismo Bento Grid)
        bloques_data = []
        folder_bloques = self.index_manager.folder_path
        if os.path.exists(folder_bloques):
            for f in sorted(os.listdir(folder_bloques)):
                if f.endswith(".md"):
                    meta_b, texto_b = self.leer_markdown_nativo(os.path.join("index", f))
                    if meta_b:
                        html_b = markdown.markdown(texto_b)
                        bloques_data.append({**meta_b, "contenido": html_b})
            print(f"[*] Bloques procesados: {len(bloques_data)}")

        # C. Carga de Index Principal
        meta_main, cuerpo_md = self.leer_markdown_nativo("index.md")
        html_main = markdown.markdown(cuerpo_md, extensions=['extra', 'admonition'])

        # D. Renderizado y Escritura
        try:
            template = self.env.get_template('base.html')
            # Inyección de todos los datos en la plantilla de Daniel
            html_final = template.render(
                **meta_main, 
                contenido=html_main, 
                bloques=bloques_data
            )
            
            ruta_index = os.path.join(self.raiz, "index.html")
            with open(ruta_index, "w", encoding="utf-8") as f:
                f.write(html_final)
            
            # E. Registro Final de Confianza
            self.index_manager.update_manifest()
            print(f"[!] ÉXITO: {ruta_index} generado y auditado.")
            
        except Exception as e:
            print(f"[X] Error en Renderizado: {e}")

if __name__ == "__main__":
    SipaWebBuilder().build()