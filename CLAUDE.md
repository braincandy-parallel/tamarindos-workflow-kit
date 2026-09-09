# Tamarindos: instrucciones para Claude Code

Lee también las reglas compartidas de `AGENTS.md`. Su sección Codex se aplica únicamente a Codex.

<!-- WFK:START - Session Startup -->
## Inicio de sesión

Al iniciar una conversación, ejecuta `/orient`. En una copia nueva sin configurar, sigue primero `SETUP.md`; no trates la falta de reportes o habilidades instaladas como un error.
<!-- WFK:END -->

<!-- WFK:START - Core Behavior -->
## Comportamiento

- Registra únicamente hechos expresados o verificados. No inventes detalles.
- Cuando falte información, pregunta o déjala pendiente.
- Guarda instrucciones en `agents.md` o referencias, fuera del contenido operativo.
- Usa `AskUserQuestion` para preguntar, una pregunta a la vez. Si la herramienta no existe en el entorno, pregunta directamente.
- Verifica documentos, sintaxis y configuración antes de modificar.
- Cambia solo lo necesario para la tarea.
- Prepara un plan antes de delegar una implementación.
- Si descubres un problema, resuélvelo dentro del alcance o acuerda un pendiente con el usuario.
- Revisa los elementos obsoletos después de un cambio. Antes de eliminarlos, confirma que pertenecen al cambio y que es seguro hacerlo.
<!-- WFK:END -->

<!-- WFK:START - Agent Teams -->
## Equipos de agentes

Cuando una tarea requiera varios agentes y el entorno disponga de Agent Teams, utiliza un equipo visible con `TeamCreate` y coordina mediante `SendMessage`. No presupongas que tmux o estas herramientas están instalados. Si no están disponibles, realiza la tarea de forma secuencial.
<!-- WFK:END -->

<!-- WFK:START - File Prefix Conventions -->
## Prefijos

| Prefijo | Tipo |
|---|---|
| DN | Nota diaria |
| MN | Minuta de reunión |
| SPC | Especificación |
| PL | Plan |
| RE | Reporte |
| PIC | Pendiente con contexto para retomar |
| PJL | Registro de proyecto |
| REF | Referencia |
| RET | Retrospectiva |
| WL | Registro de trabajo |
| WS | Resumen semanal |
| IN | Iniciativa |
| QA | Revisión de calidad |
| ARE | Reporte de agente |
| DD | Discusión de diseño |
| SO | Esquema de estructura |
| HAN | Entrega de contexto |

Usa los prefijos de las plantillas y habilidades originales. No inventes nuevos prefijos sin confirmar su necesidad. Los documentos de entrada del repositorio, como README.md, SETUP.md, WORKFLOW.md, CLAUDE.md y agents.md, conservan sus nombres técnicos.
<!-- WFK:END -->

<!-- WFK:START - Vault Structure -->
## Estructura

- `01_Notes/`: notas diarias, reuniones, resúmenes, pendientes y reportes periódicos.
- `02_Projects/`: documentación de proyectos.
- `03_Operations/`: documentación operativa.
- `04_Reference/`: referencias, decisiones y procedimientos.
- `05_System/`: plantillas y flujos de trabajo.

Conserva los nombres de las carpetas para mantener compatibilidad.
<!-- WFK:END -->

<!-- WFK:START - Routing Rules -->
## Ubicación de documentos

| Contenido | Ruta |
|---|---|
| Nota diaria | `01_Notes/Daily/DN - YYYY-MM-DD.md` |
| Minuta | `01_Notes/Meetings/MN - YYYY-MM-DD (Tema).md` |
| Resumen semanal | `01_Notes/Weekly/` |
| Pendiente | `01_Notes/Pickups/PIC - Tema.md` |
| Registro de trabajo | `01_Notes/Work Logs/WL - Tema.md` |
| Especificación | `02_Projects/<proyecto>/specs/YYYY-MM-DD/SPC - Nombre.md` |
| Plan | `02_Projects/<proyecto>/plans/YYYY-MM-DD/PL - Nombre.md` |
| Reporte | `02_Projects/<proyecto>/reports/YYYY-MM-DD/RE - Nombre.md` |
| Revisión | `02_Projects/<proyecto>/reviews/YYYY-MM-DD/` |
| Referencia | `04_Reference/REF - Nombre.md` |
| Decisiones de arquitectura | `04_Reference/ADR/` |
| Procedimientos | `04_Reference/Runbooks/` |
| Plantillas | `05_System/Templates/` |
<!-- WFK:END -->

<!-- WFK:START - Required Frontmatter -->
## Metadatos

Las notas operativas llevan YAML con `date created`, `tags` y `category`. Conserva las claves y valores técnicos requeridos por la plantilla, como `Meeting`, `Report`, `Reference` o `Pickup`. Los reportes y planes pueden añadir los campos indicados por su habilidad.
<!-- WFK:END -->

<!-- WFK:START - Standard Project Structure -->
## Proyectos

Cada proyecto contiene `specs/`, `plans/`, `reports/`, `reviews/`, `agents.md` y `lessons.md`. Guarda los documentos de las cuatro primeras carpetas en subcarpetas con su fecha de creación `YYYY-MM-DD`.
<!-- WFK:END -->

<!-- WFK:START - Daily Note Formatting -->
## Nota diaria

Organiza la sección `Worked on` con subtítulos por tema y viñetas. Coloca lo más reciente arriba. Conserva el encabezado técnico cuando la habilidad lo necesite; escribe las entradas en español.
<!-- WFK:END -->

<!-- WFK:START - Wikilinks -->
## Enlaces

Usa wikilinks con el nombre del archivo: `[[RE - Seguimiento de acuerdos]]`. Evita rutas completas cuando el nombre sea único. Se permite texto de presentación: `[[RE - Seguimiento de acuerdos|Seguimiento]]`.
<!-- WFK:END -->

<!-- WFK:START - Agent Files -->
## Contexto de proyecto

Lee los archivos `agents.md` y `lessons.md` del proyecto antes de trabajar. Trátalos como instrucciones y contexto del proyecto.
<!-- WFK:END -->

<!-- WFK:START - Git Safety -->
## Git

Antes de operaciones que modifiquen el estado de Git, sigue `/git-safe`. Diferencia la plantilla pública, la copia personal y el origen de actualizaciones. Nunca presupongas que guardar una nota equivale a subirla a GitHub.
<!-- WFK:END -->

<!-- WFK:START - Post-Compaction Recovery -->
## Recuperar contexto

Después de compactar la conversación, vuelve a leer este archivo antes de continuar.
<!-- WFK:END -->

<!-- WFK:START - Rules That Survive Compaction -->
## Reglas persistentes

- Comprueba el estado técnico antes de afirmarlo. Si no lo sabes, indícalo.
- Consulta archivos antes de preguntar algo que puedas verificar.
- Usa lenguaje claro y párrafos breves.
- No cambies pestañas ni configuración del terminal sin solicitud.
<!-- WFK:END -->

<!-- LOCAL:START - Tamarindos -->
## Idioma y adaptación Tamarindos

`wfk_role: user`

Estas reglas locales se aplican también al seguir habilidades en inglés y deben conservarse al actualizar el kit.

- Comunícate en español desde el inicio, aunque el sistema operativo esté en inglés. Cambia de idioma solo si el usuario lo solicita.
- Redacta explicaciones, preguntas, resúmenes, títulos y contenido de documentos en español.
- Mantén los nombres de habilidades, comandos, archivos de sistema, claves YAML/JSON, valores de estado y encabezados exigidos por automatizaciones. No traduzcas identificadores que rompan referencias.
- Interpreta solicitudes en español por su intención y utiliza la habilidad pertinente aunque su descripción esté en inglés. Respeta las restricciones de invocación manual de cada habilidad.
- Las habilidades y sus archivos de apoyo permanecen en inglés. No los traduzcas para responder en español.
- Esta es una plantilla para Tamarindos. No contiene el perfil real de quien la descarga. En onboarding, pregunta nombre, función y necesidad más urgente.
- No asumas que los ejemplos de Flora, VPS, redes u otras organizaciones en las habilidades describen a Tamarindos. Verifica su pertinencia.
- En una instalación nueva sigue `SETUP.md`. Antes de explorar fuera de la carpeta, confirma el alcance; antes de reemplazar habilidades personales distintas, consulta.
- Resuelve los marcadores de repositorio de las habilidades según el contexto. La distribución es `braincandy-parallel/tamarindos-workflow-kit`; la copia personal se identifica por su remoto. Consulta la guía de actualizaciones antes de `/update-wfk`.

### Solicitudes en español y habilidades

| Intención | Habilidad |
|---|---|
| «Ponme al día», «vamos a comenzar» | `orient` |
| «Retomemos», «qué pendientes tengo» | `pickup` |
| «Crea una minuta», «estos fueron los acuerdos» | `create-note MN` |
| «Prepara un reporte» | `create-note RE` |
| «Definamos esta mejora» | `create-note SPC` |
| «Hagamos el plan» | `create-note PLN` |
| «Registra lo que hicimos» | `log-work` |
| «Explícame esto» | `explain` |
| «Guarda este contexto para después» | `park` |
| «Terminamos por hoy», «cerremos la sesión» | `closeout` |

Elige según la intención y el contexto, no solo palabras aisladas. Ante ambigüedad relevante, pregunta. Las menciones heredadas a `/create-spec` y `/create-plan` corresponden a `/create-note SPC` y `/create-note PLN`.
<!-- LOCAL:END -->

## Notion: colaboración opcional

Si existe .notion/config.json con auto_publish activado, al registrar avances o cerrar
la sesión sigue scripts/NOTION-WORKFLOW.md después de guardar el trabajo local.
Consulta NOTION.md para instalar la conexión y entender sus límites.
