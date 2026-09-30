# Inconsistencias y pendientes tras alinear el capítulo 7 con `trufi-data-science`

Este archivo **no forma parte del PDF**.

- **Fuente de verdad:** `trufi-data-science` (rama `refactor/documentation`, commit `ad72d45`), en concreto `config.py`, `src/`, `notebooks/` y `resultados/<fase>/metricas.json` y los CSV de cada fase.
- **Alcance de esta iteración:** capítulo 7 (Desarrollo), Problema, Alcance y Objetivos.

## 1. Corregido en esta iteración

| Archivo | Inconsistencia | Corrección |
|---|---|---|
| `03_problema.tex` (2.1 y 2.2) | Decía que el esperado se estima a partir de la población, la localización **y la cobertura de la red mapeada**, e incluía el municipio como factor. En el código, `dist_trazado_m` y `gtfs_covered` son solo de contraste (`config.CONTRASTE`) y el municipio solo lo usa la línea base B1. | Lo esperado se estima con la población y la localización. La cobertura se reserva para interpretar la brecha, y se explica por qué. |
| `03_problema.tex` | Alias temporal `sec:friccion-a-brecha`. | Eliminado. |
| `06_objetivos.tex` (OG) | Mismo problema de la cobertura como insumo. | "…a partir de la población residente y la localización…, y contrastar la diferencia … con la cobertura". |
| `05_alcance.tex` | Enumeraba 7 municipios, pero el área real abarca 14. | Se remite a la sección 7.2.5 y se menciona la extensión a municipios vecinos del valle. |
| `08_01` … `08_06` | Todo el capítulo describía el pipeline antiguo: panel celda × semana, rezagos, partición cronológica, Ridge/Lasso/RF/XGBoost, MAE 10,19, H1/H2, API REST, 12 figuras inexistentes. | Reescrito a partir del proyecto real, con la estructura de la guía 2.7.1–2.7.6. |
| `scripts/sincronizar_figuras`, `docs/figuras_cap7.md` | Apuntaban a `reports/` y a notebooks que ya no existen. | Apuntan a `resultados/<fase>/figuras/`. Hay 21 figuras sincronizadas, y se borraron las 22 antiguas. |
| `preambulo.tex` | Envoltorio TEMPORAL de `\includegraphics`; desbordes de 1,4 pt en los folios de tres cifras de los índices. | Envoltorio retirado. Se añadieron TikZ, `\pendiente{}`, `\celda{}` y las columnas `L`/`Y`, y se ajustaron `\setpnumwidth` y `\setrmarg`. El documento queda con 0 desbordes. |
| `scripts/pendientes` | Contaba cada "todo/Todos" del español como `TODO`. | `TODO` y `FIXME` pasan a distinguir mayúsculas; además detecta `\pendiente{`. |

> **Aviso sobre el otro repositorio:** `trufi-data-science/EXPLICATIVO.md` §2 repite la misma imprecisión ("a partir de la población residente, la localización **y la cobertura**…"). No se modificó, pero conviene alinearlo con el código.

## 2. Marcadores `[Revisar]`: resueltos el 30-09-2026 con los resultados nuevos del repositorio

Commits de `trufi-data-science` usados: `68e290b`, `e7116c0`, `3e1e47b`, `0ca65cb` y `34356a8`.

| Sección | Resolución | Fuente |
|---|---|---|
| 7.1.3 | Plantilla de terreno: `field_result` (precargada con `sin_visitar`) y `field_notes`; protocolo en 7.6.3 | `06_propuesta/zonas_prioritarias.csv` |
| 7.2.5 | Registro parcial: exportaciones entregadas en plazo; causa del hueco no confirmada; remite a 8.1.2 y R8 | `EXPLICATIVO.md` §5 |
| 7.2.7 | Tabla 11 sin `dist_trazado_m` y con P25; tablas 11, 16 y 18 trazables | `03_feature_engineering/estadisticas_descriptivas.csv`, `resumen_municipio.csv`, `resumen_anillo.csv` |
| 7.3.3 | Pureza del municipio: 99,38 % de las consultas con etiqueta modal; 5,02 % de zonas mixtas (umbral del 90 %); tabla 16 ampliada | `resumen_municipio.csv`, `metricas.json` |
| 7.4.3 | Sin ZIP/ZINB: 345 ceros observados; Poisson espera 631,5 y NB2 espera 323,8 (tabla nueva) | `04_modelado/ceros_esperados.csv` |
| 7.4.5 | M3 por pliegue (tabla nueva) y ajuste completo; fuga de la parada temprana del 98,6 % | `cv_hiperparametros_m3.csv`, `metricas.json` |
| 7.5.5 | Variantes Kontur 2022 y H3 7/9 no ejecutadas; R10 | — |

Matices incorporados que no venían en el texto propuesto:
- **M3 no es estable.** En los pliegues gana la profundidad 3 con tasa de 0,10 (4 de 5), mientras que el ajuste completo elige profundidad sin límite con tasa de 0,05.
- **`field_result` no está vacía.** Viene precargada con `sin_visitar`.

## 2b. Despliegue (7.6), Resumen, Conclusiones, Glosario y Anexos: cerrados el 30-09-2026

**7.6 Despliegue.** Se sustituyó la sección provisional por el texto del autor (introducción y 7.6.1 a 7.6.4), con `\ref{}` en lugar de números fijos y un diagrama TikZ de arquitectura (`fig:arquitectura`). Se ajustaron cuatro pasajes que venían de la versión antigua del proyecto y no tienen respaldo:

| Pasaje original | Ajuste |
|---|---|
| «Chequeo de completitud (piso de 10.041 consultas semanales)» y «dos semanas de prueba que eran fragmentos de un día (7.5.4)» | Tercera alerta de monitoreo por semanas faltantes o parciales (como propone `EXPLICATIVO.md`), justificada por el hueco de siete semanas de 7.2.5. No se cita la cifra 10.041. |
| Cadencia trimestral «alineada con la ventana de validación» | Cadencia trimestral como recomendación, sin atarla a una ventana de validación que ya no existe. |
| Umbrales «derivados de la distribución real de error» | Umbrales presentados como orientativos, a calibrar con las primeras reejecuciones. La calibración de la prueba (0,597) ya está fuera de [0,9; 1,1]. |
| «Tabla 35», «figuras 22 y 23», «sección 7.5.5/7.1.3» | `\ref{}` |

Se añadió a 7.6.1 una frase que distingue el 79,7 % (top-20 sobre zonas sin cobertura) del 60,2 % de 7.5.5 (top-20 sobre todas las zonas).

**Resumen.** Reescrito en «zona», recortado a una plana (cabe con seis palabras clave). Cifras corregidas:

| Antes | Ahora |
|---|---|
| Devianza 1.807,2 → 981,7; D² 76,5 % | 2.183,8 (tasa única) → 1.086,5; D² de 0,502 frente a la tasa global; Spearman de 0,88 |
| D² de 0,91 frente a 0,64 (validación aleatoria) | Eliminado: ese análisis no existe en el pipeline |
| Spearman ≥ 0,87 | Jaccard de 1,0 ante el hueco temporal |
| «sin una parada a 500 m»; δ de Cliff = +0,37 | «sin trazado cercano»; δ de Cliff = −0,058 (despreciable) |

**Conclusiones (cap. 9).** Reescritas por objetivo (OE1 a OE4) con las cifras del cuerpo. Limitaciones y recomendaciones R1 a R10 alineadas con `EXPLICATIVO.md` §11–§12; R8 y R10 conservan su número porque el cap. 7 las cita. Ya no quedan H1/H2, Random Forest, MAE 10,19, Diebold-Mariano ni OE5 a OE7.

**Glosario y anexos.** `B0, B1, B2, B3` y `M1, M2, M3` (con «línea base = punto de referencia inicial»); entradas nuevas (línea base, índice de Jaccard, regla de un error estándar, Spearman, zona); se retiraron IRR y «tabla minable», que ya no se usan. El anexo B remite a `tab:trazabilidad-oe`, los seis notebooks y `resultados/<fase>/`.

**Marco teórico.** 6.1.6 (edición única 2023-11-01), 6.3.3 (ejemplo con la distancia al centro y no con la cobertura), 6.3.6 (municipio por etiqueta de Trufi; cobertura solo de contraste), 6.4.7 (solo δ de Cliff, sin p-valor).

**Introducción y Alcance.** «celda» pasa a «zona»; el dominio territorial se reformula con los 14 municipios.

### Nota sobre los análisis externos que se pegaron

No aplicaron, tras verificarlo contra el PDF y el repositorio:
- «Sección ??» en 7.1.4 y 7.5.6: no existen en el cap. 7 (los 13 «??» estaban todos en el cap. 9 antiguo).
- «CRISPR-ML(Q)»: no aparece en ningún `.tex`.
- «Fórmulas incompletas en 6.3.3» y «tabla 26 con columnas juntas»: el LaTeX es correcto.
- Fuentes de las 755 zonas sin cobertura (`contraste_gtfs.csv`) y de las 125 zonas de borde (`metricas.json`): correctas.
- «Cochabamba (Cercado)» en la tabla 16: se conserva porque es la etiqueta de los datos y 7.3.3 la explica.

Contenían errores los textos propuestos de resumen y conclusiones:
- «Devianza de 1.807,2 a 1.086,5»: la devianza de la tasa global en la prueba es **2.183,8** (recalculada en el repositorio; con ella el D² de 0,502 cuadra). El 1.807,2 es de la versión antigua.
- «D² 0,91 frente a 0,64», «Spearman ≥ 0,87» y «parada de la red»: son de la versión antigua.
- El resumen propuesto tenía unas 520 palabras, y la guía pide una plana (caben unas 250).
- La devianza de la tasa global (2.183,8) no está en `resultados/`: se deriva de 1.086,5 / (1 − 0,502). Conviene que `05_evaluacion` la guarde en `metricas_prueba.csv`.

## 3. Pendientes que quedan

- **Anexos C a F:** eliminados por decisión del autor (30-09-2026); quedan los Anexos A y B.
- **Devianza de B0 (2.183,8):** no se guarda en `resultados/`. Si el autor añade la fila a `metricas_prueba.csv` en `05_evaluacion`, no hay que actualizar la monografía: el cambio es aditivo y el pipeline es determinista (semilla 42). Solo cambia la nota de la Tabla 30. Comprobación: reejecutar 05 y 06 y `git diff --stat resultados/` (solo deben cambiar `metricas_prueba.csv` y el `metricas.json` de 05). Se actualizaría todo solo si cambian los datos de entrada (R8) o `config.py`.
- **Notebook `05_evaluacion`:** guardar la devianza de la tasa global en la prueba (2.183,8).
- **Figuras del pipeline (iteración 2):** ver `docs/figuras_cap7.md`.
- **Marco teórico, diferencias menores con la implementación:**
  - 6.3.2 describe el primer anillo con regla de respaldo, y la implementación amplía el disco hasta reunir 3 vecinas (máximo 10 anillos) antes de usar la tasa global. Es compatible, pero conviene precisarlo.
  - 6.4.5 menciona Moran y LISA sobre los residuos, que el pipeline no calcula sobre la brecha.
