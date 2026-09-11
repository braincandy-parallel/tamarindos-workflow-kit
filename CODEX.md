# Usar Tamarindos Workflow Kit con Codex

Esta edición incluye **17 adaptadores de Codex**. Se distribuyen con la plantilla
y reutilizan las habilidades originales en inglés. La conversación y el contenido
de tus notas se redactan en español.

## 1. Crea tu copia

En [la plantilla](https://github.com/braincandy-parallel/tamarindos-workflow-kit),
elige **Use this template → Create a new repository**. Selecciona tu cuenta,
elige un nombre y usa **Private** si guardarás información de trabajo.

Descarga tu repositorio mediante Git o **Code → Download ZIP** y extrae la carpeta.
Una descarga ZIP permite trabajar localmente; el respaldo y la sincronización con
GitHub requieren configurar Git por separado.

## 2. Abre la carpeta en Codex

Instala e inicia sesión siguiendo la [guía oficial de Codex](https://developers.openai.com/codex/quickstart).
Abre la carpeta descargada como proyecto en la aplicación o inicia Codex CLI
desde esa carpeta. Conserva juntas las carpetas ocultas y las carpetas de notas.

Codex lee `AGENTS.md` y descubre las habilidades en `.agents/skills/`.
No copies los adaptadores a tu carpeta personal: necesitan los archivos de esta
misma plantilla. No necesitas instalar Claude Code para usar esta ruta.
Si acabas de añadir el kit a una sesión abierta y no aparecen las habilidades,
vuelve a abrir el proyecto.

## 2.1 Deja de confirmar cada cambio

Codex pregunta antes de escribir archivos o ejecutar comandos según la
configuración de aprobación de **tu propia instalación**, no de este
repositorio. Ninguna instrucción dentro de esta plantilla puede desactivar
esas confirmaciones — es una protección del propio Codex, igual que en
Claude Code. Por eso este archivo no puede resolverlo por ti: cada persona
activa esto en su propia computadora, como parte de la incorporación que
Luca guía en persona.

Configuración estándar del equipo Tamarindos: Codex procede sin pedir
confirmación y puede escribir en cualquier parte de la computadora, no solo
dentro del proyecto. Inicia cada sesión con el siguiente comando desde la
carpeta de tu copia:

```
codex --dangerously-bypass-approvals-and-sandbox
```

Luca guía personalmente la creación de un acceso directo de escritorio que
abre PowerShell en la carpeta correcta y ejecuta ese mismo comando. Así, cada
doble clic inicia una sesión nueva de Codex con esta configuración, sin editar
archivos de configuración globales. No copies el comando dentro de una nota o
archivo del proyecto: se ejecuta en PowerShell.

Con esta configuración, Codex escribe archivos, crea notas en cualquier
carpeta del proyecto y ejecuta comandos sin pedir confirmación. También puede
escribir fuera del proyecto, en cualquier parte de la computadora. Es el mismo
nivel que Luca ya usa en Claude Code (`--dangerously-skip-permissions`),
aplicado aquí para que el equipo no pierda tiempo confirmando cada paso durante
la incorporación guiada.
Los nombres exactos de estas opciones pueden cambiar entre versiones de
Codex. Si no coinciden con lo que ves, revisa `codex --help` o la
documentación oficial de Codex antes de copiar estos valores.

## 3. Configura tu perfil en español

Escribe:

> Configura mi espacio de Tamarindos en español.

O invoca explícitamente:

```text
$wfk-setup
```

Codex preguntará tu nombre, tu función y tu primera prioridad si todavía no los
conoce. Crea tu configuración local, la nota diaria, una carpeta de proyecto,
su registro de trabajo, archivos de contexto y un primer pendiente.

El asistente de configuración incluye un script opcional que usa Python 3.10 o
posterior. Si tu equipo no tiene Python, la habilidad puede crear la misma
estructura con las herramientas de archivos disponibles, sin instalar programas.

Repetir la configuración conserva tus archivos y tu perfil. Puedes pedir cambios
concretos después, por ejemplo: «Actualiza mi función a responsable de servicio».

## 4. Trabaja con las habilidades del kit

| Lo que necesitas | Comando de Codex | Ejemplo en español |
|---|---|---|
| Configuración inicial | `$wfk-setup` | «Configura mi espacio». |
| Ponerte al día | `$wfk-orient` | «Ponme al día». |
| Retomar pendientes | `$wfk-pickup` | «¿Qué pendientes tengo?». |
| Crear documentos | `$wfk-create-note MN` | «Crea una minuta con estos acuerdos». |
| Registrar avance | `$wfk-log-work` | «Anota lo que hicimos hoy». |
| Cerrar la sesión | `$wfk-closeout` | «Guarda el avance para mañana». |
| Entender un documento | `$wfk-explain` | «Explícame este reporte». |
| Guardar una lección | `$wfk-learn` | «Guarda esta lección». |
| Aparcar contexto | `$wfk-park` | «Guarda esta idea para después». |
| Revisar una especificación | `$wfk-review-spec` | «Revisa esta especificación». |
| Ejecutar un plan | `$wfk-implement` | «Ejecuta la primera fase». |
| Operaciones Git solicitadas | `$wfk-git-safe` | «Sube estos cambios a mi repositorio». |
| Consultar habilidades | `$wfk-discover` | «¿Qué habilidades puedo usar?». |

La selección por lenguaje natural depende del contexto. Usa el comando explícito
si el asistente no selecciona la habilidad esperada. Las habilidades se mantienen
en inglés e incluyen ejemplos de solicitudes en español para su descubrimiento.

Documentos disponibles: **MN, RE, EB, SPC, PL/PLN, PIC, PD, SD, DD y SO**.
La revisión de especificaciones usa tres perspectivas secuenciales; no presupone
que haya tres agentes independientes. La ejecución de planes puede preparar y
documentar tareas físicas, pero no realiza el trabajo del personal.

## 5. Abre tus notas en Obsidian

Elige **Abrir carpeta como bóveda** y selecciona la misma carpeta. Las notas de
Codex y Claude Code comparten rutas, prefijos y metadatos. Algunos encabezados
técnicos permanecen en inglés para conservar compatibilidad.

Puedes cambiar de asistente y pedirle que consulte el contexto guardado.
El historial de conversación no se transfiere automáticamente. Evita que dos
sesiones editen el mismo archivo al mismo tiempo.

## Alcance de esta edición

Los 49 flujos originales siguen disponibles para Claude Code. Esta edición
incluye los 17 adaptadores indicados, no una conversión automática de todo el
catálogo. Los flujos restantes, incluidos `end-day`, `roadmap`, `update-wfk`
y las integraciones externas, aún no tienen adaptador de Codex.

No se incluye la configuración personal de Luca, sus datos ni sus reglas de
permisos. Cada entorno conserva sus controles de acceso; una instrucción dentro
del repositorio no los desactiva. Guardar notas no crea automáticamente commits,
publicaciones, correos ni tickets externos.

## Comprobación de una copia nueva

1. Configura un perfil y comprueba que aparezca un primer pendiente.
2. Crea una minuta con hechos de ejemplo y revisa nombres, acuerdos y responsables.
3. Registra un avance y verifica que figure en el registro del proyecto y la nota diaria.
4. Cierra la sesión dejando una tarea concreta pendiente.
5. Abre una nueva sesión, pide retomar y comprueba que recupere ese pendiente.
6. Repite la configuración y comprueba que tus notas y perfil se conserven.

Consulta [el estado de validación](05_System/Workflows/REF%20-%20Codex%20Validation.md)
para distinguir las comprobaciones automatizadas de las pruebas en asistentes reales.

## Ciclo completo de proyectos

Consulta [PIPELINE.md](PIPELINE.md). Los cuatro nuevos adaptadores son
`$wfk-project`, `$wfk-create-spec`, `$wfk-plan-spec` y `$wfk-rollup`.
El asistente entrevista antes de construir cuando falta alcance, revisa la
especificación y guarda el plan. No necesitas invocar cada etapa manualmente.
Los resúmenes semanal/mensual tienen adaptador propio; esto no equivale a portar
todo end-day, roadmap ni los hooks de Claude.

Las habilidades nuevas se descubren al abrir una sesión nueva. La disponibilidad
depende del host: si el catálogo no se actualiza, vuelve a abrir la carpeta/sesión.
