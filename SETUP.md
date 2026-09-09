# Configuración inicial de Tamarindos

Abre Claude Code en esta carpeta y escribe: «Lee SETUP.md y ayúdame a configurar mi espacio de Tamarindos en español».

## Instrucciones para Claude

1. Lee `CLAUDE.md` y `agents.md`. Trabaja en español desde la primera pregunta. Esta preferencia ya está elegida y no depende del idioma del sistema operativo.
2. Verifica Git y Claude Code. Si falta Obsidian, explica cómo instalarlo y permite continuar.
3. Lee `skills/setup/SKILL.md` y sus referencias conforme las necesites. Ejecuta ese procedimiento aplicando las reglas locales de Tamarindos de este documento. No es necesario que `/setup` ya esté instalado para leer y seguir su archivo.
4. Pregunta el nombre, la función en Tamarindos y el pendiente más urgente. No presupongas que todos son gerentes. Confirma el alcance antes de explorar archivos fuera de esta carpeta.
5. Genera el perfil y las carpetas que la persona confirme. Usa ejemplos de reuniones, servicio, cocina o reservaciones cuando correspondan. No inventes procedimientos, responsables ni datos.
6. Conserva las habilidades en inglés. Al instalarlas en `~/.claude/skills/`, compara las que ya existen y consulta antes de reemplazar versiones diferentes. No elimines habilidades ajenas al kit. Usa comandos adecuados para macOS o PowerShell en Windows.
7. En `workflow-kit.config.json`, configura `repo_url` con la URL real de la copia del usuario, consultando su remoto Git. No guardes el marcador `YOUR_USERNAME/workflow-kit` del ejemplo original. Distingue esta copia de la distribución `braincandy-parallel/tamarindos-workflow-kit`.
8. Guarda la preferencia «Español» en el registro de onboarding generado por la habilidad. Conserva las reglas locales de idioma al personalizar `CLAUDE.md` y `agents.md`.
9. Crea los pendientes de bienvenida en español: personalizar el perfil, incorporar documentos elegidos por el usuario y definir una primera mejora. Usa `/create-note SPC`, `/review-spec` y `/create-note PLN` según corresponda. Las referencias heredadas a `/create-spec` y `/create-plan` se resuelven mediante `/create-note`.
10. Resume qué se configuró, cuántas habilidades se instalaron y dónde están las notas. Indica que vuelva a abrir Claude Code en esta carpeta y luego use `/pickup`.

## Comprobación de la primera sesión

- Claude responde en español.
- `/discover` muestra las habilidades después de reiniciar Claude Code.
- «Ayúdame a retomar mis pendientes» utiliza `pickup` cuando corresponde. Si no se activa, prueba `/pickup`.
- Una minuta con `/create-note MN` tiene contenido en español y conserva los campos técnicos requeridos.
- Las carpetas y el perfil corresponden a la persona que configura su copia.

La activación en lenguaje natural debe comprobarse en Claude Code con las habilidades instaladas. Una revisión de archivos por sí sola no garantiza qué habilidad elegirá el modelo.
