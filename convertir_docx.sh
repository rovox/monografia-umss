#!/usr/bin/env bash
# ============================================================
#  Convierte la monografía (secciones/*.tex) a un único .docx
#  editable de Word, usando Pandoc.
#  ------------------------------------------------------------
#  Por qué Pandoc y no "tex2word"/"rstex2word": esos nombres no
#  corresponden a un paquete mantenido de CTAN/TeX Live instalable
#  aquí. Pandoc es la herramienta libre estándar para este tipo de
#  conversión, ya viene instalada en este entorno, y entiende
#  directamente la estructura real de este documento (capítulos,
#  tablas booktabs/tabularx, figuras, \label/\ref, listas). Este
#  script solo le da un preámbulo compatible (docx/preambulo_pandoc.tex)
#  en lugar de preambulo.tex, que usa comandos de memoir/fontspec
#  que Pandoc no necesita (el estilo lo pone la plantilla Word).
#
#  Uso:
#    ./convertir_docx.sh              -> genera monografia.docx
#    ./convertir_docx.sh plantilla    -> regenera docx/referencia_umss.docx
#                                         (punto de partida de estilos Word;
#                                         normalmente no hace falta rehacerlo)
#    ./convertir_docx.sh limpiar      -> borra build/docx/ y monografia.docx
# ============================================================
set -euo pipefail
cd "$(dirname "$0")"

BUILD_DIR="build/docx"
FLAT_TEX="$BUILD_DIR/monografia_flat.tex"
REFERENCIA="docx/referencia_umss.docx"
SALIDA="monografia.docx"

# Orden real de inclusión de secciones, tomado de main.tex (frontmatter
# sin numerar + mainmatter numerado 1..9). Si se agrega o reordena un
# \include en main.tex, actualizar esta lista.
SECCIONES=(
  00_caratula
  01_preliminares
  02_introduccion
  03_problema
  04_justificacion
  05_alcance
  06_objetivos
  07_marco_teorico
  08_desarrollo
  09_conclusiones
  10_bibliografia
)

generar_plantilla() {
  echo "Generando plantilla de referencia docx/referencia_umss.docx..."
  mkdir -p docx
  tmp_ref="$(mktemp --suffix=.docx)"
  pandoc -o "$tmp_ref" --print-default-data-file reference.docx
  python3 docx/estilizar_referencia.py "$tmp_ref" "$REFERENCIA"
  rm -f "$tmp_ref"
}

case "${1:-}" in
  limpiar)
    rm -rf "$BUILD_DIR" "$SALIDA"
    echo "build/docx/ y $SALIDA eliminados."
    exit 0
    ;;
  plantilla)
    generar_plantilla
    exit 0
    ;;
esac

if ! command -v pandoc >/dev/null 2>&1; then
  echo "ERROR: no se encontró 'pandoc'. Instálalo (p. ej. 'pacman -S pandoc' / 'apt install pandoc')."
  exit 1
fi

if [ ! -f "$REFERENCIA" ]; then
  generar_plantilla
fi

mkdir -p "$BUILD_DIR"

echo "Ensamblando documento plano para Pandoc..."
{
  cat docx/preambulo_pandoc.tex
  echo
  # Variables del proyecto (título, postulante, versión, año):
  # se extraen en vivo de main.tex para no duplicarlas a mano.
  sed -n '/^\\newcommand{\\tituloMonografia}/,/^\\newcommand{\\anioMonografia}/p' main.tex
  echo
  echo '\begin{document}'
  echo
  for s in "${SECCIONES[@]}"; do
    echo "% ---------- secciones/${s}.tex ----------"
    if [ "$s" = "00_caratula" ]; then
      # Versión simplificada compatible con Pandoc (ver el archivo
      # para la explicación); secciones/00_caratula.tex es solo para PDF.
      cat "docx/00_caratula_docx.tex"
    else
      cat "secciones/${s}.tex"
    fi
    echo
  done
  echo '\end{document}'
} > "$FLAT_TEX"

# El glosario usa \begin{description}[leftmargin=...,style=nextline,font=\bfseries]
# (sintaxis extendida de enumitem): ese argumento opcional confunde al lector
# LaTeX de pandoc y le hace perder las etiquetas \item[TÉRMINO]. Es el único
# entorno del documento con argumento opcional propio (los [htbp] de table/figure
# y los [t]{...} de minipage sí los procesa bien), así que se retira solo aquí.
sed -i 's/\\begin{description}\[[^]]*\]/\\begin{description}/' "$FLAT_TEX"

echo "Convirtiendo con Pandoc (esto puede tardar unos segundos)..."
# Sin --toc: pandoc siempre inserta el índice generado al PRINCIPIO del
# documento (antes de la carátula), que no es el orden de la guía UMSS
# (carátula -> preliminares -> índice -> cuerpo). En su lugar, generar el
# índice real DENTRO de Word una sola vez tras abrir el archivo:
# Referencias > Tabla de contenido (usa los estilos Heading 1/2/3 que
# --number-sections ya dejó bien puestos) e, igual, Referencias > Insertar
# tabla de ilustraciones para el índice de tablas/figuras (estilos
# TableCaption/ImageCaption que pandoc ya aplicó a cada \caption).
pandoc "$FLAT_TEX" \
  -f latex -t docx \
  --resource-path=".:imagenes" \
  --reference-doc="$REFERENCIA" \
  --number-sections \
  --standalone \
  -o "$SALIDA"

if [ -f "$SALIDA" ]; then
  python3 docx/estilizar_caratula.py "$SALIDA"
  echo "Listo: $SALIDA generado."
  echo
  echo "Pendiente de un clic en Word (no lo hace pandoc):"
  echo "  1. Referencias > Tabla de contenido, después de la carátula/preliminares."
  echo "  2. Referencias > Insertar tabla de ilustraciones, una para 'TableCaption'"
  echo "     (índice de tablas) y otra para 'ImageCaption' (índice de figuras)."
  echo "  3. Revisar los estilos 'Normal' / 'Título 1' si quieres Arial real en vez"
  echo "     de Liberation Sans (Inicio > Estilos > clic derecho > Modificar)."
else
  echo "ERROR: no se generó $SALIDA. Revisa la salida de pandoc arriba."
  exit 1
fi
