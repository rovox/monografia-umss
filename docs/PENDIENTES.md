# Informe de Pendientes y Advertencias

**Generado:** 2026-10-01 00:16:17

## Resumen
- **Imágenes ausentes:** 0
- **Figuras sin citar:** 0
- **Marcadores de contenido:** 0
- **Placeholders:** 0
- **Datos faltantes:** 0
- **Underfull \\hbox:** 2
- **Overfull \\hbox:** 1

---

## 1. Imágenes Ausentes

Las siguientes imágenes se referencian pero no existen en el filesystem:

*Ninguna.*


---

## 2. Figuras sin Citar

Estas figuras existen en `imagenes/07_desarrollo/` pero ningún `.tex` las referencia:

*Ninguna.*


---

## 3. Marcadores de Contenido Pendiente

| Archivo | Línea | Tipo | Texto |
|---|---|---|---|
| --- | --- | --- | *Ninguno* |


---

## 4. Observaciones de Fondo


De **notas_internas.md**:
# Notas internas de trabajo (fuera del PDF)

Este archivo reúne las notas de borrador que antes vivían dentro del PDF
(`secciones/10_bibliografia.tex`), retiradas de ahí porque la instrucción de
formato prohíbe explícitamente dejar notas internas en el documento final
(defecto #9). Su contenido no cambió, solo su ubicación.

## Nota sobre la bibliografía

Las 14 referencias de `secciones/10_bibliografia.tex` (ahora `referencias.bib`)
fueron verificadas por título, autoría y año antes de incorpor


De **observaciones_fase1.md**:
# Observaciones de la transcripción: Fase 1 (del título a Objetivos)

Fuente: `Monografia_Prediccion_Espacial_TrufiApp(2).md`, líneas 1–381.
Este archivo **no forma parte del PDF**. Solo reúne lo que queda pendiente, lo que conviene mejorar y las observaciones de esta fase.

Leyenda: **[AÑADIR]** falta contenido que solo el autor puede aportar · **[MEJORAR]** el contenido existe, pero conviene revisarlo · **[OBS]** para tener en cuenta, sin acción obligatoria.

Estado de compilación: `make` sin 



---

## 5. Advertencias de LaTeX

### Imágenes ausentes
- **Conteo:** 0
- **Acción:** Ejecutar `make figuras` para sincronizar desde `trufi-data-science`, o reemplazar con archivos locales.

### Underfull / Overfull \\hbox
- **Underfull \\hbox:** 2 (espaciado flojo, menor prioridad)
- **Overfull \\hbox:** 1 (texto desbordado, revisar tablas largas)
- **Acción:** Revisar `build/main.log` con `grep Underfull` / `grep Overfull`.

### microtype
- **Conteo:** 304 (caracteres sin protrusión en EB Garamond)
- **Severidad:** Inocua, solo aviso tipográfico.

### Fuentes no encontradas
- **Garamond:** 0 fallback a EB Garamond (Linux: instalar `fonts-ebgaramond-pro`)
- **fancyhdr + memoir:** aviso de incompatibilidad menor (sin efecto en compilación)

### Referencias/citas indefinidas
- **Referencias indefinidas:** 0 (buscar `??` en PDF)
- **Citas indefinidas:** 0 (clave no en `referencias.bib`)
- **Acción:** Ejecutar `scripts/verificar` para lista completa.

---

## Siguiente Paso

1. Copiar imágenes a `imagenes/07_desarrollo/7_N_*` desde `trufi-data-science/reports/`
2. Reemplazar placeholders de contenido en secciones
3. Ejecutar `./compilar.sh` y `scripts/pendientes` nuevamente
4. Cuando todo esté completo, cambiar `\borradorfalse` en `configuracion.tex`

