# Notas internas de trabajo (fuera del PDF)

Este archivo reúne las notas de borrador que antes vivían dentro del PDF
(`secciones/10_bibliografia.tex`), retiradas de ahí porque la instrucción de
formato prohíbe explícitamente dejar notas internas en el documento final
(defecto #9). Su contenido no cambió, solo su ubicación.

## Nota sobre la bibliografía

Las 14 referencias de `secciones/10_bibliografia.tex` (ahora `referencias.bib`)
fueron verificadas por título, autoría y año antes de incorporarse al
documento. Las referencias específicas al contexto boliviano (movilidad
urbana en Cochabamba, transporte informal en ciudades bolivianas) no pudieron
verificarse en las bases consultadas y se retiraron en lugar de mantenerse sin
confirmar; se recomienda buscar fuentes reales para ese punto en el
repositorio institucional de la UMSS, SciELO Bolivia o Redalyc antes de la
entrega final, dado que el argumento sobre transporte informal en Cochabamba
(sección "El contexto: una ciudad que se mueve sin mapa oficial",
`secciones/08_02_comprension_datos.tex`... según corresponda tras el split de
Fase 3) se sostiene actualmente sin cita académica de respaldo.

## Apéndice C. Control de coherencia (checklist de cierre)

Verificaciones pendientes antes de considerar cerrado cada capítulo, a
completar conforme avance el proyecto:

1. Confirmar con Trufi App la hipótesis planteada en las secciones de
   auditoría de esquema y cobertura temporal sobre el cambio de proceso de
   exportación en abril de 2024; actualizar la redacción si se obtiene
   confirmación o desmentido.
2. Sustituir las referencias bibliográficas señaladas como pendientes de
   verificación en la nota anterior antes de la entrega definitiva.
3. Una vez definida la resolución H3 final (capítulo Marco Teórico y sección
   de agregación H3), actualizar de forma consistente todas las menciones a
   "resolución 8" y a los conteos de celdas en los capítulos Alcance y
   Desarrollo.
4. Verificar que cada cifra cuantitativa de los capítulos Introducción a
   Marco Teórico tenga respaldo directo en una tabla, figura o script del
   capítulo Desarrollo y sus anexos.
5. Actualizar el índice general, el índice de tablas y el índice de figuras
   conforme se incorporen secciones nuevas.
6. Eliminar esta nota de control (de este archivo) una vez cerrada la
   versión final de entrega.

## Capítulo 6 (Marco teórico): referencias por verificar

Transcritas de `Marco_teorico.md` (sección "Referencias [por verificar]").
Las tres últimas se citan en el texto y tienen entrada provisional en
`referencias.bib` (claves `trufi-100000`, `trufiapp-25rutas`,
`trufi-appstore`), sin URL ni fecha hasta comprobarlas.

- Angulo Andrade (2024): el título exacto y el tipo de documento se tomaron del nombre del archivo en el repositorio de la UMSS, que no admitió acceso automatizado; conviene cotejarlos con la portada. (En `referencias.bib` se conserva el título largo que ya usaban los capítulos anteriores.)
- Anselin, L., Lozano, N., y Koschinsky, J. (2006). *Rate transformations and smoothing* [Informe técnico]. Spatial Analysis Laboratory, University of Illinois. No se localizó en esta revisión; si se desea citar una fuente específica sobre el suavizado de tasas en GeoDa, se recomienda comprobarla antes de incorporarla (en el texto se cita en su lugar Anselin et al., 2006, sobre GeoDa).
- Kittelson & Associates et al. (2013), TCRP Report 165: se verificó la existencia, la edición y el DOI del manual, pero no la página exacta en la que figuran los umbrales de caminata de 400 m y 800 m; el TCRP Report 100 (2.ª ed., 2003) no se verificó y no se incluye en la lista principal.
- MobilityData (s.f.), GTFS Schedule reference: se describió la estructura del estándar sin consultar directamente la página en esta revisión; conviene confirmar la URL vigente y la condición de obligatorio u opcional de cada archivo.
- Chapman et al. (2000): la guía CRISP-DM 1.0 carece de DOI; debe añadirse la URL del ejemplar consultado, y verificarse en ella la afirmación sobre la proporción del esfuerzo dedicada a la preparación de datos.
- SAS Institute (s.f.), metodología SEMMA: se menciona sin referencia formal; si se exige, debe citarse la documentación de SAS Enterprise Miner que se consulte.
- Romano et al. (2006): ponencia sin DOI, verificada solo a través de fuentes secundarias (documentación del paquete effsize de R y artículos que la citan).
- Trufi Association. (s.f.-d). *100,000+ installs for the Trufi App in Cochabamba*. Sitio web de la Trufi Association. Se cita en 6.1.2 a partir de un cotejo secundario; la URL y la fecha no se han comprobado directamente.
- Trufi App. (s.f.). *25 new routes* [Publicación en el sitio trufi.app]. Se cita en 6.1.2 a partir de un cotejo secundario; la URL y la fecha no se han comprobado directamente.
- Trufi Association e.V. (s.f.). *Trufi* [Ficha de la aplicación en App Store]. Apple. La cifra de 626 rutas se obtuvo de un cotejo secundario de la nota de versión; debe comprobarse la ficha vigente y registrar la fecha de consulta.

Nota: las letras s.f.-a, s.f.-b… las asigna biblatex-apa al compilar
(orden alfabético del título), así que en el PDF pueden no coincidir con
las del .md.

## Capítulo 6 (Marco teórico): notas para el autor

- Cifras del contexto: los porcentajes de reparto modal y el inventario de 132 líneas con 648 rutas provienen de Cabrera y De Marchi Moyano (2022), que a su vez citan fuentes previas (un plan metropolitano de movilidad y un inventario estudiantil); deben presentarse como datos citados y no como mediciones propias. Las cifras de instalaciones y de rutas de Trufi proceden de la propia Trufi Association y tienen carácter institucional o promocional.
- Población de Cochabamba: el INE comunicó 2 005 373 habitantes para el departamento en la socialización del conteo de 2024; para el municipio de Cochabamba circulan cifras distintas (661 484 en el conteo preliminar, cuestionado por la alcaldía, y cifras posteriores en agregadores no oficiales), por lo que se optó por no citar cifras municipales.
- Los DOI de los manuales clásicos (Cameron y Trivedi, Hilbe, McCullagh y Nelder, Hastie et al., Little y Rubin) y de algunos artículos (Rubin, Friedman, Donoho, Goodchild) se tomaron de fuentes bibliográficas estándar sin consultar Crossref en esta revisión; conviene una comprobación final en crossref.org antes del depósito.
- Si la monografía debe reportar la versión exacta de scikit-learn, conviene sustituir "stable" en las URL de la documentación por la versión efectivamente empleada.
