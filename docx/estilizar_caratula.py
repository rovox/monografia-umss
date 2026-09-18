#!/usr/bin/env python3
"""Ajusta tamaño y centrado de los párrafos de la carátula en el .docx ya
generado por Pandoc (docx/00_caratula_docx.tex + convertir_docx.sh).

Por qué un post-proceso y no LaTeX: se comprobó empíricamente que el lector
LaTeX de Pandoc descarta \\begin{center}, \\Large/\\LARGE y \\fontsize sin
avisar (no hay forma de pedirle desde el .tex que un párrafo sea más grande
o esté centrado). La única vía confiable es editar el XML del .docx
después de la conversión, igual que ya hace estilizar_referencia.py con los
estilos globales.

Identifica los párrafos por POSICIÓN (los primeros del cuerpo del
documento, ver docx/00_caratula_docx.tex): la tabla de logos (índice 0) y
luego, en orden, título / leyenda / postulante / ciudad / año (1-5). Si
cambias el contenido de docx/00_caratula_docx.tex, revisa que los índices
aquí abajo sigan correspondiendo a los mismos párrafos.

Uso:
    python3 estilizar_caratula.py archivo.docx
"""
import re
import sys
import zipfile
from pathlib import Path

# índice (entre los bloques w:p/w:tbl de nivel superior) -> (tamaño en
# medios-punto, centrado)
AJUSTES = {
    1: (40, True),   # título de la monografía (20 pt)
    2: (24, True),   # "MONOGRAFÍA PRESENTADA PARA..."
    3: (28, False),  # "POSTULANTE: ..." (alineado a la izquierda, como el PDF)
    4: (24, True),   # "Cochabamba -- Bolivia"
    5: (24, True),   # año
}

BLOCK_RE = re.compile(r"<w:p\b.*?</w:p>|<w:tbl\b.*?</w:tbl>", re.S)
RPR_RE = re.compile(r"<w:rPr>(.*?)</w:rPr>", re.S)
SZ_RE = re.compile(r"<w:sz[^/]*/><w:szCs[^/]*/>|<w:sz[^/]*/>|<w:szCs[^/]*/>")
PPR_RE = re.compile(r"<w:pPr>(.*?)</w:pPr>")


def _set_size(rpr_inner: str, size: int) -> str:
    inner = SZ_RE.sub("", rpr_inner)
    return inner + f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>'


def _apply_to_paragraph(block: str, size: int, center: bool) -> str:
    def repl_rpr(m):
        return "<w:rPr>" + _set_size(m.group(1), size) + "</w:rPr>"

    if RPR_RE.search(block):
        block = RPR_RE.sub(repl_rpr, block)
    else:
        # No rPr yet on the run(s): add one right after each <w:r>'s opening tag.
        block = re.sub(
            r"(<w:r(?:\s[^>]*)?>)",
            lambda m: m.group(1) + f'<w:rPr><w:sz w:val="{size}"/><w:szCs w:val="{size}"/></w:rPr>',
            block,
        )

    if center:
        jc = '<w:jc w:val="center"/>'
        if PPR_RE.search(block):
            block = PPR_RE.sub(lambda m: f"<w:pPr>{m.group(1)}{jc}</w:pPr>", block, count=1)
        else:
            block = block.replace("<w:p>", f"<w:p><w:pPr>{jc}</w:pPr>", 1)
    return block


def main() -> None:
    if len(sys.argv) != 2:
        print(__doc__)
        raise SystemExit(1)
    path = Path(sys.argv[1])

    with zipfile.ZipFile(path, "r") as zin:
        names = zin.namelist()
        contents = {n: zin.read(n) for n in names}

    xml = contents["word/document.xml"].decode("utf-8")
    body_start = xml.index("<w:body>") + len("<w:body>")
    head, body = xml[:body_start], xml[body_start:]

    # Sustitución EN EL LUGAR sobre el string original: nunca se reconstruye
    # el documento concatenando coincidencias. El cuerpo real contiene, entre
    # los w:p/w:tbl de nivel superior, marcadores de marcador de posición
    # (w:bookmarkStart/w:bookmarkEnd, uno por cada \label del documento) que
    # esta expresión regular no captura; reconstruir "a mano" perdía esos
    # fragmentos y corrompía el XML. re.sub con un contador solo toca los
    # bloques 1..5 y deja absolutamente todo lo demás intacto.
    counter = {"i": 0}

    def repl(m: re.Match) -> str:
        idx = counter["i"]
        counter["i"] += 1
        block = m.group(0)
        if idx in AJUSTES and block.startswith("<w:p"):
            size, center = AJUSTES[idx]
            block = _apply_to_paragraph(block, size, center)
        return block

    body = BLOCK_RE.sub(repl, body, count=max(AJUSTES) + 1)
    xml = head + body

    contents["word/document.xml"] = xml.encode("utf-8")

    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zout:
        for name in names:
            zout.writestr(name, contents[name])

    print(f"Carátula ajustada en {path}")


if __name__ == "__main__":
    main()
