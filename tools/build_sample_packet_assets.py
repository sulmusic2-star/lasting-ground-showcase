#!/usr/bin/env python3
"""Build shareable Lasting Ground sample packet assets.

This script creates a fake-data printable PDF-style sample packet and a cover preview image with neutral claim language and no real address records.
"""
from __future__ import annotations
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import textwrap

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "assets"
OUT.mkdir(parents=True, exist_ok=True)
PDF_PATH = OUT / "lasting-ground-sample-packet.pdf"
COVER_PATH = OUT / "lasting-ground-sample-packet-cover.png"
HTML_PATH = OUT / "lasting-ground-sample-packet.html"

W, H = 612, 792


def _font(size: int, bold: bool = False):
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
    ]
    for p in candidates:
        if Path(p).exists():
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


class MiniPDF:
    def __init__(self):
        # Reserve catalog, pages, and two standard fonts at stable IDs 1-4.
        self.objects: list[bytes | None] = [None, None, None, None]
        self.pages: list[int] = []

    def add_obj(self, data: str) -> int:
        self.objects.append(data.encode("latin-1"))
        return len(self.objects)

    @staticmethod
    def esc(text: str) -> str:
        return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")

    def add_page(self, commands: list[str]) -> None:
        stream = "\n".join(commands)
        content_id = self.add_obj(f"<< /Length {len(stream.encode('latin-1'))} >>\nstream\n{stream}\nendstream")
        page_id = self.add_obj(f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {W} {H}] /Resources << /Font << /F1 3 0 R /F2 4 0 R >> >> /Contents {content_id} 0 R >>")
        self.pages.append(page_id)

    def write(self, path: Path) -> None:
        page_refs = " ".join(f"{p} 0 R" for p in self.pages)
        self.objects[0] = b"<< /Type /Catalog /Pages 2 0 R >>"
        self.objects[1] = f"<< /Type /Pages /Kids [{page_refs}] /Count {len(self.pages)} >>".encode("latin-1")
        self.objects[2] = b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>"
        self.objects[3] = b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>"
        out = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
        offsets = []
        for i, obj in enumerate(self.objects, 1):
            assert obj is not None
            offsets.append(len(out))
            out.extend(f"{i} 0 obj\n".encode("latin-1"))
            out.extend(obj)
            out.extend(b"\nendobj\n")
        xref = len(out)
        out.extend(f"xref\n0 {len(self.objects)+1}\n0000000000 65535 f \n".encode("latin-1"))
        for off in offsets:
            out.extend(f"{off:010d} 00000 n \n".encode("latin-1"))
        out.extend(f"trailer << /Size {len(self.objects)+1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode("latin-1"))
        path.write_bytes(out)


def rgb(r, g, b):
    return f"{r/255:.3f} {g/255:.3f} {b/255:.3f} rg"


def stroke(r, g, b):
    return f"{r/255:.3f} {g/255:.3f} {b/255:.3f} RG"


def text(cmds, x, y, s, size=11, bold=False, color=(20, 32, 48)):
    font = "F2" if bold else "F1"
    cmds.append(rgb(*color))
    cmds.append(f"BT /{font} {size} Tf {x} {y} Td ({MiniPDF.esc(s)}) Tj ET")


def rect(cmds, x, y, w, h, fill=(255, 255, 255), line=(225, 232, 240)):
    cmds.append(rgb(*fill)); cmds.append(stroke(*line)); cmds.append(f"{x} {y} {w} {h} re B")


def wrap_lines(s: str, width: int = 74):
    lines = []
    for para in s.split("\n"):
        if not para.strip():
            lines.append("")
        else:
            lines.extend(textwrap.wrap(para, width=width))
    return lines


def header(cmds, page_title="Lasting Ground"):
    cmds.append(rgb(248, 250, 252)); cmds.append(f"0 0 {W} {H} re f")
    cmds.append(rgb(7, 17, 31)); cmds.append(f"0 {H-86} {W} 86 re f")
    text(cmds, 40, H-40, page_title, 20, True, (255,255,255))
    text(cmds, 40, H-62, "Sample source-backed review packet - fictional data", 10, False, (209,213,219))
    text(cmds, 40, 28, "Public showcase sample. Not legal, engineering, inspection, or permitting advice.", 8, False, (100,116,139))


def page_cover(pdf: MiniPDF):
    c=[]; header(c)
    text(c, 40, 646, "42 Harbor View Road", 30, True, (15,23,42))
    for i,line in enumerate(wrap_lines("This fake packet demonstrates the artifact shape, source appendix, and validation posture of a source-backed property review system without using any real address.", 70)):
        text(c, 40, 610-i*15, line, 11, False, (51,65,85))
    rect(c, 40, 430, 250, 90, (255,251,235), (251,191,36))
    text(c, 60, 488, "FICTIONAL SAMPLE", 16, True, (146,64,14))
    text(c, 60, 462, "SOURCE-BACKED", 16, True, (146,64,14))
    rect(c, 322, 430, 250, 90, (236,253,245), (34,197,94))
    text(c, 342, 488, "Packet purpose", 14, True, (21,128,61))
    for i,line in enumerate(wrap_lines("Translate fragmented public and official context into a reviewable, homeowner-readable packet while preserving uncertainty and source boundaries.", 36)):
        text(c,342,466-i*13,line,9,False,(22,101,52))
    text(c,40,366,"What this sample shows",18,True,(15,23,42))
    items=["source lane summary","support-depth caution","validation gate","plain-English findings","source appendix with claim boundaries"]
    for i,it in enumerate(items):
        text(c,60,334-i*22,f"- {it}",12,False,(51,65,85))
    rect(c,40,132,532,92,(239,246,255),(96,165,250))
    text(c,60,196,"Sample support depth",14,True,(30,64,175))
    for i,line in enumerate(wrap_lines("Publish with caution: several source lanes are validated, but permit-history evidence is incomplete in this fictional sample. Public wording should disclose the missing lane rather than imply certainty.", 76)):
        text(c,60,172-i*13,line,9,False,(30,64,175))
    pdf.add_page(c)


def page_lanes(pdf: MiniPDF):
    c=[]; header(c)
    text(c,40,670,"1. Source Lane Summary",22,True,(15,23,42))
    for i,line in enumerate(wrap_lines("A source lane is a category of evidence. The system should track what each lane supports and what it does not support.",74)):
        text(c,40,642-i*14,line,10,False,(51,65,85))
    rows=[("State GIS Context","VALIDATED","Broad regional screening context."),("Town Zoning Reference","VALIDATED","Local routing/reference context."),("Conservation Record Lane","CAUTION","Public lane incomplete; disclose uncertainty."),("Flood Context","VALIDATED","Regional flood-context layer available."),("Permit History Packet","MISSING","No complete local packet in this fictional sample.")]
    y=570
    for name,status,desc in rows:
        fill=(236,253,245) if status=="VALIDATED" else (255,251,235) if status=="CAUTION" else (254,242,242)
        rect(c,40,y,532,52,fill,(226,232,240))
        text(c,58,y+30,name,12,True,(15,23,42))
        text(c,360,y+30,status,11,True,(21,128,61) if status=="VALIDATED" else (146,64,14) if status=="CAUTION" else (185,28,28))
        text(c,58,y+12,desc,9,False,(71,85,105))
        y-=64
    pdf.add_page(c)


def page_findings(pdf: MiniPDF):
    c=[]; header(c)
    text(c,40,670,"2. Plain-English Findings",22,True,(15,23,42))
    findings=[("What the packet found","Regional and local source context exists for this fictional address."),("What needs caution","One local record lane is incomplete, so a property-specific conclusion is not supported."),("What the reader should understand","This packet provides context and source direction, not legal, permit, engineering, or inspection advice."),("What happens next","A stronger packet would require a verified local permit/history lane or an explicit no-record result from a public source.")]
    y=610
    for head,body in findings:
        text(c,40,y,head,14,True,(15,23,42)); y-=20
        for line in wrap_lines(body,78):
            text(c,60,y,line,11,False,(51,65,85)); y-=15
        y-=16
    pdf.add_page(c)


def page_gate(pdf: MiniPDF):
    c=[]; header(c)
    text(c,40,670,"3. Validation Gate",22,True,(15,23,42))
    checks=[("PASS","Source present","Every key claim has a named source."),("PASS","Scope boundary","Context cannot become legal/engineering advice."),("PASS","Freshness visible","Reviewed dates and stale-source warnings are visible."),("CAUTION","Local support","Local claims require local source support."),("PASS","Missing evidence disclosed","Incomplete lanes are shown, not hidden.")]
    y=610
    for status,head,body in checks:
        col=(21,128,61) if status=="PASS" else (146,64,14)
        text(c,50,y,status,10,True,col)
        text(c,128,y,head,13,True,(15,23,42))
        text(c,128,y-17,body,10,False,(51,65,85))
        y-=56
    rect(c,40,150,532,86,(239,246,255),(96,165,250))
    text(c,60,210,"Gate outcome",14,True,(30,64,175))
    for i,line in enumerate(wrap_lines("Publish with caution. Public wording may describe the source context found, but should not imply a property-specific approval, violation, or engineering conclusion.",76)):
        text(c,60,188-i*13,line,9,False,(30,64,175))
    pdf.add_page(c)


def page_sources(pdf: MiniPDF):
    c=[]; header(c)
    text(c,40,670,"4. Sample Source Appendix",22,True,(15,23,42))
    for i,line in enumerate(wrap_lines("A useful packet should show source provenance and claim boundaries in plain English.",74)):
        text(c,40,642-i*14,line,10,False,(51,65,85))
    rows=[("sample_state_gis","regional_context","Supports broad screening context; does not support parcel-specific legal conclusion."),("sample_town_zoning","local_reference","Supports local routing context; does not predict approval."),("sample_conservation_records","public_records","Supports review-history direction; incomplete in this sample."),("sample_flood_context","regional_layer","Supports flood-context screening; does not provide engineering design advice.")]
    y=570
    for source,lane,boundary in rows:
        rect(c,40,y,532,58,(255,255,255),(226,232,240))
        text(c,58,y+34,source,12,True,(15,23,42))
        text(c,58,y+16,lane,9,False,(100,116,139))
        for i,line in enumerate(wrap_lines(boundary,48)):
            text(c,282,y+34-i*13,line,9,False,(51,65,85))
        y-=70
    pdf.add_page(c)


def build_pdf():
    pdf=MiniPDF()
    page_cover(pdf); page_lanes(pdf); page_findings(pdf); page_gate(pdf); page_sources(pdf)
    pdf.write(PDF_PATH)


def build_cover():
    im=Image.new("RGB",(1200,1553),"#f8fafc")
    d=ImageDraw.Draw(im)
    d.rectangle((0,0,1200,190),fill="#07111f")
    d.text((72,62),"Lasting Ground",font=_font(54,True),fill="white")
    d.text((72,124),"Sample source-backed review packet - fictional data",font=_font(24),fill="#cbd5e1")
    d.text((72,280),"42 Harbor View Road",font=_font(66,True),fill="#0f172a")
    d.text((72,365),"FICTIONAL SAMPLE",font=_font(30,True),fill="#92400e")
    d.rounded_rectangle((72,480,1128,720),radius=32,fill="#eff6ff",outline="#93c5fd",width=3)
    d.text((112,525),"Sample support depth",font=_font(32,True),fill="#1e40af")
    lines=wrap_lines("Publish with caution: several source lanes are validated, but permit-history evidence is incomplete in this fictional sample.",52)
    y=582
    for line in lines:
        d.text((112,y),line,font=_font(26),fill="#1e3a8a"); y+=34
    d.text((72,820),"What the packet demonstrates",font=_font(38,True),fill="#0f172a")
    items=["Source lane summary","Validation gate","Plain-English findings","Source appendix","Explicit claim boundaries"]
    y=900
    for item in items:
        d.text((110,y),f"- {item}",font=_font(31),fill="#334155"); y+=54
    d.rectangle((72,1350,1128,1352),fill="#cbd5e1")
    d.text((72,1392),"Public showcase sample. Not legal, engineering, inspection, or permitting advice.",font=_font(22),fill="#64748b")
    im.save(COVER_PATH,quality=94)


def build_html():
    HTML_PATH.write_text("""<!doctype html><meta charset='utf-8'><title>Lasting Ground Sample Packet</title><body style='font-family:system-ui;margin:40px;max-width:900px'><h1>Lasting Ground sample packet</h1><p>Fake-data sample artifact source. Open the PDF from the live demo.</p><p><a href='lasting-ground-sample-packet.pdf'>PDF</a></p><p><a href='lasting-ground-sample-packet-cover.png'>Cover preview</a></p></body>\n""")


def main():
    build_pdf(); build_cover(); build_html()
    print(PDF_PATH)
    print(COVER_PATH)

if __name__ == "__main__":
    main()
