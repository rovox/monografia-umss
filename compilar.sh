#!/usr/bin/env bash
# ============================================================
#  Compila la monografía con latexmk (recompila tantas veces
#  como haga falta hasta que índices y referencias queden
#  estables; ya no hay que acordarse de "dos pasadas a mano").
#  Los archivos auxiliares (.aux/.log/.toc/.lof/.lot/...) se
#  generan dentro de build/, nunca en la raíz del proyecto.
#  Uso:  ./compilar.sh          -> compila (LuaLaTeX)
#        ./compilar.sh watch    -> recompila en cada guardado
#        ./compilar.sh limpiar  -> borra build/ y main.pdf
# ============================================================
set -e
cd "$(dirname "$0")"

if ! command -v latexmk >/dev/null 2>&1; then
  echo "ERROR: no se encontró 'latexmk'. Instala TeX Live (incluye latexmk)."
  exit 1
fi

case "$1" in
  limpiar)
    latexmk -C
    rm -rf build
    echo "build/ y main.pdf eliminados."
    exit 0
    ;;
  watch)
    echo "Modo edición continua (Ctrl+C para salir)..."
    exec latexmk -pvc
    ;;
esac

echo "Compilando con latexmk (lualatex)..."
latexmk

if [ -f main.pdf ]; then
  echo "Listo: main.pdf generado."
  grep -i "undefined" build/main.log > /dev/null 2>&1 \
    && echo "AVISO: hay referencias sin resolver, revisa build/main.log." \
    || echo "Sin referencias indefinidas."
else
  echo "ERROR: no se generó main.pdf. Revisa build/main.log."
  exit 1
fi
