# Reglas del espacio de Tamarindos

<!-- WFK:START - Kit Role -->
## Rol del kit

`wfk_role: user`

La persona que descarga esta plantilla utiliza el kit para su propio trabajo. Las actualizaciones deben conservar su perfil y documentos.
<!-- WFK:END -->

<!-- WFK:START - Core Pipeline -->
## Trabajo estructurado

1. `/create-note SPC`: define el resultado y alcance.
2. `/review-spec`: revisa la especificación.
3. `/create-note PLN`: prepara el plan.
4. `/implement`: ejecuta el plan.

Este flujo sirve para procesos y documentos, además de software. Usa un alcance proporcional a la tarea; una anotación breve no requiere todo el proceso.
<!-- WFK:END -->

<!-- WFK:START - Daily Operations -->
## Operación diaria

- Inicio: `/orient` y `/pickup`.
- Avances: `/log-work`.
- Contexto para después: `/park`.
- Cierre de sesión: `/closeout`.
<!-- WFK:END -->

<!-- WFK:START - File Prefix Conventions -->
## Documentos

Consulta los prefijos y rutas en `CLAUDE.md`. Conserva los identificadores técnicos y redacta el contenido en español.
<!-- WFK:END -->

<!-- WFK:START - Project Structure Enforcement -->
## Proyectos

Usa `specs/`, `plans/`, `reports/` y `reviews/` con subcarpetas de fecha. Cada proyecto tiene `agents.md` y `lessons.md` en su raíz.
<!-- WFK:END -->

<!-- LOCAL:START - Tamarindos -->
## Contexto del equipo

- Organización: Tamarindos, restaurante en Los Cabos.
- Idioma predeterminado: español.
- Perfil de la persona: pendiente de configurar con `SETUP.md`.
- Pregunta la función y la necesidad más urgente antes de proponer una estrategia amplia.
- Las habilidades permanecen en inglés y se eligen por la intención de las solicitudes en español.
- No inventes políticas, menús, precios, responsables, fechas ni conexiones a sistemas.
- Esta plantilla es independiente de los documentos privados de Luca y de las copias del personal.
<!-- LOCAL:END -->

<!-- CODEX:START -->
## Codex: entrada automática

Esta sección se aplica solo a Codex. Para Codex, prevalece sobre las referencias
a comandos o herramientas de Claude en las reglas compartidas.

- Lee `05_System/Workflows/REF - Codex Execution Policy.md` antes de ejecutar un flujo.
- Las habilidades de Codex están en `.agents/skills/` y se cargan desde este repositorio.
- Usa `$wfk-setup` para una solicitud de configuración inicial. Si la persona dice
  «Configura mi espacio de Tamarindos en español», esa es la habilidad pertinente.
- En una sesión normal usa `$wfk-orient` para consultar contexto, sin iniciar
  configuración ni exploración del equipo automáticamente.
- Para notas usa `$wfk-create-note`; PL y PLN seleccionan el mismo tipo de plan.
  Para los demás flujos usa el adaptador `wfk-*` correspondiente.
- Responde en español. Los comandos `/setup` y similares del README original
  pertenecen a Claude Code; no los ejecutes como comandos de shell en Codex.
- No dependas de archivos en el directorio personal de Claude, herramientas
  TeamCreate/AskUserQuestion, cuentas de Luca ni servicios de Holden.
- No copies las restricciones de la bóveda personal de Luca. Esta distribución
  permite las escrituras locales necesarias para las tareas solicitadas y
  conserva los permisos que imponga el entorno de cada persona.
- Consulta `CODEX.md` para instalación, capacidades y comprobación inicial.
<!-- CODEX:END -->
