# Tamarindos Workflow Kit

Un sistema de productividad personal que combina Claude (IA) con Obsidian (notas) para crear un espacio de trabajo compartido donde tú y la IA construyen sobre los mismos archivos, el mismo contexto y el mismo historial.

## Por qué existe

La mayor limitación de trabajar con IA hoy es la memoria. Las ventanas de chat se saturan, el contexto se degrada y todo lo que construyen juntos nace y termina dentro de una conversación. Empiezas desde cero cada vez. Te repites. La IA olvida lo que le dijiste ayer.

Workflow Kit resuelve esto dándoles a ti y a la IA un **sistema de archivos compartido**. Tu bóveda es simplemente una carpeta de archivos de texto en tu computadora, pero esos archivos se convierten en almacenamiento persistente que tanto tú como la IA pueden leer, escribir y ampliar entre sesiones. Cuanto más lo usas, más inteligente se vuelve tu IA, porque dispone de un repositorio cada vez mayor de tu trabajo, tus decisiones, el historial de tus proyectos y tus preferencias.

Esto no es solo una interfaz alrededor de un chat. Es un sistema que:

- **Guarda todo lo que haces** como archivos organizados que la IA puede consultar después.
- **Construye tu base de conocimiento personal** automáticamente a través del propio trabajo, sin depender de documentarlo manualmente.
- **Te permite retomar cualquier proyecto al instante**, incluso semanas después, porque el contexto está en los archivos, no en tu cabeza.
- **Mejora con el tiempo** a medida que tu bóveda acumula registros de proyectos, lecciones e historial de trabajo.

Para conocer con más detalle cómo se conectan todas las piezas, consulta [Cómo funciona todo](WORKFLOW.md).

---

## Para quién es

**Profesionales con conocimientos técnicos que no son programadores.** Administradores de TI, gerentes de operaciones, coordinadores de proyectos, jefes de departamento, responsables de hotelería y consultores. Personas con capacidad técnica, que se sienten cómodas usando una terminal y realizan trabajo estructurado que implica investigación, decisiones, documentación y seguimiento.

Si perteneces a esta categoría, puedes beneficiarte de esta tecnología ahora mismo más que casi cualquier otra persona. Los asistentes de programación con IA ya están maduros, pero los sistemas de productividad con IA para trabajo que no es programación apenas están surgiendo. Workflow Kit cubre ese espacio.

No necesitas saber programar. Necesitas sentirte cómodo escribiendo comandos en una terminal y organizando archivos. De todo lo demás se encarga Claude.

### Ejemplos reales por función

**TI / Administración de redes:** Graba una visita a un sitio narrando tu inventario de dispositivos. Claude genera archivos Markdown con números de serie, ubicaciones y configuraciones. Construye poco a poco una topología completa de la red que Claude pueda consultar al resolver problemas. Cuando aparezca un bucle de VLAN a las 2 de la mañana, Claude ya conocerá la distribución de tu red.

**Operaciones de restaurante / hotel:** Graba la investigación de un incidente. Claude la transcribe, genera un reporte estructurado y crea un ticket en tu sistema de seguimiento de incidencias. El próximo mes, pregunta «¿Cuáles fueron todos los incidentes de este mes?» y obtén un resumen en segundos.

**Gerencia / Dirección:** Siéntate con tu jefe mientras enumera 15 solicitudes. Claude captura todo, lo clasifica según tus proyectos activos y no se pierde nada. Tres semanas después, cuando pregunte «¿Qué pasó con aquello?», tendrás la respuesta.

**Consultoría / Asesoría:** Construye perfiles de clientes que se actualicen con cada interacción. Las notas de reuniones, los resúmenes de correos y el historial de proyectos se acumulan en una base de conocimiento con la que cualquier nuevo integrante del equipo, o una nueva sesión de IA, puede ponerse al día al instante.

---

## Qué puedes hacer con el sistema

**La versión breve:** Describes lo que quieres lograr y el sistema te guía:

1. **Define la especificación** -- Claude te hace preguntas para entender lo que intentas hacer y después lo redacta con claridad.
2. **Revisa tu planteamiento** -- Un equipo de revisión de 3 agentes de IA busca vacíos, riesgos y cosas que podrías haber pasado por alto.
3. **Planifica el trabajo** -- Lo divide en fases con hitos claros para que puedas seguir el avance.
4. **Realiza el trabajo** -- Claude te ayuda a ejecutar cada fase, revisando la calidad durante el proceso.
5. **Retoma donde te quedaste** -- Todo queda guardado. Inicia una sesión nueva y continúa exactamente donde te detuviste.

Esto funciona para cualquier trabajo estructurado: una funcionalidad de software, un proceso de negocio, un plan de contratación, un rediseño de menú, un modelo de presupuesto o una migración de red. No es solo para programar.

---

## ¿Usar Codex o Claude Code?

Elige tu asistente para trabajar sobre la misma estructura de notas y proyectos.
Ambas rutas permiten conversar en español y conservan las habilidades en inglés.

| Opción | Qué incluye esta edición | Por dónde empezar |
|--------|--------------------------|-------------------|
| **Claude Code** | Las 49 habilidades originales del kit y la configuración de Tamarindos. | Sigue [Primeros pasos](#primeros-pasos) y [SETUP.md](SETUP.md). |
| **Codex** | 13 adaptadores para configuración inicial, notas, avances, pendientes, cierre de sesión y trabajo estructurado. | Sigue [Usar Tamarindos con Codex](CODEX.md). |

### Si eliges Claude Code

Continúa con la guía original traducida que aparece más abajo. Sus comandos
`/setup`, `/orient`, `/pickup` y demás corresponden a Claude Code.

### Si eliges Codex

Crea tu copia mediante **Use this template**, descárgala y abre la carpeta en Codex.
Las habilidades están incluidas en `.agents/skills/`; no necesitas copiarlas
manualmente ni instalar Claude Code.

Escribe:

> Configura mi espacio de Tamarindos en español.

También puedes usar `$wfk-setup`. Codex te preguntará los datos que falten y
preparará tu perfil, notas y primer pendiente. Consulta [CODEX.md](CODEX.md) para
la instalación, los comandos disponibles y las comprobaciones de una copia nueva.

Obsidian funciona con ambas opciones. Los documentos guardados permiten retomar
el trabajo con otro asistente; el historial del chat no se transfiere automáticamente.

**Alcance de Codex:** esta edición adapta 13 flujos. Las demás habilidades,
incluidas las integraciones externas y `/update-wfk`, no se presentan como
compatibles. Consulta el [estado de validación](05_System/Workflows/REF%20-%20Codex%20Validation.md).

---

## Primeros pasos

### Qué necesitas

- **macOS o Windows**.
- **Una terminal moderna** -- **[Warp](https://www.warp.dev)** en macOS (gratuita, con pestañas y funciones de IA) o **[Windows Terminal](https://aka.ms/terminal)** en Windows (gratuita, con pestañas). También funcionan la Terminal predeterminada de macOS y el Símbolo del sistema de Windows.
- **[Claude Code](https://www.claude.com/product/claude-code)** -- la herramienta de terminal o línea de comandos (no Claude Desktop, que es una aplicación de chat separada). Requiere una suscripción de Claude (Pro de $20 USD al mes o Max de $100 USD al mes). Instálalo con:
  ```bash
  npm install -g @anthropic-ai/claude-code
  ```
  Después de instalarlo, reinicia la terminal y escribe `claude --version` para confirmar. Si aparece «command not found», consulta [Solución de problemas](#solución-de-problemas-de-configuración) más abajo.
- **[Obsidian](https://obsidian.md)** instalado (aplicación gratuita para tomar notas).
- **Git** -- en macOS, abre la terminal y escribe `git` para comprobarlo (se instala automáticamente). En Windows, descárgalo de [git-scm.com](https://git-scm.com).

> **Importante:** Claude Code y Claude Desktop son productos diferentes. Claude Desktop es una aplicación de chat. Claude Code es una herramienta de terminal que lee tus archivos y ejecuta comandos. Necesitas Claude Code para este sistema. Si solo tienes Claude Desktop instalado, [instala Claude Code](https://www.claude.com/product/claude-code) por separado.

### Cuánto cuesta

Workflow Kit es gratuito. El único costo es tu suscripción de Claude (Pro de $20 USD al mes o Max de $100 USD al mes). Para ponerlo en perspectiva: una persona que realiza trabajo habitual de productividad apenas consume una parte de lo que permite la suscripción. Con precios de API, ese mismo trabajo costaría miles al mes. La suscripción es una gran oferta para este tipo de uso.

> **Nota sobre los límites de uso:** La exploración inicial de `/setup` es la operación individual más exigente. Con el plan Pro ($20 USD al mes), podrías acercarte a tu límite de uso durante una primera sesión intensiva. Si llegas al límite, espera a que se restablezca y continúa. El plan Max ($100 USD al mes) tiene límites más altos y se recomienda para un uso diario intensivo.

### Paso 1: Crea un fork y descarga la bóveda

Primero, [crea un fork de este repositorio](https://github.com/braincandy-parallel/tamarindos-workflow-kit/fork) en GitHub. Esto crea tu propia copia, bajo tu control.

Después, clona **tu fork** (sustituye `your-github-username` por tu nombre de usuario real de GitHub):

**macOS** -- Abre Terminal y pega:
```bash
git clone https://github.com/your-github-username/tamarindos-workflow-kit.git ~/Documents/Vaults/Work\ Vault
```

**Windows** -- Abre la terminal y pega:
```cmd
git clone https://github.com/your-github-username/tamarindos-workflow-kit.git "%USERPROFILE%\Documents\Vaults\Work Vault"
```

> **Sustituye `your-github-username`** por tu nombre de usuario real de GitHub. Por ejemplo, si tu usuario de GitHub es `jsmith`, la URL será `https://github.com/jsmith/tamarindos-workflow-kit.git`. Si recibes un error 404, comprueba que creaste el fork del repositorio y escribiste correctamente tu usuario.

Si el sistema no reconoce `git`, instálalo primero desde [git-scm.com](https://git-scm.com) y después reinicia la terminal.

Esto crea una carpeta llamada `Work Vault` dentro de tus Documentos. Esa carpeta **es** tu espacio de trabajo.

### Paso 2: Instala las habilidades

Claude Code necesita que las habilidades estén instaladas para que funcione `/setup`. En tu terminal:

**macOS:**
```bash
cp -r ~/Documents/Vaults/Work\ Vault/skills/* ~/.claude/skills/
```

**Windows:**
```cmd
xcopy /E /I "%USERPROFILE%\Documents\Vaults\Work Vault\skills\*" "%USERPROFILE%\.claude\skills\"
```

Esto copia todas las carpetas de habilidades al directorio de habilidades de Claude Code. Solo necesitas hacerlo una vez. Después, `/update-wfk` se encarga de las futuras actualizaciones.

### Paso 3: Ábrela en Obsidian

1. Abre Obsidian.
2. Haz clic en «Open folder as vault» (Abrir carpeta como bóveda).
3. Ve a `Work Vault` dentro de tus Documentos.
4. Haz clic en **Trust** (Confiar) cuando se te solicite; esto habilita los complementos preconfigurados.

Verás una barra lateral con carpetas como `01_Notes`, `02_Projects`, etc. Ya están configuradas para ti.

> **Nota sobre los complementos:** La plantilla de nota diaria utiliza la función [Bases](https://help.obsidian.md/bases) de Obsidian (integrada desde Obsidian 1.9) para mostrar especificaciones, reportes y pendientes recientes. Si usas una versión anterior de Obsidian, estas secciones mostrarán la sintaxis de inserción en lugar de tablas. Actualiza Obsidian a la versión más reciente para obtener la mejor experiencia.

### Comprobación previa

Antes de continuar, verifica que todo esté en su lugar:

- [ ] `git --version` devuelve un número de versión.
- [ ] `claude --version` devuelve un número de versión; si no, consulta [Solución de problemas](#solución-de-problemas-de-configuración).
- [ ] `ls ~/.claude/skills/orient/SKILL.md` muestra el archivo; las habilidades están instaladas.
- [ ] Obsidian muestra `Work Vault` con `01_Notes`, `02_Projects`, etc.

Si falla alguna comprobación, resuélvela antes de continuar. La exploración de `/setup` requiere las cuatro.

### Paso 4: Configura Claude

Abre la terminal y ve a la bóveda:

**macOS:**
```bash
cd ~/Documents/Vaults/Work\ Vault
claude --dangerously-skip-permissions
```

**Windows:**
```cmd
cd "%USERPROFILE%\Documents\Vaults\Work Vault"
claude --dangerously-skip-permissions
```

> La opción `--dangerously-skip-permissions` permite que Claude funcione sin pedir permiso para cada lectura de archivo y comando. Se recomienda durante la configuración porque la exploración lee muchos archivos y las solicitudes de permiso la vuelven muy tediosa. Después de la configuración, puedes ejecutar `claude` sin esta opción si prefieres las solicitudes de aprobación.

Después escribe:

```
/setup
```

Claude te preguntará tu nombre y después explorará tus archivos y herramientas instaladas para entender tu trabajo y configurarlo todo. Tarda aproximadamente 5 minutos.

### Paso 5: Inicia tu primer proyecto

Después de la configuración, escribe:

```
/pickup
```

Esto muestra tres tareas iniciales que te enseñan el sistema mientras lo usas:

| Tarea | Qué aprenderás |
|------|----------------|
| **Personalizar tu perfil** | Cómo adaptar el sistema a tu forma específica de trabajar. |
| **Incorporar tus archivos** | Cómo organizar tu trabajo existente dentro de la bóveda. |
| **Tu primera especificación** | El flujo principal: describir lo que quieres construir y hacer que Claude lo planifique. |

Complétalas en orden. Al terminar, entenderás cómo encaja todo.

---

## Cómo funciona en el día a día

### Hábitos diarios

| Cuándo | Qué escribir | Qué sucede |
|--------|--------------|------------|
| Al comenzar el día | `/orient` y después `/pickup` | Carga tu contexto y muestra qué sigue. |
| Mientras trabajas | Simplemente habla con Claude | Registra automáticamente lo que estás haciendo. |
| Nueva tarea estructurada | `/create-spec` | Te guía para definir lo que quieres. |
| Registrar avances | `/log-work` | Registra lo que lograste. |
| Al terminar el día | `/closeout` | Guarda tu avance para mañana. |

### Al comenzar el día

Abre Claude en el directorio de tu bóveda y escribe `/orient`. Esto carga tu contexto: en qué estabas trabajando, qué está pendiente y qué sigue. Después escribe `/pickup` para retomar donde te quedaste.

### Al trabajar en algo nuevo

Dile a Claude lo que quieres hacer. Te guiará a lo largo del proceso:

1. **«Quiero…»** -- Claude te entrevista sobre la idea, hace preguntas aclaratorias y redacta una descripción clara de lo que intentas lograr (una especificación o *spec*).
2. **Revisión** -- Antes de comprometerte a construirlo, Claude busca problemas en la especificación. ¿Hay vacíos? ¿Cosas que podrían salir mal? ¿Conflictos con otro trabajo?
3. **Plan** -- Claude divide el trabajo en fases. Cada fase entrega algo que realmente puedes ver y comprobar, no solo trabajo invisible en segundo plano.
4. **Construcción** -- Claude te ayuda a ejecutar cada fase. Para proyectos de código, despliega equipos de agentes de IA. Para otros trabajos, te guía por los pasos y da seguimiento al avance.
5. **Revisión del resultado** -- Al terminar, Claude revisa la calidad de lo producido.

No tienes que usar todos los pasos. Para tareas pequeñas, simplemente dile a Claude lo que quieres y determinará el nivel de proceso adecuado.

### Al terminar el día

Escribe `/closeout`. Claude registra en qué trabajaste y crea documentos de tipo *pickup*: archivos de contexto que te permiten a ti, o a una futura sesión de Claude, retomar exactamente donde te detuviste. Se acabaron los momentos de «¿En qué me había quedado?».

Piensa en los pickups como una extensión de tu memoria. Cuando estás atendiendo 10 cosas y tu cabeza no puede retener todos los detalles, el pickup los guarda por ti. Al terminar el día, cierras todo; por la mañana, cargas exactamente el contexto que necesitas.

### Sistema de reportes periódicos

Una de las funciones principales del kit es un sistema automatizado de reportes que mantiene a Claude orientado entre sesiones sin que tengas que volver a explicar nada. Produce documentos con tres frecuencias (diaria, semanal y mensual), cada una con un reporte de lo ocurrido y una hoja de ruta para lo que viene.

| Frecuencia | Retrospectiva: qué ocurrió | Próximos pasos: en qué enfocarse |
|------------|---------------------------|--------------------------------|
| Diaria | **EOD** (End of Day: cierre del día) | **SOD** (Start of Day: inicio del día) |
| Semanal | **EOW** (End of Week: cierre de la semana) | **WRM** (Weekly Roadmap: hoja de ruta semanal) |
| Mensual | **EOM** (End of Month: cierre del mes) | **MRM** (Monthly Roadmap: hoja de ruta mensual) |

**Cómo funciona en la práctica:**

- `/closeout` registra tu sesión y crea pickups.
- `/end-day` reúne todas tus sesiones en un reporte EOD y después genera el SOD de mañana.
- Los viernes, `/end-day` también produce un EOW y un WRM que establece 3 metas para la semana siguiente.
- El último día laborable del mes, produce un EOM y un MRM que establece entre 3 y 5 objetivos para el nuevo mes.

Cuando inicias una sesión con `/orient`, Claude lee el SOD de hoy, el WRM vigente y el MRM vigente. Esto le da tres capas de contexto: qué hacer hoy, de qué trata esta semana y qué busca optimizar este mes. Nunca tienes que volver a explicar tus prioridades.

**El ciclo de aprendizaje:** Cada reporte retrospectivo (EOD, EOW, EOM) incluye una sección de retrospectiva donde las observaciones se etiquetan con una «zona de destino»: el lugar específico donde ese hallazgo produce un cambio permanente, como una nueva regla, una mejora de una habilidad o un ajuste de una meta. Esto hace que los patrones que detectas cambien realmente el comportamiento del sistema, en lugar de quedar documentados y olvidados.

### Comandos principales

| Qué quieres hacer | Qué escribir |
|-------------------|--------------|
| Iniciar una sesión | `/orient` |
| Retomar trabajo anterior | `/pickup` |
| Crear cualquier documento | `/create-note` (detecta el tipo, o puedes especificar: SD, SPC, PIC, MN, PD, PLN, DD, SO, RE, EB) |
| Capturar una idea | `/create-note PD` |
| Iniciar un proyecto nuevo | `/create-note SPC` |
| Planificar el trabajo | `/create-note PLN` |
| Delimitar primero el alcance | `/bracket` |
| Ejecutar el plan | `/implement` |
| Control de calidad del flujo con tres funciones | `/qa-coord` |
| Hoja de ruta mensual y semanal | `/roadmap` |
| Reporte y contexto del cierre del día | `/end-day` |
| Investigar un campo antes de diseñar | `/oracle-create` |
| Hacer una pregunta de diseño al oráculo | `/oracle-ask` |
| Evaluar opciones de código abierto antes de la SPC | `/landscape-survey` |
| Definir los principios de un sistema | `/create-note SD` |
| Registrar lo que hiciste | `/log-work` |
| Entender un documento o tema | `/explain` |
| Crear notas de reunión | `/create-note MN` |
| Extraer lecciones de esta sesión | `/distill-lessons` |
| Generar un prototipo de interfaz a partir de una especificación | `/prototype` |
| Organizar archivos que llegan | `/intake` |
| Guardar contexto para después | `/park` |
| Terminar tu día | `/closeout` |
| Ver qué habilidades pueden ayudarte | `/discover` |

### También puedes simplemente conversar

Los comandos con barra diagonal no son la única forma de interactuar. Claude entiende el lenguaje natural:

- «Tuve una reunión con el equipo sobre la revisión del presupuesto» (Claude crea notas de reunión).
- «¿En qué debería trabajar ahora?» (Claude revisa tus pickups y prioridades).
- «Quiero crear un formulario de registro de clientes para mi negocio de consultoría» (Claude te guía por el proceso de especificación).
- «¿Puedes explicarme cómo funciona el flujo de especificaciones?» (Claude consulta los documentos de tu bóveda).
- «Organiza estos archivos que acabo de descargar» (Claude los clasifica dentro de la estructura de tus proyectos).

| Qué quieres hacer | Qué escribir |
|-------------------|--------------|
| Revisar trabajo terminado | `/retro` |
| Ver qué habilidades pueden ayudarte | `/discover` |
| Revisar tu lista de pendientes | `/pickup` (muestra una clasificación de prioridades cuando existen varios PIC) |

### Cuando algo sale mal

Si Claude parece atascado o sigue intentando la misma solución repetidamente, escribe `/troubleshoot`. Esto activa un modo de diagnóstico que se detiene, investiga la causa raíz y propone una solución específica en lugar de adivinar.

### Cómo se acumula el valor de tu trabajo

Cada proyecto tiene un **registro de proyecto** (`PJL - <Project>.md`) que crece entre sesiones. Cuando vuelves a un proyecto, Claude lee el PJL y sabe qué se construyó, qué decisiones se tomaron, qué falló y qué está desplegado. Cuanto más usas el sistema, más rápido se pone Claude al día con tus proyectos.

---

## Grabación y transcripción

Si tienes un dispositivo de grabación, como un colgante Omi o la grabadora de tu teléfono, el sistema puede convertir automáticamente tus conversaciones en notas estructuradas.

El flujo de trabajo:

1. Graba una conversación, reunión o visita a un sitio.
2. Entrega la transcripción a Claude con `/create-MN`.
3. Claude genera notas de reunión estructuradas: temas, decisiones y acciones pendientes.
4. Las notas se guardan en tu bóveda, se enlazan con tu nota diaria y se pueden buscar.

Esto resulta muy útil para:

- **Reuniones** -- Deja de tomar notas manuales. En su lugar, revisa y corrige las notas generadas automáticamente.
- **Visitas a sitios** -- Narra lo que ves: inventario de dispositivos, investigación de incidentes o hallazgos de una inspección. Claude lo transcribe y estructura.
- **Sesiones con gerencia** -- Graba una conversación de 30 minutos en la que tu jefe da 15 indicaciones. Claude las captura todas, las clasifica según tu trabajo activo y no se pierde nada.

El principio es sencillo: **graba todo y estructúralo después.** Cada conversación es una posible fuente de contexto. No necesitas saber de antemano qué será útil; simplemente captúralo y el sistema permitirá encontrarlo.

---

## Trabajar con conocimiento de tu área

### Primero el contexto, después la acción

El principio más importante de todos: **nunca supongas que Claude conoce tu área.** Sonará seguro incluso cuando esté equivocado. Si administras routers MikroTik, no le pidas a Claude que configure uno sin antes proporcionarle la topología de tu red, el inventario de dispositivos y las secciones pertinentes del manual.

Construye el contexto de tu área de esta manera:

1. **Descarga manuales y documentos de referencia.** Convierte los PDF a Markdown; Claude puede ayudarte. Markdown es mucho más rápido y preciso para la IA que PDF.
2. **Graba tus visitas a sitios.** Narra lo que encuentres. Las transcripciones se convierten en archivos de contexto.
3. **Crea inventarios.** Enumera tus dispositivos, cuentas, proveedores y procesos. Estos archivos se convierten en la base sobre la que trabaja la IA.
4. **Guarda tus decisiones.** Cuando elijas el enfoque A sobre el B, documenta por qué. Las sesiones futuras no volverán a debatir preguntas ya resueltas.

### Markdown antes que PDF

Prefiere siempre Markdown (`.md`) a PDF para el procesamiento con IA. Los PDF con diagramas, tablas y formatos complejos son poco fiables para los modelos de lenguaje. Las líneas y las relaciones espaciales se distorsionan. Markdown es texto plano con formato sencillo y los modelos de lenguaje lo procesan perfectamente.

Si tienes un PDF importante, como un manual de proveedor, un documento de cumplimiento o una especificación técnica, conviértelo primero a Markdown. Claude puede ayudarte: «Convierte este PDF en una serie de archivos Markdown». Después, utiliza la versión Markdown como referencia en tu bóveda.

---

## Tu bóveda

Todo se guarda en carpetas organizadas:

| Carpeta | Qué se guarda aquí |
|---------|--------------------|
| **01_Notes** | Notas diarias, notas de reuniones, resúmenes semanales y documentos pickup. |
| **02_Projects** | Tus proyectos; cada uno tiene su propia carpeta con especificaciones, planes y reportes. |
| **03_Operations** | Contenido operativo específico de tu área. |
| **04_Reference** | Conocimiento duradero: guías, decisiones y procedimientos operativos. |
| **05_System** | Plantillas y configuración del flujo de trabajo. |

### Proyectos

Cuando inicias un proyecto nuevo, Claude crea automáticamente una estructura de carpetas:

```
02_Projects/my-project/
  specs/          -- Lo que intentas hacer
  plans/          -- Cómo lo harás, dividido en fases
  reports/        -- Análisis e investigación
  reviews/        -- Revisiones de calidad
  CLAUDE.md       -- Instrucciones de IA específicas de este proyecto
  lessons.md      -- Lo que has aprendido durante el proceso
```

No necesitas crear esto manualmente; Claude se encarga cuando ejecutas `/create-spec`.

### Nombres de archivos

Cada documento comienza con un prefijo corto para que siempre puedas identificar de qué se trata de un vistazo:

| Prefijo | Qué significa |
|---------|---------------|
| `DN` | Nota diaria. |
| `MN` | Nota de reunión. |
| `SPC` | Especificación: lo que estás construyendo. |
| `PL` | Plan: cómo lo construirás. |
| `PIC` | Pickup: contexto para retomar el trabajo. |
| `RE` | Reporte. |
| `PJL` | Registro de proyecto: historial de trabajo. |
| `WL` | Registro de trabajo: registro detallado de la sesión. |
| `REF` | Referencia: conocimiento permanente. |
| `RET` | Retrospectiva: qué salió bien y qué salió mal. |

---

## Adaptarlo a tu trabajo

### Hacerlo tuyo

Durante la configuración, el sistema explora tu computadora para detectar qué tipo de trabajo realizas y adapta la bóveda en consecuencia: las secciones de las notas diarias, los prefijos de archivos y la estructura de proyectos se ajustan a tu función. El primer pickup de bienvenida te ayuda a afinarlo aún más.

El sistema se adapta con el tiempo:

- **Lecciones** -- Cuando Claude aprende algo sobre cómo funciona tu trabajo, como una herramienta que no se comporta según lo esperado o un proceso que necesita un paso adicional, lo guarda como una lección. Las sesiones futuras leen esas lecciones y evitan repetir los mismos errores.
- **Configuraciones de agentes** -- Cada proyecto tiene un archivo `CLAUDE.md` donde Claude guarda contexto específico del proyecto. Esto permite que Claude recuerde las tecnologías utilizadas, las convenciones y los detalles problemáticos de cada proyecto.
- **Pickups** -- Cada vez que dejas de trabajar, el contexto se guarda. Cuando regresas, Claude lee el pickup y sabe exactamente dónde estabas y qué sigue.

### Añadir tus propias habilidades

Las habilidades son como recetas guardadas para Claude: flujos de trabajo repetibles que puedes activar con un comando de barra diagonal. Cada corrección que haces y cada mejora que encuentras se guarda en la habilidad para que no tengas que repetirla. Puedes crear las tuyas:

1. Escribe `/skill-creator` y describe lo que quieres que haga la habilidad.
2. Claude escribe la habilidad, la prueba y la instala.
3. Ahora puedes activarla con `/your-skill-name` en cualquier momento.

---

## Mantenerte al día

Para obtener las mejoras más recientes:

```
/update-wfk
```

Esto descarga nuevas habilidades y plantillas actualizadas desde este repositorio. Tus archivos personales y los datos de tus proyectos nunca se modifican; solo se actualizan las herramientas del flujo de trabajo.

---

## Contribuir

¿Encontraste un error o tienes una mejora? Ejecuta `/update-wfk contribute` y Claude se encargará de crear el fork, la rama y el pull request por ti.

**Nota sobre autenticación:** Los tokens de acceso personal de GitHub con permisos detallados (*fine-grained PATs*) no pueden crear pull requests en repositorios que pertenecen a otros usuarios. La acción de contribución utiliza OAuth de `gh` en su lugar. Si todavía no lo has hecho, ejecuta `gh auth login` en tu terminal antes de contribuir. Esta es una limitación de la API de GitHub, no un problema de WFK.

También puedes abrir incidencias en [github.com/braincandy-parallel/tamarindos-workflow-kit/issues](https://github.com/braincandy-parallel/tamarindos-workflow-kit/issues) para reportar errores o sugerir funciones.

---

## Solución de problemas de configuración

| Problema | Solución |
|----------|----------|
| `claude: command not found` | Reinicia la terminal. Si no funciona, vuelve a ejecutar `npm install -g @anthropic-ai/claude-code` y después cierra y vuelve a abrir la terminal. En macOS, puede que necesites añadir el directorio global de ejecutables de npm a tu PATH: añade `export PATH="$HOME/.npm-global/bin:$PATH"` a tu archivo `~/.zshrc`. |
| La clonación devuelve 404 | Asegúrate de haber creado primero el fork del repositorio y de haber sustituido `your-github-username` en la URL de clonación por tu usuario real de GitHub. |
| `git: command not found` | Instala Git desde [git-scm.com](https://git-scm.com) y después reinicia la terminal. |
| Obsidian muestra una bóveda vacía | Asegúrate de haber abierto la carpeta `Work Vault`, no una carpeta superior. Ve a File > Open Vault > Open folder (Archivo > Abrir bóveda > Abrir carpeta) y selecciona `Work Vault`. |
| `/setup` indica «skills not found» | Repite el Paso 2, el comando `cp -r`. Las habilidades deben estar en `~/.claude/skills/` para que funcione `/setup`. |
| Alcanzaste tu límite de uso durante la configuración | Espera a que se restablezca el límite; consulta tu página de cuenta de Claude para ver cuándo. La exploración de `/setup` es la operación individual más exigente. Después de configurar el sistema, el uso normal es mucho más ligero. |
| Errores de permiso denegado | Asegúrate de ser el propietario del directorio de la bóveda. En macOS, `ls -la ~/Documents/Vaults/` debe mostrar tu usuario como propietario. |

## Licencia

MIT

---

Traducción íntegra al español del [README de Workflow Kit de Holden Greene](https://github.com/hgreene624/workflow-kit/blob/72bd42694fface86fc3af73b464631c6a5308464/README.md), adaptada en nombre y enlaces de repositorio para Tamarindos. Las habilidades y los comandos se conservan en inglés.
