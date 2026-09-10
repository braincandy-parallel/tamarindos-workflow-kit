# Ciclo de proyectos: de la idea al trabajo terminado

Este flujo se aplica a Claude Code y Codex. No necesitas recordar comandos: describe lo que quieres conseguir. El asistente empieza por el proyecto y su contexto, pregunta lo que falta y guarda los documentos antes de construir.

## Ejemplo de primera conversación

**Tú:** «Quiero organizar el mantenimiento del restaurante».

**Asistente:** «Lo ubicaré dentro de Tamarindos. ¿Qué problema necesitas resolver primero: que se olviden las tareas, que no haya responsables o que no se atiendan las fallas?»

Después pregunta por alcance, restricciones y cómo comprobar el resultado, usando las respuestas que ya diste. No inventa empleados, sistemas ni reglas del restaurante. Cuando el alcance está claro, guarda la especificación, revisa sus riesgos y prepara el plan. Si pediste realizar el proyecto, continúa con lo autorizado. Si pediste solamente explorar o escribir una especificación, se detiene en ese alcance.

## Los documentos que conservan el trabajo

1. **SPC:** propósito, resultado esperado, alcance/exclusiones, requisitos, restricciones y aceptación.
2. **RE/ARE de revisión:** problemas detectados, evidencia y decisiones pendientes.
3. **PL:** tareas, dependencias, hitos, estados y comprobación de cada resultado.

La revisión conecta la especificación con el plan; los tres grandes pasos siguen siendo **Spec → Plan → Implement**. La implementación usa el plan guardado y actualiza su estado después de comprobar el trabajo.

## Organización automática

Un proyecto usa 02_Projects/<proyecto>/. Un subproyecto usa 02_Projects/<padre>/<subproyecto>/.

Dentro se guardan specs/, plans/, reports/ y reviews/ con subcarpetas de fecha; agents.md conserva contexto y enlaces activos, lessons.md conserva lecciones y PJL registra trabajo. Los PIC van en pickups/ cuando se necesita contexto de continuación. No se crean versiones FINAL_FINAL ni se mueve información existente sin necesidad.

Prefijos: SPC = especificación; PL = plan; PIC = pendiente retomable; DN = nota diaria; MN = reunión; RE = reporte; PJL = registro de proyecto; WL = registro detallado; REF = referencia.

## Memoria, contexto y registro

CLAUDE.md y AGENTS.md cargan las reglas de entrada. El contexto del proyecto añade inventarios, referencias, decisiones y artefactos reales. Un cambio de chat no sustituye esos archivos ni transfiere automáticamente la conversación.

Las DN ofrecen hasta tres resultados breves por proyecto y enlazan al PJL. El PJL conserva rutas, decisiones, pruebas y lo que necesita otra sesión para continuar. Para sesiones extensas se añade WL: DN → PJL → WL.

«Resumen semanal» reúne los registros de la semana; «cierre mensual» sintetiza los reportes semanales. Se indican fuentes y huecos de información. Estos comandos no instalan una automatización programada.

## Retomar y cerrar

«Retoma este proyecto» carga especificación, revisión, plan y PIC existente y continúa donde quedó el trabajo autorizado.

«Cierra la sesión» actualiza el plan y los registros. Si quedan pendientes, actualiza o crea un PIC cuando el plan no contiene todo el contexto necesario. **Cerrar una sesión no significa terminar el proyecto.** La incorporación de personas y las pruebas de aceptación cuentan como trabajo pendiente.

## Comandos opcionales

| Intención | Codex | Claude Code |
| --- | --- | --- |
| Iniciar/retomar proyecto | $wfk-project | /wfk-project |
| Entrevista y especificación | $wfk-create-spec | /create-spec |
| Revisar especificación | $wfk-review-spec | /review-spec |
| Crear plan | $wfk-plan-spec | /create-plan o /plan-spec |
| Implementar | $wfk-implement | /implement |
| Registrar trabajo | $wfk-log-work | /log-work |
| Cerrar sesión | $wfk-closeout | /closeout |
| Resumen semanal/mensual | $wfk-rollup | /wfk-rollup |

## Preguntas y permisos

Las preguntas para definir el trabajo se conservan. Evitamos pedir repetidamente permiso para continuar una tarea ya autorizada. Una decisión pendiente, un cambio material de alcance o un permiso exigido por la aplicación sí puede requerir intervención.

## Comprobación y límites

El asistente ejecuta scripts/pipeline_gate.py antes de implementar o declarar completo un proyecto. Comprueba documentos vinculados, estado de revisión y contadores; al completar exige evidencia guardada. No evalúa por sí solo si esa evidencia es verdadera: el asistente debe revisarla.

Los hooks de Claude son específicos de ese programa y algunos solo muestran advertencias. No son una garantía universal ni se ejecutan automáticamente en Codex. Estas reglas mejoran la consistencia, pero la prueba en una sesión nueva sigue siendo necesaria.

En una copia nueva, prueba un proyecto incompleto: el asistente debe preguntar antes de construir. Después define su alcance, comprueba SPC/revisión/PL, cierra dejando una tarea pendiente y retoma desde otra sesión. Repite con el asistente que usará cada participante.
