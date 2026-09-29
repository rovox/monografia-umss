# Plantilla LaTeX — Monografía UMSS

[![Compilar monografía](https://github.com/rovox/monografia-umss/actions/workflows/build.yml/badge.svg)](https://github.com/rovox/monografia-umss/actions/workflows/build.yml)

Universidad Mayor de San Simón · Facultad de Ciencias y Tecnología · Dirección de Posgrado
Diplomado en Ciencia de Datos — 4ta. Versión

Plantilla construida siguiendo la *Guía para la Elaboración de Monografía V1.0 (2026)*.
Compila sin errores y fue verificada página por página.

---

## 1. Compilación

El proyecto usa **latexmk** como pipeline de compilación: reintenta automáticamente
hasta que los índices y las referencias cruzadas quedan estables (ya no hay que
acordarse de compilar "dos veces a mano"), y todos los archivos auxiliares
(`.aux`, `.log`, `.toc`, `.lof`, `.lot`, `.fls`, `.fdb_latexmk`) se generan dentro
de `build/`, nunca en la raíz del proyecto. `main.pdf` se sigue generando en la raíz.

```bash
./compilar.sh            # compila (equivalente: make)
./compilar.sh watch      # recompila en cada guardado, ideal para editar (equivalente: make watch)
./compilar.sh limpiar    # borra build/ y main.pdf (equivalente: make clean)
```

El motor y las opciones están fijados en `.latexmkrc` (LuaLaTeX, `-synctex=1` para
saltar del PDF al código fuente desde tu editor). No lo edites salvo que necesites
cambiar de motor.

### Alternativa manual (sin latexmk)

```bash
lualatex main.tex
lualatex main.tex     # segunda pasada: resuelve índices y referencias cruzadas
```

En Windows, ejecuta los dos comandos `lualatex` a mano o usa Git Bash.

XeLaTeX también funciona (`xelatex main.tex`, dos veces).

**Siempre dos pasadas.** La primera escribe los archivos auxiliares (`.toc`, `.lof`,
`.lot`, `.aux`); la segunda los lee para completar los índices y las referencias
cruzadas. Si compilas solo una vez, verás índices vacíos y signos `??` en las
referencias. (Esto es exactamente lo que `latexmk` automatiza arriba.)

### No uses pdflatex

Esta plantilla carga fuentes del sistema (Arial, Garamond) mediante `fontspec`, y
pdflatex no puede hacerlo: solo maneja fuentes Type1 de 8 bits, sin soporte real de
OpenType ni de Unicode en la entrada. Con pdflatex habría que falsificar Arial con
métricas de sustitución, lo cual contradice el requisito de la guía (Arial 12 en el
cuerpo, Garamond 11.5 en el Resumen). LuaLaTeX carga la fuente real instalada.

### En Overleaf

Menú *Menu → Compiler → LuaLaTeX*. Overleaf ya trae Arial y EB Garamond, así que no
requiere ninguna instalación adicional.

---

## 1B. Exportar a Word (.docx)

```bash
./convertir_docx.sh            # genera monografia.docx
./convertir_docx.sh plantilla  # regenera docx/referencia_umss.docx (normalmente no hace falta)
./convertir_docx.sh limpiar    # borra build/docx/ y monografia.docx
```

Usa **Pandoc**. `tex2word` (Python, PyPI) y `tex2word-cli` (Rust, crates.io) sí
existen, pero se probaron contra este documento real y ambos pierden o corrompen
contenido de forma no determinista (truncan capítulos enteros, o `\chapter`
directamente no está soportado en la versión Rust) — quedaron descartados hasta
que maduren. El script arma un documento LaTeX equivalente con un preámbulo
compatible (`docx/preambulo_pandoc.tex`, en vez de `preambulo.tex`, que usa
comandos de `memoir`/`fontspec` que Pandoc no necesita) y lo convierte con el
estilo de partida de `docx/referencia_umss.docx` (Liberation Sans, interlineado
doble, márgenes 3/2.5/2.5/2.5 cm — una aproximación a la guía; el estilo final
se ajusta en Word en un clic).

Pandoc reconstruye capítulos, secciones, tablas, figuras, negritas/cursivas y
referencias cruzadas (`\label`/`\ref`) como un `.docx` nativo y editable — no es
una imagen del PDF. La única página que no se convierte con el resto es la
carátula: `\fontsize{}{}` y los `\minipage` en fila que usa
`secciones/00_caratula.tex` no tienen equivalente en Pandoc (se comprobó que
ni `\Large`/`\LARGE` ni `\begin{center}` sobreviven la conversión), así que el
script usa en su lugar `docx/00_caratula_docx.tex` (misma información, con una
tabla de 3 columnas sin bordes para los logos) y luego `docx/estilizar_caratula.py`
ajusta tamaño y centrado directamente en el XML del `.docx` ya generado.

Lo único que **no** automatiza (limitación de Pandoc, no de este script) es el
índice general y el índice de tablas/figuras, porque Pandoc solo puede
insertarlos al principio del documento: se generan una vez, a mano, dentro de
Word después de abrir el archivo:

1. *Referencias → Tabla de contenido*, después de la carátula/preliminares.
2. *Referencias → Insertar tabla de ilustraciones*, una vez para el estilo
   `TableCaption` (índice de tablas) y otra para `ImageCaption` (índice de
   figuras) — son los estilos que Pandoc ya aplicó a cada `\caption`.

Si agregas una nueva sección a `main.tex`, agrégala también al arreglo
`SECCIONES` de `convertir_docx.sh` (mismo orden).

---

## 2. Estructura del proyecto

```
main.tex                  Ensambla el documento. Aquí editas los datos del proyecto.
preambulo.tex             Toda la configuración de formato, comentada regla por regla.
compilar.sh               Script de compilación (usa latexmk; ver sección 1).
Makefile                  Alias de compilar.sh (make / make watch / make clean).
.latexmkrc                Configuración del motor de compilación (LuaLaTeX).
build/                    Archivos auxiliares de la compilación (generado, no versionado).
convertir_docx.sh         Exporta a Word con Pandoc (ver sección 1B).
docx/
  preambulo_pandoc.tex    Preámbulo compatible con Pandoc (equivalente a preambulo.tex).
  referencia_umss.docx    Estilos Word de partida (Normal/Título) para la exportación.
  estilizar_referencia.py Genera/actualiza referencia_umss.docx (uso interno del script).
  00_caratula_docx.tex    Carátula compatible con Pandoc (reemplaza a 00_caratula.tex solo en el docx).
  estilizar_caratula.py   Ajusta tamaño/centrado de la carátula ya convertida (uso interno del script).
README.md                 Este archivo.
imagenes/
  logo_umss.png           Reemplazar por el logo real
  logo_facultad.png       Reemplazar por el logo real
  logo_posgrado.png       Reemplazar por el logo real
secciones/
  00_caratula.tex         Carátula (regla 3.3 + modelo del Anexo)
  01_preliminares.tex     Dedicatoria, agradecimientos, resumen, glosario
  02_introduccion.tex     1. Introducción
  03_problema.tex         2. Identificación del Problema
  04_justificacion.tex    3. Justificación
  05_alcance.tex          4. Alcance
  06_objetivos.tex        5. Objetivos
  07_marco_teorico.tex    6. Marco Teórico
    07_01..07_05_*.tex    Sus cinco secciones (6.1 a 6.5), una por archivo
  08_desarrollo.tex       7. Desarrollo (seis fases de CRISP-DM)
  09_conclusiones.tex     8. Conclusiones y Recomendaciones
  10_bibliografia.tex     9. Bibliografía y Anexos
```

El orden de los capítulos sigue el índice modelo del Anexo A de la guía.

---

## 3. Cómo empezar

### Paso 1 — Tus datos

En `main.tex`, edita únicamente estas cinco líneas:

```latex
\newcommand{\tituloMonografia}{Título de la monografía}
\newcommand{\nombreDiplomado}{Ciencia de Datos}
\newcommand{\nombreVersion}{4ta.}
\newcommand{\nombrePostulante}{Nombre Completo del Postulante}
\newcommand{\anioMonografia}{2026}
```

La carátula y los metadatos del PDF se completan solos a partir de estos valores.

### Paso 2 — Los logos

Reemplaza los tres archivos de `imagenes/` por los logos institucionales reales,
conservando los mismos nombres. Los incluidos son marcadores de posición generados
para poder verificar la maquetación.

Si tus logos tienen proporciones distintas (el de la UMSS es vertical; el de la
Facultad, horizontal), ajusta las alturas en `secciones/00_caratula.tex` — están
todas en `height=1.5cm`.

### Paso 3 — El contenido

Cada archivo de `secciones/` trae el texto de relleno entre corchetes, con la
consigna exacta de la guía para esa sección. Reemplázalos por tu contenido.

**Los archivos de `secciones/` no deben contener formato.** Todo el estilo vive en
`preambulo.tex`, así un cambio se hace una sola vez y aplica a todo el documento.

### Título largo en la carátula

La guía pide forma de pirámide invertida cuando el título ocupa más de una línea.
Escríbelo con `\\` donde quieras el corte, dejando la primera línea más larga:

```latex
\newcommand{\tituloMonografia}{Primera línea más larga del título\\segunda más corta}
```

---

## 4. Requisitos de la guía y cómo se cumplen

| Requisito | Regla | Implementación |
|---|---|---|
| Arial 12 en el cuerpo | Instr. 3 | `\setmainfont` + opción de clase `12pt` |
| Títulos Arial 14 negrilla | Instr. 3 | Estilo de capítulo `umss` |
| Garamond 11.5, interlineado 1.2 en Resumen | Preliminar | `\garamondfont` + `\interlineadoResumen` |
| Márgenes 3 / 2,5 / 2,5 / 2,5 cm | Instr. 3 | `geometry` |
| Interlineado doble | Instr. 3 | `\DoubleSpacing*` de memoir |
| Folio inferior centrado | 3.1 | `\pagestyle{plain}` |
| Preliminares en romanos i, ii, iii | 3.1 | `\frontmatter` |
| Cuerpo en arábigos desde 1 | 3.1 | `\mainmatter` |
| Carátula y dedicatoria sin folio, pero contadas | 3.1 | `\thispagestyle{empty}` |
| Secciones principales en página nueva | 3.1 / 3.4 | `\chapter` |
| Índice sin negrillas | 3.4 | `\cftchapterfont` y `\l@section` redefinidos |
| Índice con sangría en subtítulos | 3.4 | `\cftsetindents` y `\l@subsection` |
| Puntos de relleno hasta el folio | 3.4 | `\cftdotfill` |
| Palabra "Página" sobre la columna | 3.4 | `\cfttocbeforelisthook` |
| Índice de tablas y de figuras | Preliminar | `\listoftables*` / `\listoffigures*` |
| "Tabla N" negrita + título en cursiva, arriba | 3.2 | `captionsetup` + `\caption` antes del contenido |
| Solo líneas horizontales en tablas | 3.2 | `booktabs` |
| Línea "Fuente:" en cursiva | 3.2 | `\fuente{}` |
| Citas (Autor, año) | 3.5 | `\cita{}{}` |
| Registro bibliográfico institucional | 3.6 | `bibliografiaUMSS` + `\registrobiblio` |

---

## 5. Comandos propios de esta plantilla

```latex
\cita{Fardel}{1984}              → (Fardel, 1984)
\citap{Fardel}{1984}{45}         → (Fardel, 1984, p. 45)

\fuente{Elaboración propia.}     Línea de fuente bajo una tabla o figura

\interlineadoSimple              Interlineado 1   (tablas, bibliografía)
\interlineadoResumen             Interlineado 1.2 (resumen, glosario)

\ph{texto}                       Marcador de posición seguro DENTRO de tablas
```

### Sobre `\ph{}` — importante

Dentro de un `tabular`, si una celda empieza con corchete justo después de `\\`,
LaTeX interpreta ese corchete como el argumento opcional de `\\` (un espaciado
vertical), intenta leerlo como una longitud y **la compilación se cuelga sin
mensaje de error**. Por eso los textos de relleno dentro de tablas usan `\ph{...}`.

Si escribes tus propias tablas, nunca empieces una celda con `[` directamente.

---

## 6. Tabla y figura: plantillas listas

El rótulo queda arriba porque `\caption` va **antes** del contenido. Si lo pones
después, el título aparecerá abajo.

```latex
\begin{table}[htbp]
  \centering
  \caption{Título de la tabla}
  \label{tab:mi-etiqueta}
  \interlineadoSimple
  \begin{tabular}{lll}
    \toprule
    \textbf{Columna 1} & \textbf{Columna 2} & \textbf{Columna 3} \\
    \midrule
    dato & dato & dato \\
    \bottomrule
  \end{tabular}
  \fuente{Elaboración propia.}
\end{table}
```

```latex
\begin{figure}[htbp]
  \centering
  \caption{Título de la figura}
  \label{fig:mi-etiqueta}
  \includegraphics[width=0.7\textwidth]{imagenes/mi_grafico.png}
  \fuente{Elaboración propia.}
\end{figure}
```

Cítalas en el texto con `\ref{tab:mi-etiqueta}` y `\ref{fig:mi-etiqueta}`: la
numeración se ajusta sola si insertas o mueves elementos.

---

## 7. Bibliografía

```latex
\registrobiblio{APELLIDO, N.}{Año}{Título de la obra}{Datos editoriales, lugar, p. N}
```

Produce el formato de la sección 3.6: número de registro y autor en negrilla, año
entre paréntesis, título en cursiva. El interlineado simple dentro del registro y
el doble entre registros se aplican automáticamente.

`secciones/10_bibliografia.tex` incluye un ejemplo de cada tipo previsto por la
guía: libro, libro con más de dos autores, libro editado, artículo de revista,
capítulo de libro, documento técnico, tesis, revista electrónica y página web.

---

## 8. Dos advertencias para tu instalación local

### Fuentes

La plantilla usa una cadena de respaldo verificada:

- **Cuerpo:** Arial → Liberation Sans
- **Resumen:** Garamond → EB Garamond → Latin Modern Roman

En Windows y macOS cargará Arial auténtica sin que hagas nada. En Linux usará
Liberation Sans, que es métricamente idéntica a Arial (mismos anchos de carácter):
el documento no se recompagina al cambiar de máquina.

Para el Resumen conviene instalar **EB Garamond** (gratuita,
<https://fonts.google.com/specimen/EB+Garamond>) si no tienes Garamond. El documento
compila igual sin ella, pero el Resumen saldrá en otra serif.

Verifica qué fuente se usó realmente buscando `LiberationSans` o `Arial` en
`main.log`.

### Silabación en español

Si tu instalación de TeX no trae los patrones de silabación del español, verás:

```
Package polyglossia Warning: No hyphenation patterns were loaded for `spanish'
```

Es solo un aviso: el documento compila, pero algunos renglones quedan con espaciado
irregular porque las palabras no se parten. Se soluciona instalando el paquete de
idioma:

- **TeX Live:** `tlmgr install hyphen-spanish`
- **Debian/Ubuntu:** `sudo apt install texlive-lang-spanish`
- **MiKTeX:** se instala solo al compilar
- **Overleaf:** ya viene incluido

---

## 9. Antes de entregar

Lista de verificación de la guía:

- [ ] ¿El problema está claramente definido?
- [ ] ¿La justificación explica por qué y para qué se realiza el proyecto?
- [ ] ¿El alcance establece límites claros?
- [ ] ¿El objetivo general y los específicos son coherentes entre sí?
- [ ] ¿El marco teórico contiene únicamente fundamentos relacionados con el proyecto?
- [ ] ¿El desarrollo evidencia las seis fases de CRISP-DM?
- [ ] ¿Las decisiones de preparación y modelado están justificadas?
- [ ] ¿Las métricas utilizadas son apropiadas para el problema?
- [ ] ¿Los resultados son interpretados y no solo mostrados?
- [ ] ¿Las conclusiones responden a los objetivos?
- [ ] ¿Las recomendaciones se derivan de los resultados y limitaciones?
- [ ] ¿Las tablas y figuras están numeradas, tituladas y explicadas?
- [ ] ¿Las fuentes utilizadas están citadas y registradas en la bibliografía?
- [ ] ¿Los anexos contienen las evidencias técnicas necesarias?
- [ ] ¿Existe coherencia entre el índice, los títulos y el contenido final?

Técnico:

- [ ] Compilado **dos veces** al final
- [ ] Sin `??` ni referencias indefinidas (busca `undefined` en `main.log`)
- [ ] Logos reales en lugar de los marcadores de posición
- [ ] Sin texto de relleno entre corchetes olvidado
- [ ] Índices reflejan los títulos finales

---

## 10. Contribuir / mantenimiento

- Cada `push` o `pull request` dispara un workflow de GitHub Actions
  (`.github/workflows/build.yml`) que compila `main.tex` con LuaLaTeX y sube
  `main.pdf` como artefacto descargable. Si el badge de arriba está en rojo,
  la compilación se rompió con el último cambio.
- El `build/` generado localmente y `main.pdf` no se versionan (ver
  `.gitignore`); cada quien compila su propia copia.
- Antes de un PR grande, corre `./compilar.sh` localmente y revisa que no
  aparezcan referencias indefinidas.

## Licencia

Este proyecto está bajo licencia [CC BY 4.0](LICENSE): puedes reutilizar y
adaptar la plantilla dando crédito.
