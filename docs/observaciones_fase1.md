# Observaciones de la transcripción: Fase 1 (del título a Objetivos)

Fuente: `Monografia_Prediccion_Espacial_TrufiApp(2).md`, líneas 1–381.
Este archivo **no forma parte del PDF**. Solo reúne lo que queda pendiente, lo que conviene mejorar y las observaciones de esta fase.

Leyenda: **[AÑADIR]** falta contenido que solo el autor puede aportar · **[MEJORAR]** el contenido existe, pero conviene revisarlo · **[OBS]** para tener en cuenta, sin acción obligatoria.

Estado de compilación: `make` sin errores y `scripts/verificar main.pdf` → *Todo dentro de tolerancia*. Resultado: 0 desbordes, 0 citas o referencias indefinidas y 0 marcadores de borrador en las páginas transcritas.

---

## Parte 1: carátula y preliminares

### Carátula (`configuracion.tex`, `secciones/00_caratula.tex`)
- Título nuevo en pirámide de 5 renglones. La carátula sigue ocupando una sola hoja. La leyenda ahora dice "DIPLOMADO EN CIENCIA DE DATOS – CUARTA VERSIÓN", como en el .md. El título corto del encabezado es "Demanda esperada de consultas de Trufi App por celda H3".
- **[MEJORAR]** El comentario de `configuracion.tex` que describe el ancho de cada renglón del título se refiere al título anterior. Conviene revisar a ojo la silueta de la pirámide: los renglones 1 y 2 miden casi lo mismo.

### Hoja de presentación y Aclaración (no transcritas, por decisión tuya)
- **[AÑADIR]** Faltan el nombre del asesor o tutor y los cuatro miembros del comité (Presidente, Coordinador y dos Tribunales). Mientras no existan, la hoja no puede salir limpia.
- **[OBS]** Hay una incoherencia a confirmar: la hoja de presentación dice "Trabajo de Grado… para la obtención del grado académico de **Licenciatura en Ingeniería Informática, modalidad Doble Titulación**". La carátula, en cambio, dice "Monografía presentada para obtener el **certificado de Diplomado**". Hay que definir cuál es la modalidad correcta antes de añadirla.
- **[OBS]** La guía no incluye la Aclaración en el orden de preliminares. Si decides añadirla, habría que ubicarla, probablemente después de la carátula.

### Dedicatoria y Agradecimientos (`secciones/01_preliminares.tex`)
- Transcritas del .md. Los agradecimientos ahora incluyen a los docentes y a Trufi Association.

### Resumen (`secciones/01_preliminares.tex`)
- **[MEJORAR] Excede una plana.** La guía pide que el resumen ocupe una sola hoja, incluidas las palabras clave. Con el formato exigido (Garamond 11,5 e interlineado 1,2), el texto del .md (~500 palabras) ocupa las páginas iv y v. Caben unas **290–300 palabras**, así que hay que recortar unas 200. Sugerencias:
  - Párrafo 2: resumir la lista de las siete técnicas, p. ej. "cuatro líneas base de tasa, dos GLM con offset poblacional y un gradient boosting".
  - Párrafo 3: quedarse con 2–3 cifras clave (devianza de 1.807,2 a 981,7, D² 76,5 % y δ de Cliff).
- **[OBS]** Las cifras del resumen (1.924.578 consultas; 1.381 celdas; 444 sin consultas; 20 % de bloques; devianza 1.807,2 → 981,7; D² 76,5 %; 0,91 frente a 0,64; Spearman ≥ 0,87; δ = +0,37; veinte celdas prioritarias) deberán cotejarse con el capítulo 7 cuando se transcriba.
- **[OBS]** "offset" y "gradient boosting" se dejaron sin cursiva, como en el .md. En el glosario, los términos en inglés sí van en cursiva. Conviene unificar el criterio.

### Glosario y abreviaturas (`secciones/11_glosario.tex`)
- Las 26 entradas del .md reemplazan al glosario anterior. Se eliminaron ML, POI, OSM, MAUP, OTP, PR-AUC y UUID, que ya no aparecen en el .md.
- **[OBS]** El glosario sigue el orden del .md. "δ de Cliff" queda entre "Devianza" y "EDA"; es correcto si se ordena por la letra "d".
- **[MEJORAR]** Si en los capítulos 6 y 7 aparecen siglas nuevas (p. ej. Q–Q, OLS, IC), habrá que añadirlas aquí.

### Índices (general, de tablas y de figuras)
- No se transcriben: LaTeX los genera solo. Además, las tablas y figuras se numeran de forma **consecutiva** (la "Tabla 4-1" del .md sale como "Tabla 1").

---

## Parte 2: capítulos 1 y 2

### 1. Introducción (`secciones/02_introduccion.tex`)
- Transcrita. Las citas (Cabrera y De Marchi Moyano, 2022) y (Chapman et al., 2000) están enlazadas a la bibliografía, y los números de capítulo son referencias automáticas.
- **[OBS]** El estilo APA de biblatex escribe "(Cabrera **&** De Marchi Moyano, 2022)", mientras que el .md usa "**y**". Es un ajuste global del formato de citas (afecta a todo el documento), así que queda para la fase de bibliografía.
- **[AÑADIR, opcional]** El .md no tiene figuras en los capítulos 1 a 5. Un **mapa de ubicación del eje metropolitano de Cochabamba** (municipios y área de estudio) ayudaría al lector que no conoce la zona. Podría ir aquí o en el capítulo 4.

### 2. Identificación del problema (`secciones/03_problema.tex`)
- Secciones 2.1 y 2.2 transcritas. La pregunta de investigación va como cita destacada en negrita.
- Corrección ortográfica aplicada: "archivos de exportacion" → "archivos de **exportación**".
- **[OBS]** Se eliminaron las subsecciones de la versión anterior (fricción, hipótesis H1/H2 y definiciones operativas). Los capítulos 6 a 9, que aún son la versión antigua, todavía mencionan H1/H2 y OE6/OE7. Esto se corrige al transcribirlos en las próximas fases.
- **[OBS]** Queda un alias interno temporal (`sec:friccion-a-brecha`) para que el apartado 7.1 antiguo siga compilando. Se retira al transcribir el 7.1.
- **[MEJORAR, opcional]** El dato "Cercado concentraba cerca del 85 %… 801 de 863 zonas" proviene de Angulo Andrade (2024). Conviene verificar la página exacta por si el tribunal la pide.

### Bibliografía añadida en esta fase (`referencias.bib`)
- `angulo2024`: tiene el tipo "Monografía de Diplomado…" y la UMSS.
- `cabrera2022`: urbe. Revista Brasileira de Gestão Urbana, 14.
- **[AÑADIR]** Faltan los datos para completar `cabrera2022`: número o artículo, páginas o e-location y DOI. El .md solo trae el volumen.

---

## Parte 3: capítulos 3, 4 y 5

### 3. Justificación (`secciones/04_justificacion.tex`)
- Cinco párrafos corridos, sin subsecciones, como en el .md.
- **[MEJORAR, opcional]** El último párrafo ("Es menester destacar…") repite lo que ya dice el último párrafo de la Introducción sobre la estructura del documento. Podría eliminarse o acortarse.
- **[OBS]** La guía (§2.3) suele esperar que se distingan la justificación práctica, la técnica y la social. El texto las cubre en párrafos ("Desde el punto de vista práctico…", "Desde la perspectiva de la Ciencia de Datos…" y beneficiarios), pero no tiene subtítulos. Está bien así si el tribunal no los exige.

### 4. Alcance (`secciones/05_alcance.tex`)
- Lista de delimitación, Tabla 1 "Perfil inicial de los datos disponibles" con su *Nota.*, y párrafo de limitaciones.
- **[OBS]** "según el procedimiento descrito en el apartado 7.3.3" queda por ahora como texto fijo. Al transcribir el capítulo 7 se convertirá en referencia automática al apartado "Delimitación del área de estudio".
- **[OBS]** La tabla dice "ediciones 2022 y 2023" de Kontur, pero la bibliografía del .md solo cita Kontur (2023). Hay que confirmar si también se usó la edición 2022 y, en ese caso, citarla.

### 5. Objetivos (`secciones/06_objetivos.tex`)
- Objetivo general y OE1 a OE5 transcritos. Se eliminaron la matriz de coherencia antigua (OE1 a OE7) y las notas "(Completado…)".
- **[OBS]** La correspondencia entre objetivos y fases aparece en el .md como Tabla 7-1, en el capítulo 7. Se transcribirá en esa fase.

---

## Pendientes para las próximas fases (arrastrados de esta)
1. Convertir "apartado 7.3.3" en referencia automática.
2. Retirar el alias `sec:friccion-a-brecha`.
3. Cotejar las cifras del Resumen con el capítulo 7.
4. Bibliografía: cargar las 30 referencias del .md, completar "consultado [fecha]" en Kontur y Uber H3, y ajustar "&" → "y" en las citas.

---

## Figuras (añadido el 28-09-2026)
- **[OBS]** Las 23 figuras del .md ya tienen imagen en `imagenes/`, ordenadas por sección. La correspondencia completa, las figuras generadas pero no citadas y cómo resincronizarlas (`make figuras`) están en [figuras_cap7.md](figuras_cap7.md).
- **[OBS]** Hay un envoltorio TEMPORAL de `\includegraphics` en `preambulo.tex`: omite las 12 `fig_*.png` antiguas que aún piden los `08_0N_*.tex`. Se retira al transcribir el capítulo 7.
