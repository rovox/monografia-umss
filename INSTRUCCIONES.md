## 0. Modo de trabajo (léelo primero)

- **Trabaja directamente sobre `main`.** Un commit por fase (`faseN: resumen`) y `git push` a `main` al terminar cada fase.
- **Antes de empezar**, crea y sube una etiqueta de respaldo: `git tag pre-refactor && git push origin pre-refactor`.
- **Cada commit debe compilar sin errores.** Si una fase no compila o no pasa su verificación, corrígela antes de hacer commit; nunca subas un `main` roto.
- **No te detengas entre fases** ni pidas confirmación. Solo pregunta si algo bloquea de verdad y no está resuelto en este archivo.
- **Esta instrucción es la especificación completa.** No necesitas leer la guía, el PDF de Century 21 ni el .docx de Fernando: todo lo relevante ya está desglosado en la sección 2. No generes reportes por fase ni capturas de pantalla; solo un informe final corto (sección 8).
- **Prioridad si el tiempo aprieta:** P1 (cumplir la guía) → P2 (estilo) → P3 (opcional). Las fases 1 a 4 son P1; no las dejes a medias por trabajar en P2/P3.
- Nunca uses pdflatex. No versiones `build/` ni `main.pdf`. Equipo de compilación modesto: no agregues paquetes pesados sin necesidad.

## 1. Contexto y regla de oro

Repo `rovox/monografia-umss`: `main.tex` (datos y ensamblado), `preambulo.tex` (formato), `secciones/00..10_*.tex` (contenido), `imagenes/`, `.latexmkrc`, `compilar.sh`, `Makefile`, `.github/workflows/build.yml`, `README.md`. Motor: LuaLaTeX + memoir + latexmk.

**Cambias formato y estructura, NO contenido.** No reescribas texto, no cambies cifras, no inventes datos ni referencias. Excepciones permitidas: (a) retirar las notas internas de borrador (sección 3), (b) convertir citas y bibliografía al sistema nuevo conservando exactamente los mismos datos.

## 2. Requisitos de formato (desglose completo)

Origen: **G** = Guía 2026 (explícita, manda), **M** = modelo final de Century 21 (manda donde la guía calla o se contradice), **D** = decisión de diseño para lo que ninguno fija.

### 2.1 Página, tipografía e interlineado

| Requisito | Valor exacto | Origen |
|---|---|---|
| Papel | Carta | G/M |
| Márgenes del **bloque de texto** | Izq. 3 cm · Der. 2,5 cm · Sup. 2,5 cm · Inf. 2,5 cm | G §2/3 |
| Encabezado y pie | Dentro de los márgenes; **no** descuentan del cuerpo (las notas al pie también respetan márgenes) | G §3.6 |
| Texto general | Arial 12 (respaldo: Liberation Sans) | G |
| Títulos principales | Arial 14 negrita | G |
| Resumen | Garamond 11,5 pt, interlineado 1,2, 6 pt antes y después de cada párrafo (respaldo: EB Garamond); una sola hoja incluyendo palabras clave | G |
| Interlineado de la prosa | **Doble real = 27,6 pt** entre líneas con Arial 12 (el modelo mide 27,6) | G/M |
| Interlineado sencillo en | Tablas, "Nota.", captions, bibliografía (dentro de cada registro), listados de código, líneas 2+ de entradas del índice | G ("salvo elementos que por su naturaleza requieran otro formato") |
| Justificación | Cuerpo justificado | M |
| Fuente de captions, encabezado corrido, folio, "Página" del índice | La misma Arial (hoy salen en Latin Modern por error) | D |
| Monoespaciada (variables, código) | IBM Plex Mono / JetBrains Mono / Source Code Pro, escalada a la altura de x de Arial | D |

### 2.2 Numeración y orden de preliminares

| Requisito | Valor | Origen |
|---|---|---|
| Folio | **Abajo y centrado**, misma posición en todas las páginas | G §3.1 |
| Preliminares | Romanos minúscula (i, ii, iii, iv…) | G §3.1 |
| Cuerpo | Arábigos desde **1** en la primera página del texto (Introducción) | G §3.1 |
| Carátula, dedicatoria, agradecimientos | **Cuentan en el conteo pero no muestran número** | G §3.1 |
| Secciones principales (capítulos, bibliografía, anexos) | Siempre en página nueva | G §3.1 |
| Orden de preliminares | Carátula → Dedicatoria → Agradecimientos → Resumen → Índice general → Índice de tablas → Índice de figuras → Glosario y abreviaturas, cada uno en página nueva | D (G lista el orden de forma ambigua) |
| Opcionales | Dedicatoria, agradecimientos, glosario, índice de tablas e índice de figuras se muestran solo si existen; no dejar hojas en blanco ni entradas vacías | G §2 |
| Modo alterno "continua" (interruptor) | Arábiga continua desde la carátula, como el modelo | M |

### 2.3 Carátula (una sola hoja)

| Elemento | Especificación | Origen |
|---|---|---|
| Línea 1 | UNIVERSIDAD MAYOR DE SAN SIMÓN — Arial 16 negrita | G §3.3 |
| Línea 2 | FACULTAD DE CIENCIAS Y TECNOLOGÍA — Arial 14 negrita | G §3.3 |
| Línea 3 | DIRECCIÓN DE POSGRADO — Arial 12 negrita; las tres líneas a interlineado sencillo | G §3.3 |
| Logos | Posgrado a la **derecha**, alineado con el borde superior de la primera línea; UMSS y Facultad a la **izquierda**, lado a lado | G §3.3 |
| Título | Mayúsculas, Arial 20 negrita, centrado, entre comillas (como el modelo del Anexo), en **pirámide invertida** con saltos de línea explícitos configurables; sin reducir el tamaño | G §3.3 / M |
| Leyenda "MONOGRAFÍA PRESENTADA PARA OBTENER EL CERTIFICADO DE DIPLOMADO EN … VERSIÓN" | Tres líneas bajo el título; **a 2,5 cm del margen izquierdo**, justificación completa; Arial 12 negrita, mayúsculas | G §3.3 |
| POSTULANTE | Cinco líneas bajo la leyenda; "POSTULANTE" Arial 14 negrita y **1 cm a la derecha** ": NOMBRE"; justificación completa | G §3.3 |
| Pie | Centrado: "Cochabamba – Bolivia" y debajo el año; Arial 12 negrita, interlineado sencillo; dos espacios antes del salto de página | G §3.3 |
| Línea "Docente / Módulo" | Oculta por defecto (interruptor). La guía la menciona en §2 pero no en el modelo §3.3 | D |
| Construcción | Espacios verticales **proporcionales** (que se estiren), no medidas fijas, para que nada empuje el pie a una segunda hoja | D |

### 2.4 Títulos e índice

| Requisito | Valor | Origen |
|---|---|---|
| Capítulos | MAYÚSCULAS, Arial 14 negrita, centrados, siempre en página nueva, numerados "1.", "2."… | G/M |
| Secciones | Arial 13 negrita, alineadas a la izquierda, mayúscula solo inicial (tipo oración) | M/D |
| Subsecciones | Arial 12 negrita cursiva | D |
| Profundidad (numeración e índice) | **Tres niveles** (7 · 7.2 · 7.2.1) | M |
| Títulos | Nunca huérfanos al pie de página | D |
| Capítulo 7 | "DESARROLLO (SECCIÓN APLICATIVA: CRISP-DM)" | G Anexo A / M |
| Capítulo 9 | "BIBLIOGRAFÍA Y ANEXOS" con 9.1 Bibliografía y 9.2 Anexos, **cada uno en página nueva** | G §3.1 |
| Índice — formato | **Mismo formato de títulos que el texto** (capítulos en MAYÚSCULAS también en el índice); sin negrillas | G §3.4 |
| Índice — estructura | Capítulos alineados a la izquierda sin sangría; subtítulos sangrados; puntos guía hasta el folio (folios justificados a la derecha); palabra "Página" encima de la columna de folios | G §3.4 |
| Índice — espaciado | Doble espacio **antes** de cada título principal (hoy un capítulo queda pegado a las subsecciones anteriores); si un título ocupa más de una línea, la segunda va sangrada y a espacio sencillo | G §3.4 |
| Índice — contenido | Debe incluir bibliografía y **todos los anexos** (A, B, C…), y los marcadores del PDF también; coincidencia exacta de numeración con el texto | G §3.4 |
| Índices de tablas y figuras | Con prefijo "Tabla N" / "Figura N", cada uno en página nueva | G §2 |
| Marcadores del PDF | Carátula, Índice, Índice de tablas, Índice de figuras, Glosario, Bibliografía, Anexos y capítulos/secciones | D |

### 2.5 Tablas, figuras y notas

| Requisito | Valor | Origen |
|---|---|---|
| Identificación | Toda tabla/figura con título y fuente; figuras legibles y explicadas en el texto | G §2/3.2 |
| Numeración | **Consecutiva** en todo el documento (Tabla 1…, Figura 1…); en anexos con letra: Figura A1, Tabla B1 | G/M |
| Rótulo | Arriba, en una línea, centrado: **rótulo en negrita** + título en cursiva; igual en cuerpo y anexos | D (el modelo mezcla estilos) |
| "Nota." | Bajo cada tabla/figura, una sola línea con "Nota." en cursiva + texto normal, 10 pt, sencillo, al ancho del elemento; reúne fuente, unidades y abreviaturas (cubre las "notas de tabla" de la guía). Sustituye al comando actual de fuente conservando el texto | G §3.6 / M |
| Tablas | Solo líneas horizontales finas, encabezado en negrita, 10–11 pt, más aire entre filas, columnas de texto con reparto flexible, números alineados por coma decimal y miles con "."; unidades en el encabezado | D |
| Si una tabla no cabe | 1.º redistribuir columnas → 2.º `\footnotesize` → 3.º apaisar. **Nunca escalar por debajo de ~85 %** | D |
| Tablas largas | Encabezado repetido en cada página | D |
| Nombres de variables (con `_`) | Deben poder cortarse sin desbordar la columna | D |
| Figuras | Ancho ≤ ancho útil, alto ≤ ~55 % de la altura útil; anchos estandarizados (completo, ¾, ½); figura y rótulo siempre juntos | D |
| Flotantes | Anclados a su sección (barrera de flotantes al inicio de cada sección) | D |
| Referencias cruzadas | Automáticas con prefijo en español ("sección 7.2.5", "tabla 4", "anexo B", "figura A2"); sustituir los `sección~\ref{}` manuales revisando el diff | D |
| Cifras | Un solo formato numérico en todo el documento | D |

### 2.6 Citas y bibliografía

| Requisito | Valor | Origen |
|---|---|---|
| Citas en el texto | Formato norteamericano (autor, año): `(Autor, año)`, `(Autor & Autor, año)`, `(Autor et al., año)`, página como `p. N` | G §3.5 / M |
| Lista | Solo obras realmente citadas y citadas todas; alfabética; **sin numerar**; apellido e iniciales; año entre paréntesis; título de obra/revista en cursiva; "s.f." si no hay fecha; sangría francesa | G §3.6 / M (APA) |
| Espaciado | Sencillo dentro de cada registro y una línea en blanco entre registros | G §3.6 |
| Sistema | biblatex + biber con un único `referencias.bib` (Zotero → Better BibTeX, exportación automática) | D |
| Migración | Pasa las 14 referencias actuales de `secciones/10_bibliografia.tex` al `.bib` **sin agregar datos** (si falta volumen, DOI, etc., déjalo vacío y anótalo en el informe final). Convierte cada `\cita`/`\citap` a su clave; una cita sin entrada es un fallo, no la inventes | D |
| Modo numerado de la guía §3.6 (número y autor en negrilla, apellido en MAYÚSCULAS) | **P3 opcional**, como interruptor | G §3.6 |

### 2.7 Estilo propio donde la guía calla (sobrio, tipo "MIT")

| Elemento | Especificación |
|---|---|
| Color | **Un solo acento**: azul marino institucional muestreado del logo de Posgrado (`imagenes/logo_posgrado.png`); el rojo institucional solo en detalles mínimos. Solo en filetes, líneas de tabla y barras de recuadros. **El texto siempre negro.** Interruptor "impresión" → todo en negro/gris |
| Encabezado corrido | Solo en el cuerpo; no en preliminares ni en la primera página de cada capítulo; Arial 9–10 pt cursiva con filete de 0,4 pt; izquierda: título corto del proyecto; derecha: capítulo actual. El folio sigue abajo y centrado |
| Recuadros | Entorno sobrio "Hallazgo / Decisión / Advertencia" (barra lateral fina, fondo casi blanco). **Créalo y documéntalo, pero no lo insertes en el texto del autor** |
| Tablas | Encabezado con fondo muy tenue permitido; nada de íconos, trofeos ni capturas como tablas |
| Hipervínculos | Azul oscuro en modo digital, negro en impresión; metadatos del PDF con idioma español y título/autor tomados del panel de control |
| Justificación | Sin ajuste global "sloppy"; patrones de silabación en español; sin avisos de silabación |

## 3. Defectos actuales conocidos (corrígelos, no los busques)

1. La carátula ocupa **2 hojas** ("Cochabamba – Bolivia / 2026" cae sola en la 2.ª) y desplaza el conteo: el Resumen sale "iii" en la 5.ª hoja.
2. Márgenes reales de ~3,8 cm arriba y ~3,85 cm abajo por opciones que descuentan encabezado y pie del cuerpo.
3. Interlineado real de 17,3 pt (≈1,25×); no es doble.
4. Latin Modern Sans en captions y en "Página", Latin Modern Mono en `\texttt`.
5. 6 `Overfull \hbox` en la tabla del diccionario de datos (`origin_latitude`, `destination_latitude`… se solapan con la columna "Tipo").
6. "9.2 Anexos" empieza a media hoja; los Anexos A–F no salen en el índice ni en los marcadores.
7. En el índice, un capítulo queda pegado a las subsecciones previas y el índice mezcla minúsculas con el título en mayúsculas.
8. Ajuste global "sloppy".
9. Notas internas dentro del PDF: la "Nota sobre la bibliografía" y el "Apéndice C. Control de coherencia" → muévelas a `docs/notas_internas.md`, fuera del documento.
10. El capítulo 7 se titula "Desarrollo" (debe ser "DESARROLLO (SECCIÓN APLICATIVA: CRISP-DM)").

## 4. Panel de control e interruptores

Concentra en `main.tex` (o un `configuracion.tex` incluido desde él) **todo lo que cambia**: título largo (con los cortes de la pirámide), título corto, nombre, año, versión, diplomado, docente/módulo, y estos interruptores (valor por defecto primero):

| Interruptor | Por defecto | Alternativa |
|---|---|---|
| Numeración | Guía (romanos + arábigos) | Continua desde la carátula |
| Folio | Abajo centrado | Abajo a la derecha |
| Docente/Módulo en carátula | Oculto | Visible |
| Modo | Final | Borrador (resalta `[…]`/TODO); en **final**, falla la compilación si quedan marcadores o notas internas |
| Color | Digital con acento | Impresión (negro/gris) |
| Preliminares opcionales | Mostrar los que existen | Ocultar |
| Compilar solo un capítulo | Apagado | Encendido |
| Bibliografía | APA | Numerada de la guía (P3) |

Los archivos de `secciones/` **no llevan formato**: solo contenido y comandos semánticos del preámbulo. Entornos definidos una sola vez: tabla estándar, tabla ancha, tabla larga, figura, nota, recuadro, bloque de código, identificador de variable.

## 5. Fases (ejecútalas todas seguidas)

### Fase 1 — Página, tipografía, interlineado y verificación (P1)
- Márgenes reales, interlineado doble real, tipografía unificada en Arial/Garamond/monoespaciada, silabación española, fin del "sloppy".
- Crea `scripts/verificar` (Python o shell, sin dependencias exóticas) que sobre `main.pdf` mida con `pdftotext -bbox-layout` los márgenes del texto y el interlineado de la prosa, liste fuentes con `pdffonts`, cuente páginas y desbordes del log, y detecte referencias/citas indefinidas y marcadores `[…]`.
- **Aceptación:** márgenes 3 / 2,5 / 2,5 / 2,5 cm ±0,15; prosa a 27,6 ± 0,5 pt; `pdffonts` solo con Arial/Liberation Sans, Garamond/EB Garamond y la monoespaciada elegida, **ninguna "LM"**.

### Fase 2 — Carátula, preliminares y numeración (P1)
- Secciones 2.2 y 2.3, más el panel de control y sus interruptores de esta parte.
- **Aceptación:** carátula en **1 hoja**; el Resumen sale con el romano correcto según el orden y modo; carátula/dedicatoria/agradecimientos sin folio; el folio de todas las demás páginas abajo y centrado; conmutar numeración y folio funciona sin tocar `secciones/`.

### Fase 3 — Títulos, índices, anexos y reorganización (P1)
- Sección 2.4. Parte el capítulo 7 en un archivo por fase CRISP-DM (7.1 … 7.6) y crea un archivo por anexo; **mantén estables todos los `\label`**. Modo borrador/final y compilar un solo capítulo.
- **Aceptación:** capítulos en mayúsculas en texto e índice; índice a tres niveles con "Página", puntos guía y doble espacio antes de cada capítulo; anexos A–F y bibliografía en índice y marcadores; "9.2 Anexos" en hoja nueva; ningún título huérfano; el PDF equivale al anterior en contenido.

### Fase 4 — Tablas, figuras, notas, citas y bibliografía (P1)
- Secciones 2.5 y 2.6. Convierte las tablas y figuras existentes a los entornos nuevos sin cambiar su contenido; migra citas y bibliografía a biblatex/biber.
- **Aceptación:** cero `Overfull \hbox` > 2 pt; tabla del diccionario de datos sin solapes; rótulos y "Nota." uniformes; índices de tablas/figuras con prefijo; referencias cruzadas con prefijo automático; 0 citas indefinidas; cada obra listada está citada y cada cita está en la lista; el `.bib` refleja las 14 referencias originales; se retira la nota de borrador de la bibliografía.

### Fase 5 — Estilo visual, documentación y limpieza (P2)
- Sección 2.7 (acento, encabezado corrido, recuadros solo definidos, enlaces digitales/impresos, modo impresión).
- Añade a `.github/workflows/build.yml` un paso que ejecute `scripts/verificar` y falle si algo sale de tolerancia (si el tiempo lo permite; si no, déjalo como pendiente en el informe).
- Actualiza `README.md`: interruptores y su efecto, flujo con Zotero (Better BibTeX → `referencias.bib`), cómo compilar en Arch, Overleaf y CI, y la lista de verificación de entrega.
- **Aceptación:** modo impresión sin ningún color; encabezado ausente en preliminares y en primeras páginas de capítulo; márgenes y folio siguen dentro de tolerancia; tiempo de compilación ≲ 1,5× el inicial (justifica si lo supera).

### Fase 6 — Opcionales (P3, solo si sobra tiempo)
- Modo de bibliografía numerada de la guía §3.6; empaquetar fuentes libres en `fuentes/` (con licencias) para un PDF idéntico en local/Overleaf/CI (no empaquetes Arial).

## 6. Criterios de aceptación finales

- [ ] Carta; márgenes efectivos 3 / 2,5 / 2,5 / 2,5 cm (±0,15).
- [ ] Prosa a 27,6 ± 0,5 pt; sencillo en tablas, notas, captions, bibliografía interna.
- [ ] Solo Arial/Liberation Sans, Garamond/EB Garamond y la monoespaciada elegida; ninguna "LM".
- [ ] Carátula en una hoja conforme a §2.3; numeración y folio correctos.
- [ ] Preliminares en el orden definido; cada uno en página nueva.
- [ ] Capítulos en MAYÚSCULAS en texto e índice; índice a tres niveles con "Página"; anexos y bibliografía incluidos; marcadores completos.
- [ ] Rótulos consecutivos, "Nota." uniforme, cero desbordes > 2 pt, referencias cruzadas automáticas.
- [ ] Citas y bibliografía APA sin claves indefinidas.
- [ ] Modo final sin marcadores ni notas internas; modo impresión sin color.
- [ ] Contenido del autor intacto; `main` compila.

## 7. Prohibiciones

- No modificar texto, cifras ni argumentos del autor. No inventar referencias, DOIs, volúmenes ni datos.
- No escalar tablas por debajo de ~85 %; no usar capturas de pantalla como tablas.
- No colorear texto de cuerpo ni títulos. No cambiar Arial ni el tamaño de títulos fijado por la guía.
- No dejar espacios verticales fijos ni saltos de página manuales para "acomodar".
- No subir a `main` un commit que no compile. No versionar `build/` ni `main.pdf`.

## 8. Informe final (una sola vez, máximo una página)

1. Qué se hizo por fase (una línea cada una) y el enlace al último commit.
2. Tabla de métricas **antes → después**: páginas, márgenes, interlineado, fuentes, desbordes, tiempo de compilación.
3. Qué quedó pendiente o en P3.
4. Datos que faltan al `.bib` (campos vacíos que no inventaste).
5. Hasta tres dudas para el usuario (numeración, folio y bibliografía, a confirmar con el docente).