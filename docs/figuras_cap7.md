# Figuras del capítulo 7: origen y ubicación

Este archivo **no forma parte del PDF**. Relaciona cada figura del capítulo 7 (Desarrollo) con su sección, su archivo en `imagenes/` y el notebook de `trufi-data-science` que la genera.

Todas las figuras de datos provienen de `trufi-data-science/resultados/<fase>/figuras/` (rama `refactor/documentation`). El diagrama del flujo CRISP-DM del proyecto (figura del 7.1) se dibuja con TikZ dentro de `secciones/08_01_comprension_negocio.tex`, así que no hay ningún PNG manual.

## Cómo volver a traerlas

Cuando se vuelvan a ejecutar los notebooks:

```sh
make figuras                       # = scripts/sincronizar_figuras
TRUFI_REPO=/otra/ruta make figuras # si el repositorio está en otro lugar
```

El script copia las 21 figuras del manifiesto, no borra nada y termina con error si falta alguna.

## Correspondencia

| Sección | Etiqueta LaTeX | Archivo en `imagenes/07_desarrollo/` | Origen (`resultados/…/figuras/`) |
|---|---|---|---|
| 7.1 Comprensión del negocio | `fig:flujo-crisp-proyecto` | — (TikZ) | — |
| 7.2.4 Valores atípicos | `fig:distancia` | `7_2_comprension_datos/distancia.png` | `01_eda` |
| 7.2.5 Cobertura temporal | `fig:cobertura-semanal` | `7_2_comprension_datos/cobertura_semanal.png` | `01_eda` |
| 7.2.5 Cobertura temporal | `fig:perfil-temporal` | `7_2_comprension_datos/perfil_temporal.png` | `01_eda` |
| 7.2.5 Área de estudio | `fig:area-estudio` | `7_2_comprension_datos/area_estudio.png` | `01_eda` |
| 7.2.5 Área de estudio | `fig:gtfs-red` | `7_2_comprension_datos/gtfs_red_y_demanda.png` | `01_eda` |
| 7.2.5 Variable objetivo | `fig:objetivo-distribucion` | `7_2_comprension_datos/objetivo_distribucion.png` | `01_eda` |
| 7.2.6 Relaciones | `fig:objetivo-poblacion` | `7_2_comprension_datos/objetivo_vs_poblacion.png` | `01_eda` |
| 7.2.6 Dependencia espacial | `fig:lisa` | `7_2_comprension_datos/lisa.png` | `01_eda` |
| 7.3.1 Selección de datos | `fig:consultas-por-zona` | `7_3_preparacion/consultas_por_zona.png` | `02_preprocesamiento` |
| 7.3.2 Limpieza | `fig:flujo-limpieza` | `7_3_preparacion/flujo_limpieza.png` | `02_preprocesamiento` |
| 7.3.4 Características | `fig:correlacion-predictores` | `7_3_preparacion/correlacion_predictores.png` | `03_feature_engineering` |
| 7.3.5 Entrenamiento y prueba | `fig:anillos-prueba` | `7_3_preparacion/anillos_y_prueba.png` | `03_feature_engineering` |
| 7.4.6 Comparación | `fig:comparacion-tecnicas` | `7_4_modelado/comparacion_tecnicas.png` | `04_modelado` |
| 7.4.7 Regla de selección | `fig:calibracion-oof` | `7_4_modelado/calibracion_oof.png` | `04_modelado` |
| 7.5.3 Análisis de errores | `fig:calibracion-deciles` | `7_5_evaluacion/calibracion_deciles.png` | `05_evaluacion` |
| 7.5.3 Análisis de errores | `fig:observado-esperado` | `7_5_evaluacion/observado_vs_esperado.png` | `05_evaluacion` |
| 7.5.5 Interpretación | `fig:mapa-brecha` | `7_5_evaluacion/mapa_brecha.png` | `05_evaluacion` |
| 7.5.5 Interpretación | `fig:brecha-cobertura` | `7_5_evaluacion/brecha_por_cobertura.png` | `05_evaluacion` |
| 7.5.5 Sensibilidad | `fig:sensibilidad` | `7_5_evaluacion/sensibilidad.png` | `05_evaluacion` |
| 7.6.1 Priorización | `fig:mapa-acciones` | `7_6_despliegue/mapa_acciones.png` | `06_propuesta` |
| 7.6.1 Priorización | `fig:zonas-prioritarias` | `7_6_despliegue/zonas_prioritarias.png` | `06_propuesta` |

## Mejoras sugeridas para la iteración 2 (se hacen en los notebooks, no aquí)

- **Separador decimal.** Los títulos y ejes de matplotlib usan punto decimal y coma de miles ("1505.7 km²", "0.948", "1,924,578"). La monografía usa coma decimal y punto de miles. Conviene fijar `locale` o formatear los textos en `src/entorno.py`.
- **Tildes en `sensibilidad.png`.** Las etiquetas del eje salen de los identificadores ("mejor tecnica media", "poblacion minima mayor"). Hay que usar etiquetas legibles con tildes.
- **`mapa_brecha.png`.** El título invade la etiqueta de la barra de color. Se puede acortar el título o usar `constrained_layout`.
- **`correlacion_predictores.png`.** Los valores −0,58 se imprimen en gris oscuro sobre azul medio, con poco contraste.
- **Mapas en general** (`area_estudio`, `gtfs_red_y_demanda`, `lisa`, `mapa_acciones`). Las etiquetas de ejes y leyendas quedan pequeñas al ancho de página (unos 7 pt). Conviene subir `font.size` a 11–12 o exportar con `figsize` menor.
- **Imágenes sin uso previo.** Ninguna; las 21 figuras de `resultados/` están citadas.

## Colocación de tablas y figuras en el capítulo 7

Cada tabla o figura se declara con `[H]` (paquete `float`, cargado en `preambulo.tex`): queda exactamente donde se escribe, entre dos párrafos, y nunca parte un párrafo ni una lista. El costo es que, si el flotante no cabe en lo que queda de página, esta termina antes y el flotante empieza la siguiente. Si el hueco molesta, se reduce el ancho de la figura (`width=…\textwidth`) o se mueve el flotante después del párrafo siguiente. `make flotantes` (scripts/verificar_flotantes) comprueba que ningún flotante parta un párrafo y lista las páginas con más del 40 % en blanco.
