# Tamarindos — trabajo compartido

Cada persona trabaja en su propia copia con Claude Code o Codex. Notion reúne los proyectos, las tareas y las actualizaciones. El nombre real del responsable se guarda explícitamente, incluso si varias personas usan una cuenta.

## Arquitectura

| Base | Para qué sirve | Campos principales |
| --- | --- | --- |
| Proyectos | Seguir resultados del negocio | Responsable, resultado esperado, estado, indicador, valor actual, meta, fecha objetivo |
| Tareas | Saber qué importa y qué impide avanzar | Proyecto, responsable, prioridad, estado, siguiente paso, bloqueo, quién desbloquea, próximo seguimiento, fecha límite |
| Actualizaciones | Ver qué hizo cada persona | Proyecto, responsable, fecha, hecho, siguiente paso, bloqueo, enlace al entregable |

Los estados y responsables vigentes se mantienen en Notion. El publicador agrega actualizaciones; todavía no cambia tareas ni calcula el avance de proyectos automáticamente. Los indicadores se actualizan con datos reales, sin inventar porcentajes.

## Conectar una vez

Requiere Python 3.10 o posterior y una conexión interna de Notion con acceso de lectura, inserción y actualización. Crea la conexión en el portal de desarrolladores de Notion y agrégala a la página padre mediante el menú Conexiones. No publiques la página para dar acceso.

Ejecuta desde la carpeta del kit, reemplazando ID_DE_PAGINA por el UUID de la página padre:

```text
python scripts/notion_team.py setup --parent ID_DE_PAGINA
```

La terminal pide el token con entrada oculta y lo guarda dentro de .notion/config.json, que está excluido de Git. Así el archivo de configuración lleva todo lo que una persona necesita y no hay que editar el perfil de la terminal en cada computadora. Si prefieres no guardarlo ahí, define NOTION_TOKEN en el entorno local: la variable de entorno siempre tiene prioridad sobre el valor del archivo.

El token queda en texto plano en esa carpeta, igual que si estuviera en ~/.zshrc. Compártelo solo por un canal privado y nunca lo publiques en el repositorio. Si .notion/config.json llegara a quedar bajo control de versiones, el script se niega a usar el token guardado y lo dice.

El comando crea una página Tamarindos — Equipo y tres bases relacionadas. Guarda los identificadores en .notion/config.json, excluido de Git. Una sola persona ejecuta la instalación; después comparte ese archivo de configuración de forma privada con los demás participantes. Cada participante necesita acceso autenticado. No ejecutes instalaciones simultáneas.

Si falla la instalación, vuelve a ejecutar el mismo comando: busca los elementos ya creados y comprueba sus campos antes de continuar. No borra ni reemplaza bases existentes. Un conflicto de nombres o estructura requiere revisión.

## Vistas iniciales en Notion

La instalación crea las bases y sus tablas predeterminadas. Configura estas vistas en la interfaz de Notion; este paso todavía no está automatizado:

- Prioridades de la semana: tareas con prioridad Urgente o Esta semana; excluir Completado.
- Por persona: agrupar tareas por Responsable.
- Bloqueados: Estado = Bloqueado; mostrar Bloqueo, Quién desbloquea y Próximo seguimiento.
- Proyectos activos: excluir Completado; mostrar Resultado esperado, Indicador, Valor actual y Meta.
- Actividad reciente: Actualizaciones ordenadas por Fecha descendente.

Empiecen con los pendientes reales más importantes. Cada tarea debe tener una persona responsable y un siguiente paso concreto. Revisen bloqueos y prioridades al comenzar el día.

## Publicación automática al cerrar la sesión

Después de configurar la conexión, pide «cierra la sesión» o «registra mi avance». El asistente consulta scripts/NOTION-WORKFLOW.md y publica un resumen del trabajo del equipo. Esto ocurre durante el flujo del asistente; no es un servicio de sincronización continua y no funciona con la aplicación cerrada.

Cada resumen se guarda primero en .notion/outbox/ con un UUID estable. Los reintentos buscan ese ID en Notion antes de crear una actualización. Una interrupción conserva el archivo pendiente. No envíes el mismo archivo desde varios equipos simultáneamente: Notion no ofrece unicidad atómica para este campo.

La primera versión publica texto breve y enlaces HTTPS compartidos. No sube archivos adjuntos, documentos completos, datos privados de empleados ni toda la bóveda. Las decisiones, los entregables y el avance deben provenir del trabajo real. Los estados de las tareas se editan en Notion, evitando sobrescribir cambios de otro compañero.

## Portabilidad y comprobación

La configuración y la cola usan JSON, los registros tienen IDs externos, y los documentos siguen en Markdown. Esto facilita una futura migración a software propio.

Previsualizar la estructura sin credenciales:

```text
python scripts/notion_team.py plan
python -B -m unittest discover -s tests -v
```

La comprobación local usa una API simulada. La instalación y publicación reales requieren una prueba con la conexión del equipo; no se consideran verificadas hasta obtener enlaces reales.

Referencias: [conexiones internas](https://developers.notion.com/guides/get-started/internal-connections), [crear bases](https://developers.notion.com/reference/create-a-database).
