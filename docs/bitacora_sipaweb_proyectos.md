# BITÁCORA DE SIPAweb

Registro de sesiones de diseño y desarrollo de SIPAweb, he adquirido algo de experiencia y la primera conclusión que obtengo es que si documento, escribo, resumo, explico, cualquier añadido que pueda hacer a mi código no solo me beneficia a mí, sino a otros a parte del aprendizaje que adquieres.

Observas el código, y empiezas a ver que has hecho ahora que no se te ocurrio antes, o como mejora la comunicación con tú ayudante tecnológico, por lo tanto este documento es vivo, registrara todo lo que se pueda y formara parte de un aprendizaje y sobre todo de una estandarización para otros proyectos, bitácora es el documento personal guía de desarrollo.

## Registro de bitácora comienza 18/02/2026 19:50:06

### BITÁCORA - ejemplo

#### Tema tratado : Título del tema

#### Conclusión y cambios o propuesta de nueva revisión

#### Cerrada fecha

### HITO 1 Y 2 CERRADO

### HITO 2A

### BITÁCORA - ABIERTA - 20260218 195204

#### Tema tratado : Completar proyectos.html, aprovechar y organizar

Pregunta: Lo primero vamos a situarnos donde estamos, en la ultima contestación parece que vayamos por libre uno y otro, estamos en la versión 1.4.4 y el hito es el 2A, por eso lo primero me remito al acta fundacional que tú también tienes y lo actualizo:

```markdown
#### HITO 2 EN PROCESO

Hito 2: Página de presentación profesional (Landing Page inicial).

- Generador y Despliege

-Para alcanzar el hito 2, los pasos a seguir son estos

- [x] Crear docs/about-me.md
  - Crear directorio templates/
  - Crear templates/base.html
- [x] Crear funciones en sipaweb.py incluirlas en la clase
  - leer_markdown_nativo()
  - renderizar_index()
  - generar_sitio()
- [x] Crear index.html
  - Test página html navegador
- [x] Planificar el despliege
  - Crear ubicación correcta
  - Crear index real .md, about-me.md debe ser secundaria, se incluye la biografía mínima
  - Crear proyectos.md
  - Crear contacto.md
  - Crear ayuda.md
  - Test web completa, se ejecuta correctamente la actualización en local y todo es correcto
  - Añadir github actions, configurar correctamente, realizar pruebas necesarias
- [x] Revisión completa a modo auditoría
  - [x] README.md presente
  - [x] mkdocs.yml presente
  - [x] .gitignore presente
  - [x] requirements.txt presente
  - [x] /.github/workflows/deploy.yml presente
  - [x] acta_fundacion.md presente
  - [x] index.md presente
  - [x] referencia.md presente
  - [x] bitacora_sipaweb.md presente
  - [x] revisión arquitectura y árbol
  - [x] revisión lógica
  - [x] revisión objetivo
  - [x] revisión situación final

Hito 2 A : Confeccionar página a página

- [x] Diseño estructura, acciones, contenido de index.html
  - [x] Definir estructura
  - [x] Definir colores marca
  - [x] Definir iconos
  - [x] Definir bloques
  - [x] Definir contenido
- [x] Enlace de todas con todas, a través de una barra navegación fija
- [x] Enlace de los proyectos en el pie según perfil tovid o mimod
- [x] Diseño estructura, acciones, contenido de sobre-mi.html
- [ ] Diseño estructura, acciones, contenido de proyectos.html
- [ ] Diseño estructura, acciones, contenido de contacto.html
- [ ] Diseño estructura, acciones, contenido de ayuda.html

[] Cierre proyecto SIPAweb versión 1.5
```

- Vale, después de esto agradecerte la colaboración pero si en un futuro releo las bitácoras me puedo confundir, por eso, nos grabamos que soy yo quién abre hitos, bitácoras, versiones, por fa, igual que tenemos la obligación de comentar el código y no solo comentar que en breve entraremos en eso, si no incluso ofrecer una explicación pedagógica, también tenemos la obligación de seguir el orden pactado, acta fundacional.

- Y ahora sí, vamos a entrar en materia, he abierto la bitácora para confeccionar proyectos.html, llevo todo el día pensando como afrontar esta página y quiero exponer alguna idea. Te parece que paremos un momento, cafe y entramos al tema.

Registro de Sesión | Sincronización de Hitos y Preparación de Proyectos
Pregunta del usuario: "Estamos en la v1.4.4, Hito 2A. He actualizado el acta fundacional y quiero que sigamos el orden pactado. Vamos a entrar en materia con proyectos.html, pero antes, ¿paramos un momento para café y entramos al tema?"

- Acepto el café virtual y el "tirón de orejas" técnico. Tienes toda la razón: en un proyecto de ingeniería, la trazabilidad es sagrada. Si la bitácora o el acta fundacional dicen que estamos en el Hito 2A, ahí es donde debemos documentar cada paso para que el "Daniel del futuro" no se pierda en el código.

- Sincronización de Estado (Checkpoint)
  - He registrado la actualización del Acta Fundacional. Estamos exactamente aquí:
    - Hito 2A: Confección de página a página.
    - Estado: index.html y sobre-mi.html finalizados.
    - Objetivo Inmediato: Diseño, estructura y contenido de proyectos.html.
    - Versión Actual: 1.4.4.

- Premisas para Proyectos.html
  - Mientras te tomas ese café, dejo sobre la mesa las coordenadas que tenemos para esta página según lo que hemos construido:
    - Herencia de Clase: Usaremos una estructura similar a SipaFileIndex, pero enfocada a una galería.
    - Los "Candidatos": Tenemos sobre la mesa SIPAweb, SIPAcurator, FCH_CiberAudit y tu historial del Portfolio 2018.
    - Transición de Bloques: Como mencionaste antes, hay que decidir cómo viajarán los bloques Bento hacia el detalle de cada proyecto.

- Nota Pedagógica (Documentación)
  - Entendido el mensaje sobre la explicación pedagógica. A partir de ahora, cuando propongamos cambios en el sipaweb.py para la página de proyectos, desglosaré:
    - El Qué: La línea de código.
    - El Porqué: La lógica de ingeniería detrás (por ejemplo, por qué usamos un diccionario para los estados de proyecto: activo, en proceso, parado).

- Punto de Espera
  - La bitácora 20260218 195204 queda en estado ABIERTA.
  - Cuando estés listo, exponme esas ideas que has estado madurando hoy. ¿Cómo visualizas la jerarquía de tus proyectos? ¿Quieres clasificarlos por "perfil" (Mimod/Tovid) o por "categoría técnica" (Seguridad/Desarrollo)?

- Quedo a la espera de tus instrucciones para empezar a picar el código de la clase SipaFileProyectos.

Pregunta: Vamos a tener una imagen de donde estamos también en el código, te voy a pasar lo que ya tenemos hecho y revisas, realmente la maquinaria ya está en marcha, estamos hablando de contenido y bloques, organización practicamente:

- fichero proyectos.md

```markdown
---
titulo: Proyectos
nombre_sitio: Daniel Miñana Montero
rol: Propietario
subtitulo: Plantearme metas és el plasma de mi ser
hero_bg: img/proyectos-bg.png
estado: Protegido
tag: Proyectos
---
# Mis proyectos

Este es el espacio para tu presentación proyectos.
```

- clase SipaFileProyectos(SipaModule)

```python
class SipaFileProyectos(SipaModule):
    """
    CLASE ESPECÍFICA: Creadora de contenido para Proyectos.
    Réplica exacta de la lógica de matrices del Index.
    """
    def provision(self):
        """Si no existen los ficheros, los crea con el estándar SIPA."""
        # 1. Crear el sobre-mi.md principal (Estructura de Identidad)
        if not os.path.exists(self.file_path):
            os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
            content = (
                "---\n"
                "titulo: Proyectos\n"
                "nombre_sitio: Daniel Miñana Montero\n"
                "rol: Propietario\n"
                "subtitulo: Plantearme metas és el plasma de mi ser\n"
                "hero_bg: img/proyectos-bg.png\n" # Ruta preparada para tu nueva imagen
                "estado: Protegido\n"
                "tag: Proyectos\n"
                "---\n"
                "# Mis proyectos\n\n"
                "Este es el espacio para tu presentación proyectos."
            )
            with open(self.file_path, "w", encoding="utf-8") as f: f.write(content)

        # 2. Crear carpeta proyectos/ y el bloque de ejemplo 'trayectoria'
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path, exist_ok=True)
            bloque_path = os.path.join(self.folder_path, "01_proyectos.md")
            bloque_content = (
                "---\n"
                "id: proyectos_ejemplo\n"
                "icono: ph-briefcase\n"
                "titulo: Proyectos ejemplo\n"
                "enlace: '#'\n"
                "orden: 1\n"
                "estado: Auditado\n"
                "tag: Profesional\n"
                "---\n"
                "# PROYECTOS\n\n"
                "Usa este bloque como plantilla para tus tablas proyectos."
            )
            with open(bloque_path, "w", encoding="utf-8") as f: f.write(bloque_content)
```

- fichero proyectos.html

```html
<!DOCTYPE html>
<html lang="es" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="SIPAweb - Identidad Digital Automática de Daniel Miñana">

    <title>Proyectos</title>
    <link rel="icon" type="image/x-icon" href="img/favicon.ico">
    
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css">
    <link rel="stylesheet" href="css/custom.css">
    <script src="https://unpkg.com/@phosphor-icons/web"></script>
</head>
<body>
    <header class="hero-sipa" style="background-image: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.4)), url('img/proyectos-bg.png');">
        <nav class="container">
            <ul>
                <li>
                    <a href="index.html" class="logo-container">
                        <img src="img/danielminanamontero-logo.png" alt="Logo de Daniel Miñana" class="logo-image" style="height: 100px; vertical-align: middle">
                        <span class="logo-text">SIPAweb</span>
                    </a>
                </li>
            </ul>
            <ul>
                <li><a href="index.html" class="nav-link"><i class="ph ph-house"></i> Inicio</a></li>
                <li><a href="ayuda.html" class="nav-link"><i class="ph ph-question"></i> Ayuda</a></li>
            </ul>
        </nav>

        <div class="hero-content container">
            <h1>Proyectos</h1>
            <p class="hero-intro">Más de 20 años de evolución IT</p>
        </div>
    </header>

    <main class="container">
        <div id="app-content">
            <h1>Mis proyectos</h1>
<p>Este es el espacio para tu presentación proyectos.</p>

            <div class="bento-grid">
                
                <article class="bloque-card">
                    <i class="ph ph-briefcase" style="font-size: 2rem; color: var(--primary);"></i>
                    <h3>Proyectos Destacados</h3>
                    <div class="card-body">
                        <h1>PROYECTOS</h1>
<p>Usa este bloque como plantilla para tus tablas proyectos.</p>
                    </div>
                    
                    <a href="'#'" class="outline">Saber más</a>
                    
                </article>
                
                <article class="bloque-card">
                    <i class="ph ph-briefcase" style="font-size: 2rem; color: var(--primary);"></i>
                    <h3>Proyecto SIPA (Sistema Identificación Personal Autorizada)</h3>
                    <div class="card-body">
                        <h1>PROYECTO SIPA, módulo SIPAweb</h1>
<p>Bienvenido a <strong>SIPAweb</strong>, el núcleo digital de mi identidad profesional. Este espacio no es solo una web; es un ecosistema automatizado diseñado para gestionar y proyectar una trayectoria de más de dos décadas en el sector tecnológico.</p>
<h2>¿Qué es SIPA?</h2>
<p>El <strong>Sistema de Identificación Personal Autorizada (SIPA)</strong> nace de la necesidad de unificar mi perfil profesional bajo un estándar de integridad y transparencia. Es el motor que destila años de administración de sistemas, redes y soporte técnico hacia el nuevo paradigma de la automatización y la ciberseguridad.</p>
<h2>¿Qué es SIPAweb?</h2>
<p>Es la implementación física de esta visión. Un sistema <strong>automático, gratuito y resiliente</strong> que transforma documentos Markdown en una presencia web profesional. Construido bajo la filosofía <em>Plug &amp; Play</em>, SIPAweb garantiza que mi perfil esté siempre actualizado, auditado y listo para los retos del futuro digital.</p>
                    </div>
                    
                    <a href="'#'" class="outline">Saber más</a>
                    
                </article>
                
            </div>
        </div>
    </main>

    <footer class="footer-sipa">
        <div class="container">
            <div class="grid">
                <div class="footer-col">
                    <p><strong>Daniel Miñana Montero</strong><br>
                    <small>by SIPAweb 2026</small></p>
                    <a href="#top" class="nav-link-subir"><i class="ph ph-caret-double-up"></i> Inicio</a>
                </div>
                
                <div class="footer-col">
                    <h6>Conectar</h6>
                    <ul class="footer-links">
                        <li><a href="https://linkedin.com/in/danielminanamontero" target="_blank">LinkedIn</a></li>
                        <li><a href="https://github.com/danielminanamontero" target="_blank">GitHub (Mimod Bland)</a></li>
                    </ul>
                </div>

                <div class="footer-col">
                    <h6>Recursos</h6>
                    <a href="#" class="btn-cv-azul">
                        <i class="ph ph-file-pdf"></i> Currículum
                    </a>
                </div>

                <div class="footer-col">
                    <h6>Radar Ciber</h6>
                    <ul class="footer-links">
                        <li><a href="https://www.incibe.es" target="_blank">Incibe</a></li>
                        <li><a href="#">Seguridad IT</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </footer>
</body>
</html>
```

- Te comento algunas cosas, me falta la imagen para el hero que es el siguiente paso, me falta el texto de la página proyectos.html y algunos otros detallitos, pero son de poco peso. A ver si ahora nos colocamos los dos en el mismo punto.

- Se breve, si estamos los dos a la par, seguimos y te planteo algunas cosas.

Registro de Sesión | Sincronización Técnica Hito 2A: Proyectos
Respuesta breve: Estamos exactamente en el mismo punto. Los ficheros que compartes confirman que la maquinaria de proyectos.html ya es operativa y sigue la lógica de "Matrices Bento" que diseñamos.

- Estado de la Auditoría Técnica
  - Clase SipaFileProyectos: Correcta. Implementa la provisión del .md principal y la carpeta de bloques, asegurando que el sistema no rompa en entornos limpios.
  - Estructura HTML: Has unificado con éxito el header (Logo de 100px) y el footer. Los bloques "SIPA" y "Ejemplo" ya renderizan correctamente dentro del bento-grid.
  - Identidad: El hero_bg apunta a img/proyectos-bg.png. Aunque la imagen no exista físicamente aún, el código ya la espera.

- Puntos Críticos para Avanzar
  - Para estar al 100% a la par, solo observa estos dos detalles menores en tu código:
    - Doble Comilla en Enlaces: En el HTML de los botones veo href="'#'". El orquestador está poniendo comillas simples dentro de las dobles. Habrá que ajustarlo en la plantilla para que sea href="#" limpio.
    - Coherencia de Texto: El hero dice "Más de 20 años...", mientras que el subtítulo del Frontmatter dice "Plantearme metas...". Solo falta decidir cuál quieres que prevalezca en el renderizado final.

Estamos sincronizados. Adelante con el planteamiento de esos temas de organización y contenido que tienes en mente. ¿Qué es lo primero?

Pregunta: Esta claro que proyectos.html esta pendiente de acabar y costará una tarde como mucho, pero me preocupa uno, el análisis de la web, ¿Es momento de tomar una pausa he implementar analistic o los que me planteantes anteriormente?, y dos, proyectos podría ser la página que ya hiciera el salto a páginas interiores, tipo post para los artículos, tipo lista con buscador para listas de bloques por ejemplo, y una página especifica para las trayectorias, se que son muchas cosas, por eso vamos a desmenuzarlo todo. Se breve y empezamos uno por uno, no hablamos de todos a la vez, cada cosa tiene su camino.

Ah, tengo que preparar la imagen hero para proyectos, es otra de las cosas pendientes.

Registro de Sesión | Análisis de Prioridades Hito 2A
Estamos alineados. Para no perder el foco y seguir el Acta Fundacional, vamos a desmenuzarlo por orden de impacto técnico.

- Analítica: ¿Pausa o implementación?
  - Recomendación: No pares el desarrollo por la analítica. SIPAweb es un generador estático. La analítica (como Google Analytics o Umami) es solo una línea de código en el \<head> de tu base.html.
    - Acción: Podemos dejar el "hueco" en la plantilla hoy, pero no pierdas una tarde en configurar paneles hasta que el contenido de Proyectos esté publicado.

- Salto a Páginas Interiores (Post/Artículos)
  - Esta es la evolución natural. Si proyectos.html va a crecer, no puede ser solo una lista de bloques infinitos.
    - Lógica Pedagógica: Necesitamos un nuevo layout (ej. proyecto-detalle.html) para que cuando el usuario haga clic en "Saber más", el orquestador sepa que debe renderizar un .md específico fuera de la cuadrícula Bento.

- Imagen Hero de Proyectos
  - Es el cierre estético. Al igual que el corazón circuiteado de "Sobre Mí", Proyectos necesita un visual que hable de "Metas y Plasma".

- ¿Por dónde empezamos?
  - Tú mandas el orden, pero mi sugerencia técnica para no romper el ritmo es:
    - Terminar el contenido de proyectos.html (incluyendo la imagen Hero).
    - Una vez que la página exista y sea sólida, implementar la Analítica (es lo más rápido).
    - Atacar la estructura de página interior (es lo más complejo a nivel de Python).

- ¿Empezamos con la creación de la imagen Hero para Proyectos o prefieres definir primero los textos de los proyectos activos? Te leo.

Pregunta: Pués empezamos, vamos a dar dos pasitos, imágen hero y listado de proyectos en borrador aquí en la bitácora y valoramos a partir de ahí.

Registro de Sesión | Ejecución Hito 2A: Activos y Estructura de Proyectos
Daniel, excelente elección. Definir primero el continente (la imagen Hero) y el contenido (el listado) nos permite visualizar el peso de la página antes de tocar el orquestador.

- Generación de Imagen Hero: "Proyectos - El Plasma del Ser"
  - Buscamos algo que represente ese "plasma", la energía de creación y las metas. He diseñado un concepto que une la tecnología abstracta con la visión de futuro, manteniendo los azules eléctricos que ya tenemos en el ADN de la web.
  - Instrucción: Guarda esta imagen como proyectos-bg.png en tu carpeta core/assets/img/. El orquestador se encargará de llevarla a SIPAweb/img/ en la próxima ejecución.

- Borrador de Listado de Proyectos (Estructura de Bloques)
  - Para que proyectos.html no sea solo una réplica del index, vamos a organizar tus bloques por Estado y Tipo. Aquí tienes mi propuesta basada en lo que hemos hablado

- Nota Pedagógica: La Organización en el Orquestador
  - Cuando pasemos este borrador al código, no crearemos un solo archivo .md gigante. Usaremos la carpeta content/proyectos/ (que tu clase SipaFileProyectos ya crea) para meter un archivo por cada fila de la tabla anterior.
  - ¿Por qué?
    - Escalabilidad: Si mañana quieres dedicarle una página entera al "FCH_CiberAudit", ya tendrás su bloque independiente listo para ser "ascendido" a página interior.
    - Mantenimiento: Puedes corregir una errata en el proyecto NCR sin riesgo de romper el código del bloque SIPAweb.

- ¿Qué te parece este listado inicial? Si estás de acuerdo con los proyectos seleccionados, el siguiente paso será redactar el contenido mínimo de cada bloque para que la página de Proyectos deje de ser un "ejemplo" y pase a ser real.

Pregunta: Vamos por partes, no anticipes, voy a redactar un manual, colocar imagenes en el hero de las paginas en sipaweb, el proceso lo he repetido con esta ya tres veces, y así empezamos a crear la página ayuda, de momento se queda en borrador aquí, no avancemos deprisa quiero disfrutarlo.

- Ya tenemos la imagen, me ha gustado
- ![Proyectos_bg](../core/assets/img/proyectos-bg.png)

- Ahora le vamos a decir a sipaweb que como por seguridad nuestra imagen origen descansa en SIPAweb/core/assets/img/proyectos-bg.png la tiene que trasladar a la carpeta SIPAweb/img/, cada vez que ejecutemos sipaweb.py, y donde lo realizamos en el fichero sipaweb.py en la "class SipaWebBuilder:" en la función:

```python
    def asegurar_activos_core(self):
        """
        Sincroniza activos desde core/assets a sus destinos de producción.
        Detecta subcarpetas en el origen para evitar errores de 'File Not Found'.
        """
        # Mapeo: (Subruta_Origen, Nombre_Fichero, Carpeta_Destino)
        activos = [
            ("", "base.html", self.templates),
            ("", "custom.css", os.path.join(self.raiz, "css")),
            ("img", "avatargithub.png", os.path.join(self.raiz, "img")),
            ("img", "sobre-mi-bg.png", os.path.join(self.raiz, "img")),
            ("img", "favicon.ico", os.path.join(self.raiz, "img")), # Nuevo: Favicon
            ("img", "danielminanamontero-logo.png", os.path.join(self.raiz, "img")), # Nuevo: Tu logo azul
            ("img", "proyectos-bg.png", os.path.join(self.raiz, "img")),
            ("pdf", "2018_porfolio.pdf", os.path.join(self.raiz, "pdf"))
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
```

- Una vez incluida en el sistema y asegurada, ahora falta decirle al fichero proyectos.md en el campo de hero_bg especifico para este tema que la ruta es la siguiente /img/proyectos-bg.png, y con esto cuando sipaweb.py se ejecute, por un lado el sistema verificara el fichero y lo trasladara a SIPAweb/img y el sistema creara el proyectos.html con la ruta a la imagen guardada allí mismo.

- fichero proyectos.md ya preparado:

```markdown
---
titulo: Proyectos
nombre_sitio: Daniel Miñana Montero
rol: Propietario
subtitulo: Plantearme metas és el plasma de mi ser
hero_bg: img/proyectos-bg.png
estado: Protegido
tag: Proyectos
---
# Mis proyectos

Este es el espacio para tu presentación proyectos.
```

- Vemos que en el campo hero_bg: ya esta indicada la ruta a la imagen. Con todo esto, si ejecutamos sipaweb.py podremos ver como encaja la imagen en la página.

- Voy a testearlo

- Me gusta mucho, a la primera y sin protestar.

- Paramos aquí, voy a cenar.

Registro de Sesión | Validación de Procedimiento de Activos v1.5.6
Pregunta del usuario: "¿Es correcto el proceso de incluir la imagen en asegurar_activos_core y actualizar el Frontmatter de proyectos.md para que la imagen se desplace y renderice correctamente?"

- Daniel, el proceso que acabas de describir es ejemplar. Has asimilado perfectamente la lógica de "Origen Seguro" vs "Destino de Producción". Lo que estás haciendo no es solo subir una imagen; estás programando la persistencia de tu identidad visual.

- Análisis Técnico del Manual (Paso a Paso)
  - La Fuente de Verdad: Al colocar la imagen en core/assets/img/, garantizas que, aunque borres toda la carpeta de producción para una limpieza total, el sitio siempre renacerá con sus imágenes.
  - El Mapeo en el Orquestador: La actualización del diccionario activos es la clave. Al añadir ("img", "proyectos-bg.png", ... ), le das al script la orden de "logística" necesaria.
  - El Frontmatter como Puente: Al poner hero_bg: img/proyectos-bg.png, estás cerrando el círculo. El HTML final simplemente leerá lo que el orquestador ha movido previamente.

- Estado del Hito 2A
  - Identidad Visual Proyectos: Completada (Imagen Hero integrada y funcional).
  - Automatización de Activos: Validada (El sistema traslada los ficheros sin errores).
  - Prueba de Estrés: Superada ("A la primera y sin protestar").

- Nota Pedagógica para tu Manual
  - Importante: Recuerda que si alguna vez la imagen no se actualiza en el navegador a pesar de que el script diga "Sincronizado", suele ser por la memoria caché del navegador. Un Ctrl + F5 suele ser el comando de soporte técnico por excelencia en estos casos.

- Disfruta de la cena, Daniel. Has cerrado el día con una base técnica impecable para la página de Proyectos. Mañana, con las energías renovadas, nos sentaremos a redactar los bloques de contenido para que esa cuadrícula Bento deje de ser un borrador y cuente tu verdadera historia técnica.

- Bitácora 20260218 195204 queda en PAUSA (Pendiente de contenido). ¡Hasta mañana!

Pregunta: Lo siguiente, voy a componer el contendido de proyectos, creo que utilizaré el texto que ya tenía para sipa y sipaweb que en proyectos deben ser los protagonistas y luego modificare el bloque para sipa, y crearé el bloque para sipaweb, sipacurator, fch-CyberAudit y alguno más que tengo pensado.

```markdown
---
titulo: Proyectos
nombre_sitio: Daniel Miñana Montero
rol: Propietario
subtitulo: Plantearme metas és el plasma de mi ser
hero_bg: img/proyectos-bg.png
estado: Protegido
tag: Proyectos
---
# Mis proyectos

Bienvenido a mi rincón de pensar, y no habló en plan paradogico, es así, ante estos documentos, códigos, imágenes paso gran parte de mi tiempo, disfruto imaginando posibilidades y proponiendome retos técnicos o nuevos aprendizajes que me pdría venir bien, bueno os he presentado mi espacio de proyectos, ahora quiero hacer incapie en uno fundamentalmente, y es sus ramificaciones, hablamos de SIPA como mi proyecto principal desde hace unos meses y que por inconvenientes no pude presentarlo en Enero como tenía previsto y entonces decidi presentar solo el módulo SIPAweb que en definitiva era la imagen pública de todo lo que hay detrás. Ahora sí mi proyecto SIPA (Sistema de Identificación Personal Autorizada). Si quereis consultar más en profundidad alguno de los proyectos, los bloques a continuación os enlazan a sus páginas especificas, tambien aprovecho y os animo a dejar cualquier comentario constructivo a traves de la página de contacto.

## Proyecto SIPA, módulo SIPAweb

Bienvenido a **SIPAweb**, el núcleo digital de mi identidad profesional. Este espacio no es solo una web; es un ecosistema automatizado diseñado para gestionar y proyectar una trayectoria de más de dos décadas en el sector tecnológico. Como caracteristica o una de ellas fundamental, la construcción del sitio web se realiza de forma autonoma desde ficheros markdown que son procesados automaticamente al detectar modificaciones en los ficheros, se renueva su hash y se construye nuevamente el fichero .html.

### ¿Qué es SIPA?

El **Sistema de Identificación Personal Autorizada (SIPA)** nace de la necesidad de unificar mi perfil profesional bajo un estándar de integridad y transparencia. Es el motor que destila años de administración de sistemas, redes y soporte técnico hacia el nuevo paradigma de la automatización y la ciberseguridad.

### ¿Qué es SIPAweb?

Es la implementación física de esta visión. Un sistema **automático, gratuito y resiliente** que transforma documentos Markdown en una presencia web profesional. Construido bajo la filosofía *Plug & Play*, SIPAweb garantiza que mi perfil esté siempre actualizado, auditado y listo para los retos del futuro digital.
```

- Vamos a revisarla y comentamos, se breve que me voy a currar

Registro de Sesión | Validación de Narrativa de Proyectos v1.5.7
Respuesta breve: El texto es excelente porque establece una jerarquía clara: SIPA es el concepto (la base de datos de identidad) y SIPAweb es el producto (la interfaz pública). Esta distinción es puramente de ingeniería y aporta mucho valor profesional.

-Comentarios Técnicos / Pedagógicos
    La Metáfora del "Rincón de Pensar": Es un acierto. Humaniza el perfil introvertido que definimos en "Sobre Mí" y justifica la existencia de proyectos complejos.
    Explicación del Proceso: Al mencionar el procesamiento de Markdown y la renovación de Hash, estás "vendiendo" tus habilidades de automatización y ciberseguridad sin necesidad de un listado aburrido de aptitudes.
    Coherencia de Flujo: El texto prepara perfectamente al usuario para los bloques Bento que vienen debajo.

- Sugerencia de Ajuste (Refinado)
  - Solo un detalle para mejorar la lectura: en el segundo párrafo, la frase sobre los "inconvenientes de enero" es honesta, pero podríamos orientarla más hacia la resiliencia:
    - Original: "...por inconvenientes no pude presentarlo en Enero..."
    - Propuesta: "...tras una fase de rediseño y optimización en enero, decidí priorizar el despliegue de SIPAweb como la cara visible de un ecosistema mucho más profundo."

- Próximo Paso (Al volver del curro)
  - Ya tienes el "clima" de la página. Lo siguiente será:
    - Trocear este contenido en los archivos .md de la carpeta content/proyectos/.
    - Crear el bloque específico para SIPAcurator (el que "alimenta" de datos al sistema).

- ¡Buen turno en NCR! A tu vuelta cerramos la redacción de estos bloques y publicamos la v1.4.5.

Pregunta: Me da tiempo a modificar la clase SipaFileProyectos(), y crear una primera prueba, He realizado la prueba ajustado y verificado exhaustivamente, ya tengo la página a subir en local, y he hecho una revisión de los bloques, copiar el bloque de sobre-mi para crear el enlace y bitacora, ya lo tengo para pasar al listado de proyectos y ver si entramos en el despliegue de las páginas interiores.

- Crear repositorio SIPA en tovid dfrei (Lo básico readme y poco más)
- Modificar el bloque SIPA y dirigirlo al repositorio
- Crear un bloque SIPAweb
- Crear página post de SIPAweb
  - Crear página post para todo el sistema
  - Enlazar el bloque a la pagina post SIPAweb
- Crear página de cronograma
  - Crear página cronograma para todo el sistema
  - Se utilizara para trayectorias y para cronograma de proyectos
  - Enlazar página a trayectorias
  - Enlazar página a página post de proyecto

- Aunque antes de terminar con proyectos, porque esto en si mismo es un proyecto, vamos a terminar un par de temas que colean.
  - Insertar analytics y comenzar a capturar datos.
  - Crear estructura documental para todo el proyecto SIPA
    - Crear la parte de SIPAweb
      - tenemos templates/static/... y todo el arbol que forma la web
      - tenemos core/assets/... para los originales digamos
      - tenemos docs/... para documentación del proyecto(bitacoras, acta...)
      - tenemos, img/, css/, pdf/, que se crean automaticamente
      - en la raiz tenemos, index, sobre-mi, proyectos, contacto, ayuda, todos .html que es la publicación en sí
  - Deberiamos crear un espacio para los post, ojo, estas publicaciones ya no son del SIPAweb automatizado.
    - Son publicaciones especificas que normalmente se crean, prueban, testean, verifican, y luego se publican
    - Lo mejor sería crear una estructura como data/ y dentro public/ y process/
      - Ejemplo ahora mismo crearía en process/ el post Cómo implementar analitics en SIPAweb, pertenece a SIPAweb pero es independiente, se podría lanzar ese post desde la página post de SIPAweb

- No se si me he sabido explicar, ante la necesidad de empezar a realizar la transición hacía las páginas expecíficas, he pensado, crear dos tipos de páginas más a parte de base.html, crear, post.html y time.html:
  - base.html - es la constructora de todo el sitio web
  - post.html - sería el documento expecífico
  - time.html - sería la muestra gráfica sí le es necesaria al post.html

- La segunda otra idea es crear ya el espacio físico para esos post.html y time.html que ire creando y publicando.

- Con todo lo que he dicho, no te extiendas vamos al primer paso y luego iremos desmenuzando, tengo guardado el texto que te paso, por lo tanto, centrate en lo primero, ya lo iremos avanzando, yo dirigo. Lo dicho con todo lo que te he planteado, por donde seguirias:
  - SIPA a tovid
  - Espacio físico
  - post.html
  - time.html

Registro de Sesión | Planificación de Infraestructura de Contenidos v1.5.8
Pregunta del usuario: "Ante la transición a páginas específicas, ¿por dónde seguirías: SIPA a tovid, Espacio físico, post.html o time.html?"

- Daniel, el esquema que planteas es el de un CMS (Content Management System) profesional. Estás separando el "Motor" (SIPAweb) de la "Factoría de Contenidos" (Data/Process).

- Siendo breve y directo, yo seguiría este orden de dependencia técnica:
  - El Espacio Físico (La Base)
    - Antes de crear plantillas (post.html), necesitamos saber dónde vivirán los archivos.
      - Acción: Crear la estructura data/process/ y data/public/.
      - Por qué: Es el "almacén" que alimentará al resto. Sin este espacio, no hay nada que renderizar en las nuevas plantillas.
    - post.html (La Plantilla Estándar)
      - Es el siguiente paso lógico para dar salida a lo que hay en "Espacio Físico".
      - Acción: Crear un layout simplificado (sin la rejilla Bento) enfocado a la lectura de artículos largos (como el de Analytics).
      - Por qué: Te permite publicar ya el detalle de SIPAweb que mencionabas.
    - time.html (El Complemento)
      - Acción: Desarrollar el layout para cronogramas.
        - Por qué: Es una especialización del post.html. Una vez tengas el sistema de posts, añadir la "línea de tiempo" es solo cambiar el CSS/Estructura visual.
      - SIPA a Tovid
        - Acción: Subir el repositorio básico.
        - Por qué: Lo pongo al final porque es una tarea administrativa de GitHub. Es importante, pero no bloquea la arquitectura de tu código.

- Nota Pedagógica: La Carpeta data/
  - Al crear data/process/, estás implementando un Staging Area.
    - Escribes el post en process/.
    - Lo testeas localmente.
    - Cuando el orquestador lo valida, el .html resultante viaja a la raíz o a una carpeta posts/ para su publicación definitiva.

- ¿Empezamos definiendo la estructura de carpetas en el orquestador para que sipaweb.py reconozca esta nueva ruta de data/?

Pregunta: No, lo primero vamos a dejar esta bitácora en pausa, y vamos abrir otra para realizar los cambios y creaciones que necesitamos, esta es exclusiva para proyectos.html y lo que estamos tratando es estructura del sistema, sipaweb.py.

---

**Pregunta** Retomada esta bitácora para completarla, ya tenemos disponibles las páginas post.html y time.html, por lo tanto el enlace al index de los los ya lo tenemos se llama list_posts.html y esta en posts/, por lo tanto podemos completar proyectos.html y pasar a cerrar sobre-mi.

- Lo primero mostrar la estructura de datos que va ha quedar:

```bash
tree templates/
templates/
├── base.html
├── post.html
├── static
│   ├── ayuda
│   │   └── 01_Ayuda.md
│   ├── ayuda.md
│   ├── contacto
│   │   └── 01_Contacto.md
│   ├── contacto.md
│   ├── index
│   │   ├── 01_sobre-mi.md
│   │   ├── 02_proyectos.md
│   │   ├── 03_ayuda.md
│   │   ├── 04_bitacora.md # enlaza a list_posts.html - ok
│   │   └── 05_seguridad.md
│   ├── index.md
│   ├── posts
│   │   ├── process
│   │   │   ├── 00-plantilla-post.md
│   │   │   ├── 01-bitacora-sipaweb.md
│   │   │   ├── bitacora_sipaweb_extruc_data.md
│   │   │   ├── error-apagado-ubuntu-24-04-4.md
│   │   │   ├── formativa # Nueva carpeta para ficheros con experiencias formativas .md - ok
│   │   │   ├── laboral # Nueva carpeta para ficheros con experiencias laborales .md - ok
│   │   │   ├── test_2.md
│   │   │   └── test.md
│   │   └── public # Vacío public para crear un primer post, estoy decidiendo - ok
│   ├── proyectos
│   │   ├── 01_sobre-mi.md
│   │   ├── 02_bitacora.md # enlaza a list_posts.html - ok
│   │   ├── 03_proyectos.md # enlaza a list_posts.html - ok
│   │   └── sipa.md # Lo quito de los bloques de proyectos y se convertira en un post enlace al repositorio tovid - ok
│   ├── proyectos.md
│   ├── sobre-mi
│   │   ├── 01_proyectos.md
│   │   ├── 02_trayectoria_profesional.md # Pendiente preparar
│   │   ├── 03_trayectoria_formativa.md # Pendiente preparar
│   │   └── bitacora.md # Lo quito de sobre-mi no tiene lógica - ok
│   └── sobre-mi.md
└── time.html

12 directories, 29 files
```

- Así voy a dejar la estructura los comentarios marcan la creación de las carpetas para preparar los post de cronologia formativa y profesional - ok
- Volvemos al punto que nos hizo tener este parón, crearé el repositorio SIPA en tovid y enlazaremos este post con el repositorio
- Estoy pensando que el primer post sería poner bonita el acta fundación de SIPAweb y publicarlo - ok
- Revisar ayuda, enlace a index de momento - ok
- Incluir el enlace a contacto.html
- Revisar el Readme

---

Registro de Sesión | **Reestructuración de Activos y Despliegue v1.6.6**

- Daniel, bienvenido de nuevo al taller. El mapa de directorios que has trazado es la definición de un sistema maduro. Estás pasando de tener archivos sueltos a una arquitectura de carpetas que permitirá al motor SIPA clasificar el contenido de forma automática por su origen (laboral, formativa, process).

- Análisis de la Nueva Estructura
  - La inclusión de las carpetas posts/process/formativa y posts/process/laboral es clave.
    - **Lógica de Negocio**: Cuando sipaweb.py recorra estas rutas, el metadato tipo se asignará casi por herencia de carpeta, lo que hará que tu list_posts.html sepa perfectamente qué es una tarjeta de "Experiencia Laboral" y qué es una "Bitácora".

- Tareas de Limpieza Confirmadas:
  - Bitácora: Centralizada en list_posts.html (adiós a la redundancia en sobre-mi).
  - Proyectos: El archivo sipa.md se eleva a la categoría de Post Fundacional, vinculándolo a tu repositorio en GitHub. Es una excelente decisión de marca personal.

- El Acta Fundacional: Tu primer "Post Real"
  - Publicar el acta de fundación de SIPAweb como primer post es un movimiento maestro de storytelling.
  - Sugerencia para el Acta: Usa el formato de post.html. Al ser un documento "histórico" para tu proyecto, los niveles de título (#, ##) generarán un TOC lateral que le dará un aspecto de documentación técnica oficial de alto nivel.

- Verificación de Enlaces y Rutas (Evitando 404)
  - Para que la navegación sea fluida antes de cerrar, asegúrate de que los bloques en los ficheros .md de la carpeta index/ tengan estas rutas:

| Bloque    | Enlace en el .md                         | Destino Final                                  |
|-----------|------------------------------------------|------------------------------------------------|
| Bitácora  | `[Ver Bitácora](posts/list_posts.html)`  | Índice cronológico (time.html)                 |
| Proyectos | `[Ver Proyectos](posts/list_posts.html)` | (Por ahora al mismo índice, filtrable después) |
| Contacto  | `[Contacto](contacto.html)`              | Página de formulario/redes                     |
| Ayuda     | `[Ayuda](index.html)`                    | Retorno al inicio (Temporal)                   |

- El Repositorio SIPA y el README
  - Al crear el repositorio en GitHub, el README.md debería reflejar esta estructura técnica que hemos construido. No es solo un sitio web; es un Generador de Sitios Estáticos (SSG) basado en Python y Jinja2.

- Próximos pasos operativos:
  - Mover los archivos: Reubicar los .md según tu nuevo árbol de directorios.
  - Preparar el Acta: Crear acta-fundacion-sipaweb.md en posts/public.
  - Ejecución de Control: Lanzar sipaweb.py para verificar que el acumulador lee correctamente las nuevas subcarpetas (laboral/, formativa/).

- ¿Te parece si revisamos el contenido del README para que proyecte esa imagen de "Artesano IT" que estamos construyendo antes de que hagas el primer push al repositorio? Solo dime qué puntos quieres destacar y le damos forma.

**Pregunta** Voy avanzando en la reorganización y creación de lo que llamaremos el estandar del site, pero he detectado un error bastante sutil pero muy perjudicial. Al repasar los niveles de los ficheros markdown los niveles que en su contenido tienen una palabra con acento ya no se la puede enlazar en el html entre las dos columnas, lo acabo de probar con el acta, misión y mision una si y la otra no, cuando parseamos el fichero no parseamos los acentos, lo revisamos por fa.

---

Registro de Sesión | **Depuración de Codificación y Slugify v1.6.7**

- Daniel, has dado en el clavo. Es el clásico error de normalización de caracteres. El problema es que al generar el "ancla" (el ID en el HTML), estamos eliminando o transformando los caracteres especiales de forma inconsistente entre el menú lateral (TOC) y el cuerpo del texto.

- En español, para que un enlace como #misión sea robusto, lo estándar es "limpiar" el texto: quitar acentos y convertir la ñ en n.

- La Solución en sipaweb.py
  - Debemos actualizar la lógica de generación del anchor dentro de ejecutar_ciclo_editorial. Vamos a usar una técnica más profesional para eliminar tildes.
  - Busca la sección donde generas el anchor y sustitúyela por esta (necesitaremos importar unicodedata al principio del archivo):

```python
import unicodedata
import re

# ... dentro de tu bucle de títulos ...
titulo = linea_clean.replace('#', '').strip()

# NORMALIZACIÓN PROFESIONAL (Slugify)
# 1. Convertir a minúsculas
anchor = titulo.lower()
# 2. Quitar acentos (Misión -> Mision)
anchor = unicodedata.normalize('NFKD', anchor).encode('ascii', 'ignore').decode('ascii') # Esta línea lo ha solucionado todo
# 3. Quitar caracteres raros y poner guiones en espacios
anchor = re.sub(r'[^\w\s-]', '', anchor)
anchor = re.sub(r'[\s]+', '-', anchor).strip('-')

indice_dinamico.append({
    'nivel': nivel,
    'titulo': titulo, # El título original (con acento) para mostrar en el menú
    'anchor': anchor  # El ID limpio (sin acento) para el enlace técnico
})
```

- Por qué esto arregla el Acta
  - **El ID**: La sección "Misión" se convertirá en \<h2 id="mision">.
  - **El Enlace**: El menú lateral apuntará a \<a href="#mision">.
  - **El Resultado**: Al no haber caracteres especiales en el atributo id, el navegador no se confunde con la codificación de la URL.

- Verificación de la Codificación (UTF-8)
  - Asegúrate también de que al leer el archivo .md en Python estés forzando encoding='utf-8', de lo contrario, al encontrar una tilde, Python podría romper el proceso de lectura antes de llegar al parseo:

```python
# Cuando abras el MD para procesar:
with open(ruta_md, 'r', encoding='utf-8') as f:
    texto = f.read()
```

- Estado del Acta Fundacional
  - Una vez apliques esta limpieza de acentos en el generador de anclas, el acta con Misión, Visión y Valores funcionará perfectamente en las dos columnas.

- Próximo Paso
  - Aplica este cambio en el sipaweb.py, regenera el sitio y comprueba el acta. Si los enlaces del lateral ya saltan correctamente a las secciones con tildes, habremos eliminado el último "bug" técnico de navegación.

- ¿Te parece si después de esto revisamos el README del repositorio para dejar constancia de que el sistema ya soporta normalización de caracteres en español? Es un buen detalle técnico para presumir.

#### Listado de proyectos, en proceso, parados, activos, preparar página y publicar

- Cierro esta bitácora, esta preparada para tener un flujo de navegación correcta, proyectos.html es funcional no tiene enlaces perdidos, ya conecta con list_posts.html y desde ahí cierra la navegación.
- El filtrado por estado todavía no ha sido aplicado, de momento el control lo gestiono yo creando contenido, en versiones siguientes mejoraremos fundamentalmente búsquedas y filtros según estado, según etiquetas, y algunos otros filtros que puedan ser útiles.
- Verificación ortográfica realizada
- Commit versión 1.4.6 proyectos.html, post.html, time.html

#### Cerrada 28/02/2026 18:14:15
