# Envoltorio fino sobre latexmk (ver .latexmkrc). Alterna con ./compilar.sh.
.PHONY: all watch clean figuras pendientes

all:
	latexmk

watch:
	latexmk -pvc

clean:
	latexmk -C
	rm -rf build

# Copia desde trufi-data-science las figuras que cita el capítulo 7
# (origen configurable con TRUFI_REPO; ver docs/figuras_cap7.md).
figuras:
	scripts/sincronizar_figuras

# Genera docs/PENDIENTES.md con contenido faltante y advertencias LaTeX.
pendientes:
	scripts/pendientes
