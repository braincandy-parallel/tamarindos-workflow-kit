# Tamarindos Workflow Kit

**Tu espacio de trabajo con Claude Code, en español.**

Organiza pendientes, documenta reuniones y retoma tu trabajo sin empezar de cero cada día. Esta plantilla está pensada para el equipo de Tamarindos: administración, cocina, servicio, reservaciones, mantenimiento y marketing.

No necesitas programar. Escribes lo que necesitas en español y Claude te ayuda a convertirlo en trabajo organizado, con contexto que se guarda en archivos.

Basado en [Workflow Kit de Holden Greene](https://github.com/hgreene624/workflow-kit). Las habilidades (*skills*) y los comandos se conservan en inglés; la bienvenida y la conversación son en español.

## ¿Qué puedes hacer?

| Puedes decir | Para qué sirve |
|---|---|
| «¿Qué pendientes tengo para hoy?» | Consultar trabajo guardado y prioridades. |
| «Tuvimos una reunión de cocina. Estos fueron los acuerdos…» | Preparar una minuta con acuerdos y responsables confirmados. |
| «Quiero mejorar el proceso de reservaciones» | Definir el problema y preparar un plan. |
| «Anota que hoy terminamos el inventario» | Registrar el avance que reportaste. |
| «Guarda este pendiente para mañana» | Conservar contexto para retomarlo. |
| «Explícame este reporte» | Entender un documento con lenguaje claro. |

Claude utiliza lo que le compartes y los archivos a los que tiene acceso. Las conexiones con reservaciones, correo, inventarios u otros sistemas se configuran por separado.

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
