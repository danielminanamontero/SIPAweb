# SIPAweb

## Misión y Visión

SIPAweb nace como el puente público entre una trayectoria consolidada y la innovación tecnológica actual.

**Misión:** Proyectar la experiencia de más de 20 años en el sector IT, integrada con las competencias de FullStack (2024-2025), ofreciendo una interfaz dinámica que demuestre capacidad de adaptación y dominio técnico actual ante reclutadores y el mercado.

**Visión:** Crear un ecosistema autónomo donde la Inteligencia Artificial procese décadas de formación y laboratorios locales, cruzándolos con tendencias del mercado laboral en tiempo real para generar contenido estratégico y posicionamiento experto.

## Objetivos Estratégicos

**Automatización Local:** Procesamiento de datos en local para inyección de contenido en la web. Despliegue automatizado en GitHub Pages.

**Coste Cero y Resiliencia:** Despliegue en GitHub Pages mediante HTML plano, garantizando seguridad y máxima velocidad de carga.

Documentación técnica viva (**MkDocs**).

**Curriculum Dinámico:** Evolución constante basada en el aprendizaje automático y noticias del sector. Arquitectura "Plug & Play" para futuros módulos.

**Arquitectura de Datos:** Uso de core/persistence.py para asegurar que la información histórica sea la base del contenido futuro (SIPA_PROJECT).

## Stack Tecnológico y Protocolos

|Componente    |Tecnología            |Propósito                                                                 |
|--------------|----------------------|--------------------------------------------------------------------------|
|Núcleo        |Python 3.x            |Procesamiento de lógica e integración de IA.                              |
|Documentación |MkDocs + mkdocstrings |Documentar el proceso para perfiles no técnicos.                          |
|Generador     |Jinja2                |Transformar datos lógicos en HTML estático puro.                          |
|Despliegue    |GitHub Actions        |CI/CD: GitHub Actions. "Automatización total del flujo ""Código -> Web""."|

## Cronograma Estimado: Fases de desarrollo por hitos, no por fechas rígidas

### Cronograma de Hitos

#### HITO 1 FINALIZADO

Hito 1: Estructura de documentación y base del conector Python.

- Núcleo y Documentación

- Para alcanzar el hito 1, los pasos a seguir son estos
  - [x] Creación de estructura de desarrollo inicial
    - Ubicación desarrollo: /SIPA_PROJECT/constructor/sipaweb/
  - [x] Instalación Mkdocs
    - Instalado en sipaweb, creado /SIPA_PROJECT/constructor/sipaweb/docs/index.md
  - [x] Testeo y pruebas
    - Pruebas al documentador
    - Pruebas al script
  - [x] Todo documentado y funcionando hito 1 conseguido

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
- [ ] Revisión completa a modo auditoría
  - [ ] README.md presente
  - [ ] mkdocs.yml presente
  - [ ] .gitignore presente
  - [ ] requirements.txt presente
  - [ ] /.github/workflows/deploy.yml presente
  - [ ] acta_fundacion.md presente
  - [ ] index.md presente
  - [ ] referencia.md presente
  - [ ] bitacora_sipaweb.md presente
  - [ ] revisión arquitectura y árbol
  - [ ] revisión lógica
  - [ ] revisión objetivo
  - [ ] revisión situación final

Hito 2 A : Confeccionar página a página

- [ ] Diseño estructura, acciones, contenido de index.html
  - [ ] Definir estructura
  - [ ] Definir colores marca
  - [ ] Definir iconos
  - [ ] Definir bloques
  - [ ] Definir contenido
- [ ] Diseño estructura, acciones, contenido de sobre-mi.html
- [ ] Diseño estructura, acciones, contenido de proyectos.html
- [ ] Diseño estructura, acciones, contenido de contacto.html
- [ ] Diseño estructura, acciones, contenido de ayuda.html
- [ ] Enlace de todas con todas, a través de una barra navegación fija
- [ ] Enlace de los proyectos en el pie según perfil tovid o mimod

[] Cierre proyecto SIPAweb versión 1.0

### Proyecto conjunto con SIPA_PROJECT

Pendiente de retomar el SIPA_PROJECT para encajarlo en su cronograma de desarrollo

#### HITO 3 PLANIFICAR

Hito 3: Integración del procesador de trayectoria profesional (SIPA core).

- [] Planificar la integración de SIPAweb versión 1.0 en SIPA_PROJECT
- [] Crear cronograma ejecución aproximada 3 meses a partir de Abril 2026 flexible

#### HITO 4 PLANIFICAR

Hito 4: Módulo de análisis de mercado e inyección de contenido IA.

- [] Planificar la integración de SIPAweb versión 1.0 en SIPA_PROJECT
- [] Crear cronograma ejecución aproximada 3 meses a partir de Abril 2026 flexible
