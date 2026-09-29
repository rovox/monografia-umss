# Figuras de la monografía: origen y ubicación

Este archivo **no forma parte del PDF**. Relaciona cada figura del .md (`Monografia_Prediccion_Espacial_TrufiApp(2).md`) con su sección, su archivo en `imagenes/` y el notebook de `trufi-data-science` que la genera.

Resultado de la corroboración (.md ↔ notebooks ↔ `reports/`): **23 de 23 figuras tienen imagen.** 20 vienen del pipeline y 3 son diagramas hechos a mano.

## Cómo volver a traerlas

Cuando se vuelvan a ejecutar los notebooks (rama `refactor/crisp-dm-restart`):

```sh
make figuras                       # = scripts/sincronizar_figuras
TRUFI_REPO=/otra/ruta make figuras # si el repositorio está en otro lugar
```

El script copia solo las 20 figuras de la tabla y comprueba que estén los 3 diagramas manuales, sin sobrescribirlos. No borra nada. Termina con error y lista las que falten si alguna no está en `reports/`.

## Correspondencia

| Fig. | Sección | Archivo en `imagenes/` | Origen |
|---|---|---|---|
| 6-1 | 6.5 Metodología CRISP-DM | `06_marco_teorico/crisp_dm.png` | manual |
| 7-1 | Introducción del cap. 7 | `07_desarrollo/7_1_comprension_negocio/flujo_crisp_dm_proyecto.png` | manual |
| 7-2 | 7.2.2 Estructura y auditoría de esquema | `07_desarrollo/7_2_comprension_datos/esquema_grupos.png` | `01_comprension_datos.ipynb`, celda 10 |
| 7-3 | 7.2.5 Validación de la variable distancia | `…/7_2_comprension_datos/distancia_distribucion.png` | nb 01, celda 37 |
| 7-4 | 7.2.6 Identificador de usuario | `…/7_2_comprension_datos/usuario_distribuciones.png` | nb 01, celda 47 |
| 7-5 | 7.2.7 Cobertura temporal | `…/7_2_comprension_datos/cobertura_mensual.png` | nb 01, celda 40 |
| 7-6 | 7.2.8 Distribución espacial de la demanda | `…/7_2_comprension_datos/lorenz_demanda_celdas.png` | nb 01, celda 54 |
| 7-7 | 7.2.9 Estructura espacial de la demanda | `…/7_2_comprension_datos/lisa_clusters_demanda.png` | nb 01, celda 55 |
| 7-8 | 7.3.3 Delimitación del área de estudio | `07_desarrollo/7_3_preparacion/area_estudio_y_consultas.png` | `02_preparacion_datos.ipynb`, celda 41 |
| 7-9 | 7.3.4 Construcción de la tabla minable | `…/7_3_preparacion/query_count_mapa.png` | nb 02, celda 41 |
| 7-10 | 7.3.4 Construcción de la tabla minable | `…/7_3_preparacion/moran_correlograma.png` | nb 02, celda 31 |
| 7-11 | 7.3.5 Construcción de variables | `…/7_3_preparacion/gtfs_cobertura_mapa.png` | nb 02, celda 41 |
| 7-12 | 7.3.6 Reserva del conjunto de prueba | `…/7_3_preparacion/particion_bloques.png` | nb 02, celda 41 |
| 7-13 | 7.4.4 Diseño experimental | `07_desarrollo/7_4_modelado/pliegues.png` | `03_modelado.ipynb`, celda 6 |
| 7-14 | 7.5.2 Resultados de la validación cruzada | `07_desarrollo/7_5_evaluacion/devianza_por_pliegue.png` | nb 03, celda 14 |
| 7-15 | 7.5.4 Validación aleatoria frente a espacial | `…/7_5_evaluacion/optimismo_aleatorio.png` | nb 03, celda 16 |
| 7-16 | 7.5.7 Análisis de errores | `…/7_5_evaluacion/calibracion.png` | `04_evaluacion.ipynb`, celda 21 |
| 7-17 | 7.5.7 Análisis de errores | `…/7_5_evaluacion/residuos_vs_variables.png` | nb 04, celda 19 |
| 7-18 | 7.5.8 Diagnóstico espacial de los residuos | `…/7_5_evaluacion/lisa_residuos.png` | nb 04, celda 17 |
| 7-19 | 7.5.9 Brecha observadas vs. esperadas | `…/7_5_evaluacion/mapa_residuos.png` | nb 04, celda 13 |
| 7-20 | 7.5.10 Brecha y cobertura de la red | `…/7_5_evaluacion/residuos_por_cobertura.png` | nb 04, celda 15 |
| 7-21 | 7.5.11 Modelo de referencia interpretable | `…/7_5_evaluacion/descripcion_modelo_irr.png` | nb 04, celda 23 |
| 7-22 | 7.6.2 Arquitectura de la solución | `07_desarrollo/7_6_despliegue/arquitectura_despliegue.png` | manual |

Las carpetas siguen la **sección del texto**, no el notebook. Por eso 7-14 y 7-15 (generadas en `03_modelado`) están en `7_5_evaluacion`. `05_despliegue.ipynb` no genera figuras.

## Figuras generadas que el .md no cita (no se copian)

| Archivo (`reports/…/figuras/`) | Notebook | Posible uso |
|---|---|---|
| `kontur_poblacion_metro.png` | 01, celda 67 | 7.2.10 Fuente de población: Kontur Population |
| `distancia_histograma.png` | 02, celda 41 | 7.3.2 Umbral de distancia |
| `cobertura_gtfs_vs_consultas.png` | 01, celda 63 | 7.2.11 Red de transporte mapeada (GTFS) |
| `clasificacion_espacial.png` | 01, celda 33 | 7.2.4 Calidad de los datos, o anexo |
| `hallazgos_calidad_resumen.png` | 01, celda 70 | 7.2.4 / 7.2.12, o anexo |
| `proporciones_hora.png` | 01, celda 50 | anexo |
| `lorenz_query_count.png` | 02, celda 41 | repite la idea de la Figura 7-6; descartar |

Para usar alguna, hay que añadir su fila al `MANIFIESTO` de `scripts/sincronizar_figuras` y citarla en el texto.

`gtfs_paradas_sobre_consultas.png` (26-09-2026) está **huérfana**: ningún notebook actual la genera. Es un resto de una ejecución anterior y conviene borrarla de `reports/`.

## Pendiente temporal
Los `secciones/08_0N_*.tex` todavía son la versión antigua y piden 12 `imagenes/fig_*.png` que ya no existen. Mientras tanto, un envoltorio de `\includegraphics` en `preambulo.tex` (marcado como TEMPORAL) omite la imagen ausente y deja el aviso "Imagen ausente" en `build/main.log`. Hay que retirarlo cuando el capítulo 7 esté transcrito y cite las figuras de esta tabla.
