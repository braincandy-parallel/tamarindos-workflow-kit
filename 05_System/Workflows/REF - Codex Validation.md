---
date created: 2026-09-09
tags: [reference, codex, validation]
category: Reference
---

# Validación de la edición Codex

## Alcance

Esta edición distribuye 13 adaptadores de Codex sobre las habilidades originales
en inglés. No afirma compatibilidad con las 49 habilidades completas.

## Comprobaciones realizadas

- Los 13 archivos SKILL.md pasan el validador de formato de skill-creator.
- El asistente de configuración pasa pruebas de creación inicial, conservación
  de perfil y notas, reparación de archivos faltantes, cambio de ubicación,
  rechazo de rutas de proyecto inválidas y conflictos de archivos.
- El paquete comprueba las referencias a habilidades y plantillas, el nombre
  AGENTS.md con mayúsculas y los enlaces locales de la documentación.
- El catálogo original de habilidades se conserva sin editar.
- La prueba real de Codex seleccionó wfk-setup, wfk-create-note, wfk-log-work y
  wfk-closeout a partir de una solicitud en español con datos ficticios.

## Pruebas que siguen pendientes

La sesión real de Codex no pudo leer ni escribir los archivos del escenario:
la política del entorno de prueba rechazó sus herramientas de archivos.
Por lo tanto, esa prueba confirma selección de habilidades, pero no ejecución
completa de onboarding, minuta, registro, cierre y recuperación entre sesiones.

Tampoco se ha ejecutado una sesión real de Claude Code para comprobar la
continuación de un documento creado por Codex. Los formatos están diseñados para
compartirse; la interoperabilidad completa requiere esa comprobación.

Las pruebas automatizadas de esta edición están en GitHub Actions:
[Codex compatibility](https://github.com/braincandy-parallel/tamarindos-workflow-kit/actions/workflows/codex-compatibility.yml).
Revisa la ejecución correspondiente al commit que descargues.

## Repetir las pruebas locales

Con Python 3.10 o posterior, desde la raíz de la copia:

```text
python -B -m unittest discover -s tests -v
```

En macOS o Linux utiliza python3 si ese es el nombre del ejecutable.
Las pruebas crean carpetas temporales con datos ficticios y no modifican las
notas de la copia. La secuencia manual para una sesión real aparece en CODEX.md.
