#!/usr/bin/env python3
"""Edit a copy of the user's .docx resume in place, keeping its fonts, spacing, and layout.

Usage:
  python edit_resume.py list <resume.docx>
  python edit_resume.py apply <resume.docx> <edits.json> <output.docx>

edits.json is a list of operations, applied in order:
  {"op": "replace", "find": "old text", "with": "new text"}   # change text inside one paragraph
  {"op": "set", "find": "text in paragraph", "to": "whole new paragraph text"}  # rewrite a paragraph (bullets)
  {"op": "insert_after", "find": "text in paragraph", "text": "new paragraph"}  # copy that paragraph's style
  {"op": "delete", "find": "text in paragraph"}
  {"op": "move_after", "find": "paragraph to move", "after": "text in anchor paragraph"}

"find" must match exactly one paragraph. Only the standard library is used.
"""
import json
import re
import shutil
import sys
import zipfile
from xml.sax.saxutils import escape

PARA = re.compile(r"<w:p[ >].*?</w:p>", re.S)
RUN = re.compile(r"<w:r[ >].*?</w:r>", re.S)
TEXT = re.compile(r"<w:t(?: [^>]*)?>(.*?)</w:t>", re.S)
RPR = re.compile(r"<w:rPr>.*?</w:rPr>", re.S)


def unescape(value):
    return value.replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"').replace("&apos;", "'").replace("&amp;", "&")


def para_text(p):
    return "".join(unescape(t) for t in TEXT.findall(p))


def merge_runs(p):
    """Merge neighbouring text runs with identical formatting so text isn't split mid-word."""
    runs = RUN.findall(p)
    merged, prev = [], None
    for r in runs:
        rpr = (RPR.search(r) or [None])[0] if RPR.search(r) else ""
        texts = TEXT.findall(r)
        plain = texts and not re.search(r"<w:(tab|br|drawing|fldChar|instrText)\b", r)
        if plain and prev and prev[0] == rpr:
            prev[1] += "".join(texts)
            continue
        if prev:
            merged.append(prev)
        prev = [rpr, "".join(texts)] if plain else None
        if not plain:
            merged.append(r)
    if prev:
        merged.append(prev)
    if not runs:
        return p
    rebuilt = "".join(m if isinstance(m, str) else f'<w:r>{m[0]}<w:t xml:space="preserve">{m[1]}</w:t></w:r>' for m in merged)
    start = p.index(runs[0])
    end = p.rindex(runs[-1]) + len(runs[-1])
    return p[:start] + rebuilt + p[end:]


def set_text(p, new_text):
    """Replace a paragraph's text with one run that keeps the formatting of its last text run."""
    runs = [r for r in RUN.findall(p) if TEXT.search(r)]
    if not runs:
        raise SystemExit("paragraph has no text to replace")
    rpr = RPR.search(runs[-1])
    run = f'<w:r>{rpr.group(0) if rpr else ""}<w:t xml:space="preserve">{escape(new_text)}</w:t></w:r>'
    start = p.index(runs[0])
    end = p.rindex(runs[-1]) + len(runs[-1])
    return p[:start] + run + p[end:]


def load(path):
    with zipfile.ZipFile(path) as z:
        return z.read("word/document.xml").decode("utf8")


def find_one(paras, needle):
    hits = [i for i, p in enumerate(paras) if needle in para_text(p)]
    if len(hits) != 1:
        raise SystemExit(f"'{needle[:60]}' matched {len(hits)} paragraphs; use a longer, unique phrase")
    return hits[0]


def apply(src, edits_path, out):
    xml = load(src)
    body_start = xml.index("<w:body>") + len("<w:body>")
    head, body = xml[:body_start], xml[body_start:]
    paras = PARA.findall(body)
    gaps = PARA.split(body)  # text between paragraphs (tables, section properties)
    paras = [merge_runs(p) for p in paras]
    for e in json.load(open(edits_path)):
        op = e["op"]
        i = find_one(paras, e["find"])
        if op == "replace":
            p = paras[i]
            new = p.replace(escape(e["find"]), escape(e["with"]), 1)
            if new == p:
                new = set_text(p, para_text(p).replace(e["find"], e["with"], 1))
            paras[i] = new
        elif op == "set":
            paras[i] = set_text(paras[i], e["to"])
        elif op == "insert_after":
            paras.insert(i + 1, set_text(paras[i], e["text"]))
            gaps.insert(i + 1, "")  # the new paragraph takes over whatever followed the anchor
        elif op == "delete":
            del paras[i]
            gaps[i] += gaps.pop(i + 1)
        elif op == "move_after":
            moved = paras.pop(i)
            gaps[i] += gaps.pop(i + 1)
            j = find_one(paras, e["after"])
            paras.insert(j + 1, moved)
            gaps.insert(j + 1, "")
        else:
            raise SystemExit(f"unknown op {op}")
    body = gaps[0] + "".join(p + g for p, g in zip(paras, gaps[1:]))
    shutil.copy(src, out)
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = (head + body).encode("utf8") if item.filename == "word/document.xml" else zin.read(item.filename)
            zout.writestr(item, data)
    print(f"wrote {out}")


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "list":
        xml = load(sys.argv[2])
        for n, p in enumerate(PARA.findall(xml)):
            text = para_text(p)
            if text.strip():
                print(f"{n:3} {text}")
    elif len(sys.argv) == 5 and sys.argv[1] == "apply":
        apply(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print(__doc__)
        sys.exit(1)
