#!/usr/bin/env python3
"""Aplica una aproximación de la guía UMSS (Arial/Liberation Sans, doble
espacio, márgenes 3/2.5/2.5/2.5 cm) a un reference-doc de Pandoc, editando
directamente el XML interno del .docx (no requiere python-docx).

Uso:
    python3 estilizar_referencia.py entrada.docx salida.docx

Esto NO pretende reproducir el formato exacto del PDF (numeración de
capítulos "1.", interlineado calibrado por memoir, etc.): pandoc aplica
--number-sections y el resto del ajuste fino queda para retocar en Word
una sola vez (Inicio > Estilos > modificar "Normal"/"Título 1"), ya que
--reference-doc solo controla el PUNTO DE PARTIDA de esos estilos.
"""
import re
import shutil
import sys
import zipfile
from pathlib import Path

NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
}
W = "{%s}" % NS["w"]

CM_TO_TWIPS = 1440 / 2.54  # 1 cm en unidades de veinteavos de punto (twips)


def twips(cm: float) -> str:
    return str(round(cm * CM_TO_TWIPS))


FONT_BODY = "Liberation Sans"   # sustituto libre y métricamente idéntico a Arial
FONT_SIZE_BODY_HALFPT = "24"    # 12 pt (OOXML mide en medios punto)
FONT_SIZE_H1_HALFPT = "28"      # 14 pt, negrilla -> capítulos (Instrucción 3)
LINE_DOUBLE = "480"             # w:line en modo "auto" = interlineado doble


def patch_styles_xml(xml_text: str) -> str:
    # --- Normal: fuente y tamaño del cuerpo, interlineado doble ---
    def add_or_replace(rpr_or_ppr_block: str, tag: str, xml_snippet: str) -> str:
        pattern = re.compile(rf"<w:{tag}[^/]*/>")
        if pattern.search(rpr_or_ppr_block):
            return pattern.sub(xml_snippet, rpr_or_ppr_block, count=1)
        return rpr_or_ppr_block + xml_snippet

    def patch_style(xml_text: str, style_id: str, *, font: str, size_halfpt: str,
                     bold: bool = False, center: bool = False, spacing: bool = False) -> str:
        style_pat = re.compile(
            rf'(<w:style [^>]*w:styleId="{style_id}"[^>]*>)(.*?)(</w:style>)',
            re.S,
        )
        m = style_pat.search(xml_text)
        if not m:
            return xml_text
        head, body, tail = m.groups()

        # rFonts + sz dentro de rPr (crea rPr si no existe)
        rpr_pat = re.compile(r"<w:rPr>(.*?)</w:rPr>", re.S)
        rfonts = (f'<w:rFonts w:ascii="{font}" w:hAnsi="{font}" '
                  f'w:eastAsia="{font}" w:cs="{font}"/>')
        sz = f'<w:sz w:val="{size_halfpt}"/><w:szCs w:val="{size_halfpt}"/>'
        bold_tag = "<w:b/><w:bCs/>" if bold else ""
        new_rpr_inner = rfonts + sz + bold_tag
        if rpr_pat.search(body):
            body = rpr_pat.sub(f"<w:rPr>{new_rpr_inner}</w:rPr>", body, count=1)
        else:
            body = body + f"<w:rPr>{new_rpr_inner}</w:rPr>"

        # pPr: interlineado doble y/o centrado
        ppr_extra = ""
        if spacing:
            ppr_extra += f'<w:spacing w:line="{LINE_DOUBLE}" w:lineRule="auto"/>'
        if center:
            ppr_extra += '<w:jc w:val="center"/>'
        if ppr_extra:
            ppr_pat = re.compile(r"<w:pPr>(.*?)</w:pPr>", re.S)
            if ppr_pat.search(body):
                body = ppr_pat.sub(lambda mm: f"<w:pPr>{mm.group(1)}{ppr_extra}</w:pPr>",
                                    body, count=1)
            else:
                body = f"<w:pPr>{ppr_extra}</w:pPr>" + body

        return xml_text[: m.start()] + head + body + tail + xml_text[m.end():]

    xml_text = patch_style(xml_text, "Normal", font=FONT_BODY,
                            size_halfpt=FONT_SIZE_BODY_HALFPT, spacing=True)
    xml_text = patch_style(xml_text, "Title", font=FONT_BODY,
                            size_halfpt="40", bold=True, center=True)
    for hid, sz in (("Heading1", FONT_SIZE_H1_HALFPT), ("Heading2", "26"),
                    ("Heading3", "24")):
        xml_text = patch_style(xml_text, hid, font=FONT_BODY, size_halfpt=sz, bold=True)
    return xml_text


def patch_section_margins(xml_text: str) -> str:
    margins = (
        f'<w:pgMar w:top="{twips(2.5)}" w:right="{twips(2.5)}" '
        f'w:bottom="{twips(2.5)}" w:left="{twips(3)}" w:header="708" '
        f'w:footer="708" w:gutter="0"/>'
    )
    if "<w:pgMar" in xml_text:
        return re.sub(r"<w:pgMar[^/]*/>", margins, xml_text)
    return xml_text.replace("</w:sectPr>", margins + "</w:sectPr>")


def main() -> None:
    if len(sys.argv) != 3:
        print(__doc__)
        raise SystemExit(1)
    src, dst = Path(sys.argv[1]), Path(sys.argv[2])
    shutil.copyfile(src, dst)

    with zipfile.ZipFile(dst, "r") as zin:
        names = zin.namelist()
        contents = {n: zin.read(n) for n in names}

    styles = contents["word/styles.xml"].decode("utf-8")
    styles = patch_styles_xml(styles)
    contents["word/styles.xml"] = styles.encode("utf-8")

    doc = contents["word/document.xml"].decode("utf-8")
    doc = patch_section_margins(doc)
    contents["word/document.xml"] = doc.encode("utf-8")

    with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as zout:
        for name in names:
            zout.writestr(name, contents[name])

    print(f"Plantilla de referencia estilizada: {dst}")


if __name__ == "__main__":
    main()
