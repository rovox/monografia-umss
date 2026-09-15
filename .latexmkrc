# ============================================================
#  latexmk config — motor LuaLaTeX, archivos auxiliares fuera
#  del proyecto (build/), PDF final en la raíz (como siempre).
#  Uso: latexmk            (compila, reintenta hasta estabilizar)
#       latexmk -pvc       (recompila en cada guardado)
#       latexmk -C         (limpia build/ y main.pdf)
# ============================================================
@default_files = ('main.tex');  # main.tex hace \input{preambulo.tex}, y ese
                                 # archivo contiene el \documentclass. Sin fijar
                                 # el archivo raíz, latexmk detecta \documentclass
                                 # dentro de preambulo.tex y lo trata como un
                                 # segundo documento a compilar (falla: no tiene
                                 # \begin{document}).
$pdf_mode = 4;          # 4 = generar PDF vía lualatex
$lualatex = 'lualatex -no-mktex=tfm -interaction=nonstopmode -file-line-error -synctex=1 %O %S';
$aux_dir  = 'build';    # .aux/.log/.toc/.lof/.lot/.fls/.fdb_latexmk aquí
$out_dir  = '.';        # main.pdf queda en la raíz del proyecto
# \include{secciones/...} necesita build/secciones/ para poder escribir los
# .aux de cada sección; latexmk no siempre lo crea solo antes de la 1a pasada.
mkdir 'build' unless -d 'build';
mkdir 'build/secciones' unless -d 'build/secciones';
$pdf_previewer = 'xdg-open %O %S';
$clean_ext = 'synctex.gz run.xml bbl bcf';
