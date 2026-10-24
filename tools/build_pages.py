#!/usr/bin/env python3
"""法律まわりのページ（プライバシーポリシー・特商法・アカウント削除）を組み立てる。

    python3 tools/build_pages.py

原稿は `_src/*.md`（Jekyll は `_` で始まるフォルダを公開しない）。頭の項目で出力先と見出しを決め、
本文を Markdown から HTML にして、TCG-T のページと同じヘッダー・フッターで包む。
Markdown の変換は `marked`（npx で版を固定して呼ぶ）。出力した HTML もコミットする（GitHub Pages はそのまま配る）。

原稿を直したら、このスクリプトを流してから出力を確かめる。HTML を直接直さないこと（次に流すと消える）。
"""
import html
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
MARKED = 'marked@15.0.12'

LABELS = {
    'ja': {
        'skip': '本文へスキップ', 'nav': 'メインナビゲーション', 'guide': '使い方', 'support': 'サポート',
        'updated': '最終更新', 'home': 'AIyabane',
        'foot': [('/', 'AIyabane'), ('/tcg-t/support/', 'お問い合わせ'), ('/privacy/', 'プライバシーポリシー'),
                 ('/tokushoho/', '特定商取引法に基づく表記'), ('/delete-account/', 'アカウントの削除'),
                 ('/tcg-t/updates/', '更新情報')],
    },
    'en': {
        'skip': 'Skip to content', 'nav': 'Main navigation', 'guide': 'Guide (Japanese)', 'support': 'Support',
        'updated': 'Last updated', 'home': 'AIyabane',
        'foot': [('/', 'AIyabane'), ('/tcg-t/support/', 'Contact'), ('/privacy/en/', 'Privacy Policy'),
                 ('/delete-account/en/', 'Delete your account')],
    },
}

TEMPLATE = """<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{title}</title><meta name="description" content="{description}"><link rel="canonical" href="https://aiyabane.com/{path}"><link rel="icon" href="/tcg-t/assets/icon.png"><link rel="stylesheet" href="/tcg-t/assets/site.css"></head>
<body><a class="skip" href="#main">{skip}</a><header class="top"><div class="wrap"><a class="brand" href="/tcg-t/"><img src="/tcg-t/assets/icon.png" width="40" height="40" alt=""><span>TCG-T<small>TCG TRAINING</small></span></a><nav aria-label="{nav}"><a href="/tcg-t/guide/">{guide}</a><a href="/tcg-t/support/">{support}</a></nav></div></header>
<main id="main"><div class="page-head"><div class="wrap"><div class="breadcrumb"><a href="/">{home}</a><span>/</span><a href="/tcg-t/">TCG-T</a><span>/ {heading}</span></div><p class="eyebrow">{eyebrow}</p><h1>{heading}</h1><p class="description">{description}</p><div class="meta">{meta}</div></div></div>
<div class="wrap legal-body"><article class="article">
{body}
</article></div></main>
<footer><div class="wrap"><div><strong>TCG-T / TCG Training</strong><br>© AIyabane</div><div class="foot-links">{foot}</div></div></footer></body></html>
"""


def parse(path: pathlib.Path):
    text = path.read_text(encoding='utf-8')
    m = re.match(r'---\n(.*?)\n---\n(.*)', text, re.S)
    if not m:
        raise SystemExit(f'{path}: 頭の項目（--- で囲んだ部分）が無い')
    meta = dict(re.findall(r'^(\w+):\s*(.*)$', m.group(1), re.M))
    return meta, m.group(2)


def to_html(markdown: str) -> str:
    out = subprocess.run(['npx', '-y', MARKED, '--gfm'], input=markdown, capture_output=True, text=True, check=True)
    body = out.stdout
    # 表は横にはみ出すので、TCG-T と同じ枠で包む
    body = re.sub(r'<table>', '<div class="table-wrap"><table>', body)
    return re.sub(r'</table>', '</table></div>', body)


def build(src: pathlib.Path) -> pathlib.Path:
    meta, markdown = parse(src)
    lang = meta.get('lang', 'ja')
    lab = LABELS[lang]
    meta_parts = []
    if meta.get('updated'):
        meta_parts.append(f"{lab['updated']}: {html.escape(meta['updated'])}")
    if meta.get('alt'):
        meta_parts.append(f'<a href="{html.escape(meta["alt"])}">{html.escape(meta.get("altlabel", ""))}</a>')
    out_path = meta['out']
    page = TEMPLATE.format(
        lang=lang,
        title=html.escape(meta['title']),
        description=html.escape(meta.get('description', '')),
        path=re.sub(r'index\.html$', '', out_path),
        skip=lab['skip'], nav=lab['nav'], guide=lab['guide'], support=lab['support'], home=lab['home'],
        heading=html.escape(meta['heading']),
        eyebrow=html.escape(meta.get('eyebrow', '')),
        meta=' · '.join(meta_parts),
        body=to_html(markdown).strip(),
        foot=''.join(f'<a href="{href}">{html.escape(label)}</a>' for href, label in lab['foot']),
    )
    dest = ROOT / out_path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(page, encoding='utf-8')
    return dest


if __name__ == '__main__':
    for src in sorted((ROOT / '_src').glob('*.md')):
        print(build(src).relative_to(ROOT))
