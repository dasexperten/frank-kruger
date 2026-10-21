#!/usr/bin/env python3
"""Reproduce text derivatives. DOCX: stdlib; PDF: Poppler pdftotext required."""
from pathlib import Path
import hashlib
import json
import subprocess
import textwrap
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'research/dissertation'
NAMES = {
    'article-plan.docx': 'Шаблон плана научной статьи.docx',
    'article-structure.docx': 'Структура научной статьи.docx',
    'article-example.pdf': 'Образец статьи.pdf',
    'article-writing.docx': 'Как написать научную статью по гуманитарным наукам.docx',
    'academic-writing.pdf': 'Короткина-И.Б.-Академическое-письмо.pdf',
    'dissertation-concept-2026-09-07.docx': 'концепция диссертации_НОВАЯ_07.09.26.docx',
}

def main():
    out = BASE / 'sources'
    out.mkdir(parents=True, exist_ok=True)
    manifest = []
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    for name, original in NAMES.items():
        p = BASE / 'originals' / name
        target = out / (p.stem + '.txt')
        if p.suffix == '.docx':
            blocks = []
            with zipfile.ZipFile(p) as z:
                for part in ('word/document.xml', 'word/footnotes.xml', 'word/endnotes.xml'):
                    if part not in z.namelist():
                        continue
                    blocks.append('## OOXML part: ' + part)
                    root = ET.fromstring(z.read(part))
                    for i, para in enumerate(root.findall('.//w:p', ns), 1):
                        text = ''.join(t.text or '' for t in para.iter() if t.tag.endswith('}t'))
                        if text.strip():
                            blocks.append(f'[paragraph {i}] ' + text)
            text = '\n\n'.join('\n'.join(textwrap.wrap(b, width=140, replace_whitespace=False)) for b in blocks)
            target.write_text(text + '\n', encoding='utf-8')
        else:
            subprocess.run(['pdftotext', '-layout', str(p), str(target)], check=True)
        manifest.append({'original_filename': original, 'original': p.relative_to(ROOT).as_posix(),
                         'text': target.relative_to(ROOT).as_posix(),
                         'bytes': p.stat().st_size,
                         'sha256': hashlib.sha256(p.read_bytes()).hexdigest(),
                         'text_sha256': hashlib.sha256(target.read_bytes()).hexdigest()})
    (BASE / 'manifest.json').write_text(json.dumps({'source': 'Lyudmila email package 2026-10-21; forwarded guidance 2026-10-18',
        'limitations': 'Text derivatives flatten tables and may omit drawing text, equations or tracked changes. Check original before numerical or quotation use. No scientific claims independently verified.',
        'files': manifest}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

if __name__ == '__main__':
    main()
