# Tamarindos Workflow Kit

**Un sistema de productividad personal que une Claude Code (inteligencia artificial) y Obsidian (notas) en un espacio donde tú y la IA trabajan con los mismos archivos, el mismo contexto y el mismo historial. Todo en español.**

Aquí puedes investigar, organizar información, tomar decisiones, planificar mejoras y dar seguimiento al trabajo de Tamarindos. Lo que documentas hoy queda disponible para las próximas sesiones.

Basado en [Workflow Kit de Holden Greene](https://github.com/hgreene624/workflow-kit). Las habilidades (*skills*) y los comandos se conservan en inglés; la bienvenida y la conversación son en español.

## ¿Por qué existe?

Cuando trabajas con IA únicamente dentro de una conversación, mantener la continuidad se vuelve difícil. El chat crece, los detalles importantes quedan enterrados y, al abrir una sesión nueva, puedes terminar explicando otra vez el problema, las decisiones y lo que ya habías avanzado.

Workflow Kit da continuidad a ese trabajo mediante una carpeta compartida entre tú y Claude. Esa carpeta, llamada **bóveda** en Obsidian, contiene archivos de texto: notas, acuerdos, planes, reportes, pendientes y lecciones. Tú puedes leerlos y editarlos en Obsidian; Claude Code puede consultarlos y actualizarlos cuando trabajan juntos.

El contexto queda en tus archivos y puede recuperarse entre sesiones. Por ejemplo, si hace tres semanas definiste un cambio en reservaciones, la siguiente sesión puede consultar el plan, revisar el avance registrado y ayudarte a continuar.

Con el uso, tu espacio reúne más información sobre tu trabajo: qué decidiste, por qué lo decidiste, qué funcionó y qué sigue pendiente. Claude puede apoyarse en ese contexto para ayudarte con mayor continuidad y menos explicaciones repetidas. Esa continuidad depende de guardar los avances y consultar los documentos pertinentes.

El sistema te ayuda a:

- **Conservar el trabajo como archivos organizados**, para que tú y Claude puedan consultarlo después.
- **Construir una base de conocimiento personal mientras trabajas**, al registrar acuerdos, resultados y lecciones durante las tareas.
- **Retomar proyectos después de días o semanas**, recuperando el contexto y los siguientes pasos documentados.
- **Aprovechar la experiencia acumulada**, usando el historial de proyectos y decisiones como referencia para el trabajo nuevo.

Para entender cómo se conectan las notas, los proyectos y las sesiones, consulta [Cómo funciona el trabajo diario](WORKFLOW.md).

## ¿Para quién es?

Para personas que coordinan trabajo, resuelven problemas y necesitan dar seguimiento: responsables de operación, administración, cocina, servicio, reservaciones, mantenimiento, marketing y dirección de Tamarindos.

Es especialmente útil cuando tu trabajo implica investigar, comparar opciones, documentar acuerdos, coordinar responsables o convertir una idea en pasos concretos. Cada persona adapta su copia a su función y sus necesidades.

**No necesitas saber programar.** Necesitas aprender a abrir tu carpeta, escribir algunos comandos en la terminal y organizar archivos. La guía de esta página te acompaña en la instalación; después puedes pedirle ayuda a Claude en español para trabajar paso a paso.

### Ejemplos por función

**Operación y servicio:** Comparte las notas de una incidencia durante el servicio. Claude te ayuda a preparar un reporte con lo ocurrido, las acciones tomadas y los pendientes. Al cierre del mes, puedes pedirle que revise los reportes guardados y resuma los problemas recurrentes.

**Dirección y administración:** Después de una reunión con varios encargos, comparte tus notas o la transcripción. Claude te ayuda a separar los acuerdos, identificar responsables confirmados y registrar lo pendiente. Semanas después, puedes consultar qué ocurrió con cada encargo a partir del seguimiento documentado.

**Cocina e inventarios:** Documenta una revisión de inventario o una propuesta para mejorar un procedimiento. Claude puede organizar los datos que le compartes, ayudarte a definir la mejora y preparar un plan. El historial conserva las decisiones y los resultados registrados para la siguiente revisión.

**Mantenimiento y sistemas:** Registra una visita o revisión con equipos, ubicaciones, modelos y fallas observadas. Claude te ayuda a organizar esa información en fichas y reportes que podrá consultar cuando vuelvas a trabajar en esos equipos.

**Reservaciones y eventos:** Reúne requisitos, acuerdos y cambios de un evento en su carpeta de proyecto. Claude puede revisar ese contexto para preparar una lista de pendientes o ayudarte a retomar la coordinación sin reconstruir toda la conversación.

**Marketing:** Guarda objetivos, propuestas, decisiones y resultados de una campaña. Al preparar la siguiente, Claude puede consultar ese historial y ayudarte a identificar qué repetir, qué cambiar y qué información todavía falta.

Estos ejemplos parten de notas, archivos o transcripciones que compartas. Las conexiones con correo, reservaciones, inventarios, transcripción de audio u otros sistemas se configuran por separado.

## ¿Qué puedes hacer con este sistema?

Describe lo que quieres lograr y Claude te acompaña desde la idea hasta el seguimiento:

1. **Definir el trabajo.** Te hace preguntas para aclarar el problema, el resultado esperado y los límites, y lo organiza en una especificación.
2. **Revisar la propuesta.** El flujo de revisión ayuda a encontrar vacíos, riesgos y preguntas que conviene resolver antes de avanzar.
3. **Preparar un plan.** Divide el trabajo en etapas con pasos y resultados que puedas comprobar.
4. **Hacer el trabajo.** Te ayuda a ejecutar el plan, preparar los documentos necesarios y revisar el avance.
5. **Retomar donde te quedaste.** Guarda el progreso y el contexto pendiente para continuar en otra sesión.

Esto sirve para trabajo estructurado de muchos tipos: mejorar un proceso, organizar una contratación, rediseñar un menú, preparar un presupuesto, planificar mantenimiento o desarrollar una herramienta digital.

Para tareas pequeñas también puedes pedir algo directo, como registrar un acuerdo o explicar un reporte. El nivel de planificación debe corresponder al tamaño de la tarea.

### Empieza con tus propias palabras

| Puedes decir | Para qué sirve |
|---|---|
| «¿Qué pendientes tengo para hoy?» | Consultar trabajo guardado y prioridades. |
| «Tuvimos una reunión de cocina. Estos fueron los acuerdos…» | Preparar una minuta con acuerdos y responsables confirmados. |
| «Quiero mejorar el proceso de reservaciones» | Definir el problema y preparar un plan. |
| «Anota que hoy terminamos el inventario» | Registrar el avance que reportaste. |
| «Guarda este pendiente para mañana» | Conservar contexto para retomarlo. |
| «Explícame este reporte» | Entender un documento con lenguaje claro. |

## 1. Prepara tu computadora

Necesitas una cuenta de GitHub y estas herramientas:

- **Claude Code**, con acceso habilitado en tu cuenta. Sigue la [guía oficial de instalación](https://code.claude.com/docs/en/setup).
- **Git**, para descargar tu copia. [Descargar Git](https://git-scm.com/downloads).
- **Obsidian**, para leer y organizar tus notas. [Descargar Obsidian](https://obsidian.md/download).

Abre Terminal en macOS o PowerShell en Windows y comprueba:

```text
git --version
claude --version
```

Cada comando debe mostrar una versión. Si alguno no se reconoce, termina su instalación y vuelve a abrir la terminal.

## 2. Crea tu propia copia en GitHub

1. Abre [Tamarindos Workflow Kit](https://github.com/braincandy-parallel/tamarindos-workflow-kit).
2. Pulsa **Use this template → Create a new repository**.
3. Elige tu cuenta como propietario y un nombre, por ejemplo `mi-espacio-tamarindos`.
4. Selecciona **Private** para tu espacio de trabajo, donde guardarás tus documentos.
5. Pulsa **Create repository**.

Esta página es la plantilla de distribución. Tu repositorio será una copia independiente. No hay sincronización automática entre las copias del personal.

## 3. Descarga tu copia

Sustituye `TU_USUARIO` y `TU_REPOSITORIO` por los datos de la copia que acabas de crear.

### Windows (PowerShell)

```powershell
New-Item -ItemType Directory -Force -Path "$HOME\Documents\Vaults" | Out-Null
Set-Location "$HOME\Documents\Vaults"
git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git Tamarindos
Set-Location Tamarindos
```

### macOS (Terminal)

```bash
mkdir -p "$HOME/Documents/Vaults"
cd "$HOME/Documents/Vaults"
git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git Tamarindos
cd Tamarindos
```

Si ya existe una carpeta `Tamarindos`, utiliza otro nombre en los dos últimos comandos. Si GitHub pide identificarte, inicia sesión con la cuenta que tiene acceso a tu repositorio privado.

## 4. Inicia la configuración en español

Desde la carpeta que descargaste, ejecuta:

```text
claude
```

Sigue el inicio de sesión de Claude Code y revisa la solicitud de confianza de la carpeta. Después escribe:

> Lee SETUP.md y ayúdame a configurar mi espacio de Tamarindos en español.

Claude te preguntará tu nombre, tu función y qué necesitas resolver primero. También instalará las habilidades del kit y te ayudará a crear tu primer pendiente.

Las habilidades se instalan en tu carpeta personal de Claude Code y estarán disponibles en otros proyectos. Si ya tienes versiones instaladas, Claude revisará las diferencias antes de reemplazarlas.

Al terminar, vuelve a abrir Claude Code desde esta carpeta para cargar las habilidades instaladas. Escribe `/discover` para verlas o `/pickup` para comenzar con tus pendientes.

## 5. Abre tus notas en Obsidian

En Obsidian, selecciona **Abrir carpeta como bóveda** y elige la carpeta `Tamarindos` que descargaste. Puedes revisar los complementos incluidos antes de habilitarlos. Obsidian y Claude Code trabajan sobre los mismos archivos.

## Trabaja en español

Los comandos conservan sus nombres originales. Puedes conversar en español antes y después de usarlos.

| Momento | Lo que puedes decir | Comando directo |
|---|---|---|
| Iniciar | «Ponme al día» | `/orient` |
| Retomar | «Ayúdame a retomar mis pendientes» | `/pickup` |
| Reunión | «Crea una minuta con estos acuerdos» | `/create-note MN` |
| Reporte | «Prepara un reporte con estos datos» | `/create-note RE` |
| Definir una mejora | «Ayúdame a definir esta mejora» | `/create-note SPC` |
| Planificar | «Preparemos un plan de trabajo» | `/create-note PLN` |
| Registrar | «Anota lo que hicimos hoy» | `/log-work` |
| Entender | «Explícame este documento» | `/explain` |
| Guardar contexto | «Guarda esto para después» | `/park` |
| Terminar sesión | «Guarda mi avance y cerremos» | `/closeout` |

La selección automática depende del contexto y de la configuración de cada habilidad. Si Claude no activa la adecuada, usa el comando directo. Las habilidades de invocación manual requieren ese comando. Algunas etiquetas de la interfaz pueden seguir en inglés.

## ¿Dónde se guarda el trabajo?

| Carpeta | Contenido |
|---|---|
| `01_Notes/` | Notas diarias, reuniones, pendientes y reportes periódicos. |
| `02_Projects/` | Proyectos con su contexto, planes y resultados. |
| `03_Operations/` | Procedimientos y documentación operativa. |
| `04_Reference/` | Guías y referencias duraderas. |
| `05_System/` | Plantillas y configuración del flujo de trabajo. |

Los nombres técnicos se conservan para que las habilidades encuentren sus archivos. Los títulos y textos nuevos se redactan en español. Algunos campos técnicos y encabezados se mantienen en inglés por compatibilidad.

## Primera sesión sugerida

Escribe, cambiando los ejemplos por tu situación:

> Trabajo en el área de servicio de Tamarindos. Quiero organizar el seguimiento de los acuerdos de nuestras reuniones. Ayúdame a empezar con un pendiente real y explícame cada paso en español.

Más información: [Configuración inicial](SETUP.md) · [Trabajo diario](WORKFLOW.md) · [Actualizaciones](04_Reference/REF%20-%20Updating%20the%20Workflow%20Kit.md).

## Origen y mantenimiento

Esta adaptación parte de [hgreene624/workflow-kit](https://github.com/hgreene624/workflow-kit). Se conservan las habilidades originales en inglés y sus archivos de apoyo. Tamarindos añade la bienvenida, las instrucciones de idioma y los ejemplos del restaurante. El historial original está en [CHANGELOG.md](CHANGELOG.md).

La plantilla no incluye documentos privados del equipo. Usa tu copia privada para tu trabajo y revisa los archivos antes de subirlos a GitHub. Guardar un archivo localmente no significa que ya esté respaldado en GitHub.

Versión de origen: [72bd42694fface86fc3af73b464631c6a5308464](https://github.com/hgreene624/workflow-kit/commit/72bd42694fface86fc3af73b464631c6a5308464).
