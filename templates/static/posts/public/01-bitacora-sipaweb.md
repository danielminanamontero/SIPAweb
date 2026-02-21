---
titulo: Bitácora de Desarrollo SIPAweb
subtitulo: Del Caos de Rutas al Motor Editorial Inteligente
estado: proceso
fecha_creacion: 2026-02-20
fecha_publicacion: pendiente
tag: python, jinja2, arquitectura, devlog
tipo: post
autor: Daniel Miñana
---  

# Introducción

Este documento registra el proceso de metamorfosis de SIPAweb, desde un conjunto de scripts dispersos hasta convertirse en un orquestador capaz de generar su propia documentación técnica.

La filosofía del proyecto se basa en la "Metadocumentación": el código no solo funciona, sino que explica cómo funciona a través de un motor editorial integrado.

## Hitos de la Arquitectura (Timeline)

| Fecha | Hito Técnico | Cambio en el Código |
| :--- | :--- | :--- |
| **20/02 - 13:28** | **Génesis de la Estructura** | Definición de `data/process` y `data/public` para separar borradores de publicaciones. |
| **20/02 - 16:30** | **El Motor Editorial** | Creación de la clase `SipaFilePost` heredando de `SipaModule` para asegurar integridad SHA-256. |
| **21/02 - 11:00** | **Identidad Visual 10vh** | Rediseño del header al 10% de altura y fijación del menú para lectura técnica. |
| **21/02 - 15:45** | **TOC & Code Blocks** | Implementación de extracción automática de índices y bloques de código colapsables. |

## Desarrollo Técnico: El Motor de Posts

El corazón de esta fase fue la clase `SipaFilePost`. A diferencia de las páginas básicas, esta clase debe "colonizar" el sistema de archivos si lo encuentra vacío.

### Lógica de Provisión de Semillas

Para evitar errores de "Carpeta no encontrada", el sistema genera automáticamente un ejemplo si detecta el laboratorio vacío:

```python
def provision(self):
    """Asegura carpetas y crea el post de ejemplo (Semilla)."""
    os.makedirs(self.public_folder, exist_ok=True)
    os.makedirs(self.output_folder, exist_ok=True)
    if not os.listdir(self.public_folder):
        # Escribe el boilerplate del post...
```

- El Desafío del Scroll y el TOC
  - Uno de los puntos más críticos fue la creación del menú dinámico. Se decidió simplificar al máximo para evitar errores de renderizado en Jinja2, delegando el peso al CSS mediante clases de nivel.

```css
.toc-nivel-1 { margin-left: 0; font-weight: bold; }
.toc-nivel-2 { margin-left: 1rem; }
```

- Conclusiones del Ciclo
  - Independencia de Contenidos: La producción web (páginas core) ahora es independiente de la producción editorial (posts), permitiendo escalabilidad.
  - Usabilidad: El uso de \<details> para el código mantiene la limpieza visual sin perder profundidad técnica.
  - Integridad: Cada post generado pasa por la auditoría de SipaModule, garantizando que el archivo publicado coincide con su origen.

- Cierre
  - Sistema estabilizado. El motor está listo para recibir contenido de SIPAcurator.

```markdown

### Qué esperar al publicarlo
1.  **Columna Izquierda:** Mostrará los metadatos (Daniel Miñana, Estado: Publicado, Tema: Arquitectura) y el menú de navegación que se generará solo al leer los `#` del texto.
2.  **Columna Derecha:** Verás la tabla cronológica limpia y los bloques de código que hemos discutido, todos bajo el nuevo header del 10%.

**¡Buen provecho con ese café!** Avísame cuando lo tengas en el navegador para ajustar ese detalle del "summary" del código que querías hacer más sutil.

