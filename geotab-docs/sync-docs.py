#!/usr/bin/env python3
"""
Sync script for Geotab documentation.

Converts HTML documentation to compressed Markdown format.
This script should be run after updating the HTML documentation.

Usage:
    python sync-docs.py [--source DIR] [--check]

Options:
    --source DIR    Source HTML directory (default: geotab-docs-html)
    --check         Verify compressed docs are up to date

Workflow for updating documentation:
    1. Download new HTML docs to a temporary directory (e.g., geotab-docs-html/)
    2. Run: python geotab-docs/sync-docs.py --source geotab-docs-html
    3. The script will replace the current compressed docs with the new version

The original HTML is kept in geotab-docs-html/ if you need to reference it.
"""

import argparse
import os
import re
import shutil
import sys
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString

# Increase recursion limit for deeply nested HTML
sys.setrecursionlimit(3000)


def clean_text(text):
    """Clean up whitespace in text."""
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
    return text.strip()


def process_element(elem, in_list=False):
    """Recursively process an HTML element and convert to Markdown."""
    if isinstance(elem, NavigableString):
        text = str(elem)
        text = re.sub(r'[ \t\n]+', ' ', text)
        return text

    # Skip these container tags but process their children
    if elem.name in ('tbody', 'thead', 'tfoot'):
        return ''.join(process_element(c, in_list) for c in elem.children)

    # Get text from children
    content = ''
    for child in elem.children:
        content += process_element(child, in_list=(elem.name in ('ul', 'ol')))
    content = content.strip()

    if not content:
        return ''

    # Format based on element type
    if elem.name == 'h1':
        return f"\n# {content}\n\n"
    elif elem.name == 'h2':
        return f"\n## {content}\n\n"
    elif elem.name == 'h3':
        return f"\n### {content}\n\n"
    elif elem.name == 'h4':
        return f"\n#### {content}\n\n"
    elif elem.name == 'h5':
        return f"\n##### {content}\n\n"
    elif elem.name == 'h6':
        return f"\n###### {content}\n\n"
    elif elem.name == 'p':
        return f"{content}\n\n"
    elif elem.name == 'li':
        return f"- {content}\n"
    elif elem.name == 'a':
        href = elem.get('href', '')
        if href and not href.startswith('http'):
            href = href.replace('.html', '.md')
        if href:
            return f"[{content}]({href})"
        return content
    elif elem.name == 'code':
        return f"`{content}`"
    elif elem.name in ('strong', 'b'):
        return f"**{content}**"
    elif elem.name in ('em', 'i'):
        return f"*{content}*"
    elif elem.name == 'pre':
        return f"\n```\n{content}\n```\n\n"
    elif elem.name == 'summary':
        return f"\n**{content}**\n\n"
    elif elem.name in ('ul', 'ol'):
        return f"\n{content}\n"
    elif elem.name == 'tr':
        cells = [c.get_text(strip=True) for c in elem.find_all(['td', 'th'], recursive=False)]
        if cells:
            return '| ' + ' | '.join(cells) + ' |\n'
        return ''
    elif elem.name == 'table':
        rows = []
        for tr in elem.find_all('tr'):
            cells = [c.get_text(strip=True) for c in tr.find_all(['td', 'th'], recursive=False)]
            if cells:
                rows.append('| ' + ' | '.join(cells) + ' |')
        if rows and len(rows) > 0:
            num_cols = len(rows[0].split('|')) - 2
            separator = '|' + '|'.join(' --- ' for _ in range(num_cols)) + '|'
            rows.insert(1, separator)
            return '\n' + '\n'.join(rows) + '\n\n'
        return ''
    elif elem.name == 'details':
        return f"\n{content}\n"
    elif elem.name == 'div':
        if elem.find(['h1', 'h2', 'h3', 'h4', 'p', 'ul', 'ol', 'table']):
            return f"{content}\n\n"
        return content
    else:
        return content


def html_to_markdown(html_path):
    """Convert an HTML file to Markdown."""
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    # Remove unwanted elements
    for tag in soup.find_all(['script', 'style', 'svg', 'nav', 'meta', 'link']):
        tag.decompose()

    # Find main content
    content_div = (
        soup.find('div', class_='pageContent__scrollableArea') or
        soup.find('main') or
        soup.find('article') or
        soup.body
    )

    if not content_div:
        return None

    md_content = process_element(content_div)

    # Post-processing for better formatting
    md_content = re.sub(r'(## \w+)\n([^#\n])', r'\1\n\n\2', md_content)
    md_content = re.sub(r'(- .+)\n([^-\n])', r'\1\n\n\2', md_content)
    md_content = re.sub(r'\n{4,}', '\n\n\n', md_content)
    md_content = re.sub(r'(\)\.?)([A-Z])', r'\1 \2', md_content)

    return md_content.strip()


def convert_docs(source_dir, output_dir):
    """Convert all HTML files in source_dir to Markdown in output_dir."""
    source_path = Path(source_dir)
    output_path = Path(output_dir)

    if not source_path.exists():
        print(f"Error: Source directory '{source_dir}' does not exist")
        return False

    # Clean and create output directory
    if output_path.exists():
        shutil.rmtree(output_path)
    output_path.mkdir(parents=True, exist_ok=True)

    # Copy and update INDEX.md if it exists
    index_src = source_path.parent / "INDEX.md"
    if index_src.exists():
        content = index_src.read_text()
        content = content.replace('.html)', '.md)')
        (output_path.parent / "INDEX.md").write_text(content)

    html_files = list(source_path.rglob("*.html"))
    print(f"Found {len(html_files)} HTML files...")

    converted = 0
    skipped = 0
    for html_file in html_files:
        rel_path = html_file.relative_to(source_path)

        # Skip URL query artifacts from API playground (contain '@')
        # e.g., "index.html@script=..." - these are not real docs
        if '@' in rel_path.name:
            skipped += 1
            continue

        md_file = output_path / rel_path.with_suffix('.md')
        md_file.parent.mkdir(parents=True, exist_ok=True)

        content = html_to_markdown(html_file)
        if content:
            md_file.write_text(content, encoding='utf-8')
            converted += 1

    if skipped > 0:
        print(f"⚠️  Skipped {skipped} URL artifact files (containing '@')")

    print(f"✅ Converted {converted}/{len(html_files)} files")
    return True


def check_compression(source_dir, output_dir):
    """Check if the compressed docs are up to date."""
    source_path = Path(source_dir)
    output_path = Path(output_dir)

    if not output_path.exists():
        print("❌ Compressed docs do not exist")
        return False

    source_files = list(source_path.rglob("*.html"))
    output_files = list(output_path.rglob("*.md"))

    if len(source_files) != len(output_files):
        print(f"❌ File count mismatch: {len(source_files)} HTML vs {len(output_files)} MD")
        return False

    # Check modification times
    source_mtime = max(f.stat().st_mtime for f in source_files)
    output_mtime = min(f.stat().st_mtime for f in output_files)

    if source_mtime > output_mtime:
        print("❌ Source files are newer than compressed docs")
        return False

    print("✅ Compressed docs are up to date")
    return True


def main():
    parser = argparse.ArgumentParser(
        description='Sync Geotab documentation from HTML to compressed Markdown'
    )
    parser.add_argument(
        '--source',
        default='geotab-docs-html/developers.geotab.com',
        help='Source HTML directory (default: geotab-docs-html/developers.geotab.com)'
    )
    parser.add_argument(
        '--output',
        default='geotab-docs/developers.geotab.com',
        help='Output Markdown directory (default: geotab-docs/developers.geotab.com)'
    )
    parser.add_argument(
        '--check',
        action='store_true',
        help='Check if compressed docs are up to date'
    )

    args = parser.parse_args()

    if args.check:
        return 0 if check_compression(args.source, args.output) else 1

    success = convert_docs(args.source, args.output)
    if success:
        # Print size comparison
        import subprocess
        result = subprocess.run(
            ['du', '-sh', str(Path(args.source).parent), str(Path(args.output).parent)],
            capture_output=True, text=True
        )
        print("\nSize comparison:")
        print(result.stdout)

    return 0 if success else 1


if __name__ == '__main__':
    sys.exit(main())
