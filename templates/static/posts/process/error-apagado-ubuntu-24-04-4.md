---
titulo: Error apagado Ubuntu 24-04-4 LTS
subtitulo: Revisar log rápidamente para tomar decisiones
estado: proceso
fecha_creacion: 2026-02-21
fecha_publicacion: pendiente
tag: sistema operativo, hardware, error
tipo: post
autor: Daniel Miñana
---

# ESCENARIO

Al realizar el apagado de mi propio equipo, desde la última actualización del Kernel linux que maneja, el apagado me muestra muy rápidamente dos errores y se apaga, no he notado nada raro, pero de formación profesional quiero saber que esta pasando en mi equipo personal, tengo mucho acumulado para jugarmela.

El primer paso, lo más rápido es que le pida a mi colaborador ayuda y si tengo que profundizar ya extiendo la búsqueda, por lo tanto gemini preparame un script básico en bash para revisar los los sobre todo los de encendido y apagado del equipo, estoy notando algo extraño.

## CONVERSACIÓN CON GEMINI

### Me puedes crear un script en bash que me revise los log del sistema

Me puedes crear un script en bash que me revise los log del sistema, al apagar el equipo ubuntu 24.04 lts me lanza un error o dos pero no consigo rescatarlos, quiero revisar los los de arranque y apagado fundamentalmente en mi equipo sencillo

#### Esos errores que aparecen justo antes de que la pantalla se apague son como fantasmas: parpadean un segundo y desaparecen

¡Claro! Entiendo perfectamente la frustración. Esos errores que aparecen justo antes de que la pantalla se apague son como fantasmas: parpadean un segundo y desaparecen

En Ubuntu 24.04 (que usa systemd), la mejor forma de capturar esto no es solo "mirar un archivo", sino interrogar al diario del sistema (journalctl). He preparado un script sencillo que filtra específicamente lo que necesitas.

- El Script: revisor_logs.sh
  - Este script buscará los errores de nivel "crítico" hacia arriba del arranque actual y, lo más importante, del apagado anterior.

```bash
#!/bin/bash

# Colores para mejor lectura
ROJO='\033[0;31m'
VERDE='\033[0;32m'
AZUL='\033[0;34m'
NC='\033[0m' # Sin color

echo -e "${AZUL}=== Buscador de Errores de Sistema ===${NC}"

# 1. Errores en el apagado anterior
echo -e "\n${ROJO}[!] Errores detectados en el ÚLTIMO APAGADO:${NC}"
journalctl -b -1 -p 3..0 --no-hostname

# 2. Errores en el arranque actual
echo -e "\n${VERDE}[+] Errores detectados en el ARRANQUE ACTUAL:${NC}"
journalctl -b 0 -p 3..0 --no-hostname

# 3. Guardar en un archivo para que lo puedas leer con calma
journalctl -b -1 -p 3..0 > errores_apagado.txt
echo -e "\n${AZUL}---${NC}"
echo -e "Se ha creado un archivo '${VERDE}errores_apagado.txt${NC}' con los detalles del cierre anterior."
```

- Cómo prepararlo y usarlo
  - Crea el archivo:
    - Abre una terminal y escribe: nano revisor_logs.sh
    - Pega el código anterior. (Control+Shift+V para pegar en terminal).
    - Guarda y sal:
      - Presiona Ctrl + O, luego Enter y después Ctrl + X.
    - Dale permisos de ejecución:

        ```bash
        chmod +x revisor_logs.sh
        ```

    - Ejecútalo:

        ```bash
        sudo ./revisor_logs.sh
        ```

    - (Es necesario sudo porque los logs del sistema están protegidos).

- ¿Qué significan los comandos que usé?
  - Para que vayas aprendiendo qué estamos haciendo "bajo el capó":
    - journalctl: Es la herramienta moderna de Linux para leer logs.
    - -b -1: Le dice al sistema: "Muéstrame los datos de la sesión anterior (antes del último reinicio)".
    - -p 3..0: Filtra por prioridad. En Linux, 3 es "Error", 2 es "Crítico", 1 es "Alerta" y 0 es "Emergencia". Así ignoramos los mensajes informativos que no nos sirven.
    - --no-hostname: Solo para limpiar la vista y que sea más corto de leer.

- Un consejo extra para Ubuntu 24.04
  - Si el error pasa tan rápido que el sistema ni siquiera llega a escribirlo en el disco, podrías intentar ver los logs en tiempo real desde otro dispositivo o desactivar el "Splash Screen" (el logo de Ubuntu al cargar) editando el archivo /etc/default/grub y quitando las palabras quiet splash. Así verás todo el texto técnico mientras se apaga.

- ¿Te gustaría que te ayude a interpretar el resultado del archivo errores_apagado.txt una vez que lo ejecutes?

### Me lanza estos errores

Log extraido de la salida por consola del script bash revisor_logs.sh:

```bash
feb 20 13:17:39 kernel: ACPI BIOS Error (bug): Failure creating named object [\_SB.PC00.TXHC.RHUB.SS01._UPC], AE_ALREADY_EXISTS (20250404/dswload2-326)
feb 20 13:17:39 kernel: ACPI Error: AE_ALREADY_EXISTS, During name lookup/catalog (20250404/psobject-220)
feb 20 13:17:39 kernel: ACPI BIOS Error (bug): Failure creating named object [\_SB.PC00.TXHC.RHUB.SS01._PLD], AE_ALREADY_EXISTS (20250404/dswload2-326)
feb 20 13:17:39 kernel: ACPI Error: AE_ALREADY_EXISTS, During name lookup/catalog (20250404/psobject-220)
feb 20 13:17:39 kernel: ACPI BIOS Error (bug): Failure creating named object [\_SB.PC00.TXHC.RHUB.SS02._UPC], AE_ALREADY_EXISTS (20250404/dswload2-326)
feb 20 13:17:39 kernel: ACPI Error: AE_ALREADY_EXISTS, During name lookup/catalog (20250404/psobject-220)
feb 20 13:17:39 kernel: ACPI BIOS Error (bug): Failure creating named object [\_SB.PC00.TXHC.RHUB.SS03._UPC], AE_ALREADY_EXISTS (20250404/dswload2-326)
feb 20 13:17:39 kernel: ACPI Error: AE_ALREADY_EXISTS, During name lookup/catalog (20250404/psobject-220)
feb 20 13:17:39 kernel: ACPI BIOS Error (bug): Failure creating named object [\_SB.PC00.TXHC.RHUB.SS04._UPC], AE_ALREADY_EXISTS (20250404/dswload2-326)
feb 20 13:17:39 kernel: ACPI Error: AE_ALREADY_EXISTS, During name lookup/catalog (20250404/psobject-220)
feb 20 13:17:39 kernel: ACPI BIOS Error (bug): Failure creating named object [\_SB.PC00.XHCI.RHUB.HS01._UPC], AE_ALREADY_EXISTS (20250404/dswload2-326)
feb 20 13:17:39 kernel: ACPI Error: AE_ALREADY_EXISTS, During name lookup/catalog (20250404/psobject-220)
feb 20 13:17:39 kernel: ACPI BIOS Error (bug): Failure creating named object [\_SB.PC00.XHCI.RHUB.HS01._PLD], AE_ALREADY_EXISTS (20250404/dswload2-326)
feb 20 13:17:39 kernel: ACPI Error: AE_ALREADY_EXISTS, During name lookup/catalog (20250404/psobject-220)
feb 20 13:17:39 kernel: ACPI BIOS Error (bug): Failure creating named object [\_SB.PC00.XHCI.RHUB.HS02._UPC], AE_ALREADY_EXISTS (20250404/dswload2-326)
feb 20 13:17:39 kernel: ACPI Error: AE_ALREADY_EXISTS, During name lookup/catalog (20250404/psobject-220)
feb 20 13:17:39 kernel: ACPI BIOS Error (bug): Failure creating named object [\_SB.PC00.XHCI.RHUB.HS02._PLD], AE_ALREADY_EXISTS (20250404/dswload2-326)
feb 20 13:17:39 kernel: ACPI Error: AE_ALREADY_EXISTS, During name lookup/catalog (20250404/psobject-220)
feb 20 13:17:39 kernel: ACPI BIOS Error (bug): Failure creating named object [\_SB.PC00.XHCI.RHUB.HS03._UPC], AE_ALREADY_EXISTS (20250404/dswload2-326)
feb 20 13:17:39 kernel: ACPI Error: AE_ALREADY_EXISTS, During name lookup/catalog (20250404/psobject-220)
feb 20 13:17:39 kernel: ACPI BIOS Error (bug): Failure creating named object [\_SB.PC00.XHCI.RHUB.HS04._UPC], AE_ALREADY_EXISTS (20250404/dswload2-326)
feb 20 13:17:39 kernel: ACPI Error: AE_ALREADY_EXISTS, During name lookup/catalog (20250404/psobject-220)
feb 20 13:17:39 kernel: ACPI BIOS Error (bug): Failure creating named object [\_SB.PC00.XHCI.RHUB.HS05._UPC], AE_ALREADY_EXISTS (20250404/dswload2-326)
feb 20 13:17:39 kernel: ACPI Error: AE_ALREADY_EXISTS, During name lookup/catalog (20250404/psobject-220)
feb 20 13:17:39 kernel: ACPI BIOS Error (bug): Failure creating named object [\_SB.PC00.XHCI.RHUB.HS06._UPC], AE_ALREADY_EXISTS (20250404/dswload2-326)
feb 20 13:17:39 kernel: ACPI Error: AE_ALREADY_EXISTS, During name lookup/catalog (20250404/psobject-220)
feb 20 13:17:39 kernel: ACPI BIOS Error (bug): Failure creating named object [\_SB.PC00.XHCI.RHUB.HS06._PLD], AE_ALREADY_EXISTS (20250404/dswload2-326)
feb 20 13:17:39 kernel: ACPI Error: AE_ALREADY_EXISTS, During name lookup/catalog (20250404/psobject-220)
feb 20 13:17:39 kernel: ACPI BIOS Error (bug): Failure creating named object [\_SB.PC00.XHCI.RHUB.HS07._UPC], AE_ALREADY_EXISTS (20250404/dswload2-326)
feb 20 13:17:39 kernel: ACPI Error: AE_ALREADY_EXISTS, During name lookup/catalog (20250404/psobject-220)
feb 20 13:17:39 kernel: ACPI BIOS Error (bug): Failure creating named object [\_SB.PC00.XHCI.RHUB.HS08._UPC], AE_ALREADY_EXISTS (20250404/dswload2-326)
feb 20 13:17:39 kernel: ACPI Error: AE_ALREADY_EXISTS, During name lookup/catalog (20250404/psobject-220)
feb 20 13:17:39 kernel: ACPI BIOS Error (bug): Failure creating named object [\_SB.PC00.XHCI.RHUB.HS08._PLD], AE_ALREADY_EXISTS (20250404/dswload2-326)
feb 20 13:17:39 kernel: ACPI Error: AE_ALREADY_EXISTS, During name lookup/catalog (20250404/psobject-220)
feb 20 13:17:39 kernel: ACPI BIOS Error (bug): Failure creating named object [\_SB.PC00.XHCI.RHUB.HS09._UPC], AE_ALREADY_EXISTS (20250404/dswload2-326)
feb 20 13:17:39 kernel: ACPI Error: AE_ALREADY_EXISTS, During name lookup/catalog (20250404/psobject-220)
feb 20 13:17:39 kernel: ACPI BIOS Error (bug): Failure creating named object [\_SB.PC00.XHCI.RHUB.HS09._PLD], AE_ALREADY_EXISTS (20250404/dswload2-326)
feb 20 13:17:39 kernel: ACPI Error: AE_ALREADY_EXISTS, During name lookup/catalog (20250404/psobject-220)
feb 20 13:17:39 kernel: ACPI BIOS Error (bug): Failure creating named object [\_SB.PC00.XHCI.RHUB.HS10._UPC], AE_ALREADY_EXISTS (20250404/dswload2-326)
```

#### ¡Excelente! Ya tenemos al "culpable". No te asustes por la cantidad de líneas; aunque parece un desastre, en realidad es un error muy común y, generalmente, inofensivo

- ¿Qué está pasando exactamente?
  - Esos errores de ACPI BIOS Error significan que el firmware de tu placa base (la BIOS) le está intentando decir al sistema operativo (Linux) que ciertos componentes (en este caso, puertos USB y hubs como RHUB, HS01, SS01) existen... dos veces.
    - AE_ALREADY_EXISTS: Literalmente, el Kernel de Linux dice: "Oye, ya registré este puerto USB antes, no me lo vuelvas a nombrar".
    - Causa: Es un pequeño "bug" en cómo el fabricante de tu equipo escribió las tablas ACPI. Es como si el manual de instrucciones de tu casa dijera dos veces que hay un enchufe en la misma pared.

- ¿Deberías preocuparte?
  - La respuesta corta es NO. En el 99% de los casos, estos errores no afectan al rendimiento ni a la estabilidad. Linux detecta el duplicado, lanza la queja en el log y simplemente ignora el segundo anuncio, funcionando normalmente con el primero.

- Sin embargo, como entiendo que quieres un sistema "limpio", aquí tienes lo que puedes hacer:
  - La solución ideal (Actualizar BIOS)
    - Como el error viene de la BIOS/Firmware, la solución definitiva es:
      - Ir a la web del fabricante de tu PC o placa base.
      - Ver si existe una actualización de BIOS reciente.
      - A menudo, los fabricantes corrigen estas tablas ACPI para que sean compatibles con kernels de Linux más modernos.
  - La solución técnica (Ocultar los mensajes)
    - Si no hay actualización de BIOS y todo te funciona bien (teclado, ratón, puertos USB), puedes decirle al Kernel que sea menos "hablador" con el ACPI.
      - Edita el archivo de configuración del arranque:

        ```bash
        sudo nano /etc/default/grub
        ```

      - Busca la línea que dice GRUB_CMDLINE_LINUX_DEFAULT="quiet splash".
      - Añade el parámetro loglevel=3 (para que solo muestre errores graves) o acpi_loglevel=0. Quedaría algo así:

        ```bash
        GRUB_CMDLINE_LINUX_DEFAULT="quiet splash loglevel=3"
        ```

      - Guarda (Ctrl+O, Enter) y sal (Ctrl+X).
      - Muy importante, actualiza el grub:

        ```bash
        sudo update-grub
        ```

- Resumen de los errores encontrados

| Elemento en el Log  | Significado                                                    |
|---------------------|----------------------------------------------------------------|
| `\_SB.PC00.XHCI`    | Se refiere al controlador de los puertos USB 3.0.              |
| `HS01, HS02...`     | Son los puertos USB de alta velocidad (High Speed).            |
| `SS01, SS02...`     | Son los puertos USB de súper velocidad (SuperSpeed).           |
| `AE_ALREADY_EXISTS` | El sistema ignora la entrada duplicada para evitar conflictos. |

- Conclusión: Tu equipo está sano. Es solo que tu BIOS y el Kernel de Linux tienen una pequeña discusión sobre cuántas veces deben presentarse los puertos USB al encender el equipo.

- ¿Has notado si algún puerto USB te deja de funcionar o si el equipo tarda mucho en apagarse debido a esto?

### No he notado nada raro en el rendimiento del equipo

No, la verdad no he notado ni falta de rendimiento ni nada por el estilo, lo he notado desde la ultima actualización del kernel linux

#### Eso confirma nuestra sospecha: no es un fallo de tu hardware, sino una "discrepancia de opiniones" entre el nuevo Kernel y tu BIOS.

Al actualizarse el Kernel (probablemente a una versión de la rama 6.x en Ubuntu 24.04), Linux se ha vuelto más estricto al leer las tablas ACPI de tu placa base. Lo que antes el Kernel ignoraba en silencio, ahora lo reporta como un error porque detecta que la BIOS está mal programada (nombra los mismos puertos USB varias veces).

- ¿Por qué ahora?
  - Los desarrolladores del Kernel de Linux a veces activan comprobaciones más rigurosas para asegurar que el ahorro de energía y la gestión de dispositivos sean perfectos. Al encontrar esas entradas duplicadas (AE_ALREADY_EXISTS), el Kernel lanza el aviso por si acaso eso causara un conflicto de energía, pero como has visto, él mismo lo gestiona y sigue adelante sin problemas.

- ¿Qué te recomiendo hacer?
  - Dado que el sistema es estable y no tienes pérdida de rendimiento:
    - Ignóralos con tranquilidad: Es puramente "ruido" visual en el log. Tu equipo no corre peligro ni se va a romper.
    - No toques nada si no te molesta: Si no ves esos mensajes a menudo y el equipo apaga rápido, dejarlo como está es la opción más segura.
    - Si te resulta molesto ver el texto al apagar: Aplica el paso que te comenté antes de añadir loglevel=3 a la línea de GRUB. Esto filtrará los mensajes de aviso de la BIOS y solo te mostrará errores que realmente impidan el funcionamiento del sistema.

- Una curiosidad técnica
  - Si tienes curiosidad por saber de dónde viene exactamente, puedes ejecutar este comando para ver qué marca de BIOS tienes y cuándo se actualizó por última vez:

    ```bash
    sudo dmidecode -s bios-vendor
    sudo dmidecode -s bios-version
    sudo dmidecode -s bios-release-date
    ```

- Es muy probable que la fecha de tu BIOS sea anterior a la fecha del Kernel que usas ahora. Los fabricantes suelen dejar de actualizar las BIOS de equipos "sencillos" o antiguos, mientras que Linux sigue evolucionando y volviéndose más "tiquismiquis" con el orden de las cosas.

- ¿Quieres que te ayude a revisar si hay alguna otra cosa extraña en el log o prefieres que guardemos este análisis por si en el futuro aparece algo nuevo? (Recuerda que tengo anotado guardar tus consultas para futuras referencias).

### Conclusiones autor

La IA gratis que utilizo Gemini de Google hasta el momento a mi me solventa muchísimos problemas, pero no siempre acierta, ni aconseja de la mejor forma. Ha una persona como yo con la experiencia IT, decirle que la opción es dejar el error ahí o que sí no lo oculte, es abrirle una herida en su corazón, ahora tengo muchos más datos, pero no los tengo todos.

- Como se suele decir, voy a pedir una segunda opinión y voy a intentar obtener más datos en relación a la última verión oficial de bios para linux de mi equipo y si ubuntu tiene alguna referencia de este tipo de problemas, y esto lo voy hacer a la vieja usanza, consultando foros, faq, y leyendo, leyendo mucho.

### Cronograma para completar

- Búsqueda fecha última bios para equipo
  - ficha técnica del equipo
- Búsqueda información sobre error en ubuntu
- Conclusión y tareas pendientes

### Conclusión y tareas pendientes
