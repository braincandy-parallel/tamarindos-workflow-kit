# Cómo trabajar con Tamarindos Workflow Kit

Tu espacio conserva contexto en archivos. Claude Code ayuda a consultarlos y actualizarlos; Obsidian permite leerlos y organizarlos.

## Al comenzar

La primera vez, sigue [SETUP.md](SETUP.md). Después, abre Claude Code desde tu carpeta de trabajo. `/orient` consulta el contexto y `/pickup` muestra trabajo que puedes retomar. También puedes decir: «Ponme al día y ayúdame a elegir qué pendiente atender».

## Durante el día

Comparte hechos con tus propias palabras. Por ejemplo: «En la reunión acordamos revisar el inventario el jueves; Ana confirmó que hará la revisión». Claude puede preparar una minuta mediante `/create-note MN`. Si falta una fecha o responsable, debe preguntarlo o dejarlo pendiente.

Para registrar trabajo terminado usa `/log-work`. Para entender un documento, `/explain`. Para guardar contexto, `/park`.

## Cuando necesitas una mejora organizada

1. **Definir:** `/create-note SPC` aclara el problema, el resultado esperado y los límites.
2. **Revisar:** `/review-spec` busca preguntas abiertas y riesgos.
3. **Planificar:** `/create-note PLN` organiza los pasos y cómo comprobar el resultado.
4. **Ejecutar:** `/implement` guía el trabajo según el plan.

Por ejemplo, una mejora de reservaciones puede comenzar describiendo qué se pierde hoy y cómo sabremos que el seguimiento funciona. No necesitas una especificación para cada anotación breve; ajusta el proceso al tamaño de la tarea.

## Al terminar

Usa `/closeout` para guardar avances y contexto pendiente. `/end-day` genera el cierre diario y la orientación del siguiente día cuando necesites ese reporte adicional.

## Idioma y archivos

Habla con Claude en español. Los comandos permanecen en inglés. Los documentos usan prefijos técnicos como `MN` (minuta), `RE` (reporte), `SPC` (especificación), `PL` (plan) y `PIC` (pendiente con contexto).

Claude redacta contenido y títulos en español. Conserva claves, valores y encabezados que utilicen las automatizaciones originales; puede explicar su significado en español sin cambiar el identificador.

## Tu copia y la plantilla

Cada persona crea su repositorio desde la plantilla. Los documentos de una copia no aparecen automáticamente en las demás. Un espacio compartido requiere acordar aparte los accesos y la sincronización.

Consulta [la guía de actualizaciones](04_Reference/REF%20-%20Updating%20the%20Workflow%20Kit.md) antes de actualizar. Las habilidades originales pueden mencionar herramientas opcionales o ejemplos de otras organizaciones; esos ejemplos no describen a Tamarindos.
