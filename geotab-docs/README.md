# Geotab Documentation

This directory contains a local copy of the Geotab Developer documentation for offline reference by AI agents and developers.

## Purpose

The documentation in this directory serves as a **local knowledge base** for AI agents (like Kimi Code) to efficiently access Geotab API documentation without:

- Making network requests to https://developers.geotab.com/
- Parsing heavy HTML content
- Dealing with connectivity issues or rate limits

## Format

The documentation is stored in **compressed Markdown format**:

| Metric | Value |
|--------|-------|
| Format | Markdown (`.md`) |
| Files | ~500 files |
| Size | ~4.5 MB (~560 KB compressed) |
| Original | ~35 MB HTML (~9 MB compressed) |
| Compression | **8x smaller** than original HTML |

### Why Markdown?

- **Faster reads**: Plain text is faster to read than HTML
- **Smaller context**: Less token usage when processing with AI
- **Easier search**: Grep and text search work better on clean text
- **Preserved structure**: Headers, lists, tables, and links are maintained

## Directory Structure

```
geotab-docs/
├── README.md                    # This file
├── download-docs.py             # Script to download HTML from Geotab
├── sync-docs.py                 # Script to convert HTML → Markdown
└── developers.geotab.com/       # Compressed documentation
    ├── INDEX.md                 # Quick reference index
    ├── myGeotab/                # MyGeotab API documentation
    │   ├── guides/              # Concepts, getting started
    │   ├── apiReference/
    │   │   ├── objects/         # API objects (Device, Trip, etc.)
    │   │   └── methods/         # API methods (Get, Set, etc.)
│   │   └── addIns/              # Add-in development
    ├── myAdmin/                 # MyAdmin API documentation
    ├── zenith/                  # UI component library
    ├── drive/                   # Geotab Drive SDK
    └── hardware/                # Hardware documentation
```

## Scripts

### `download-docs.py`

Downloads the latest Geotab Developer documentation as HTML from https://developers.geotab.com/.

**Usage:**

```bash
# Download all documentation to a new directory
python geotab-docs/download-docs.py --output geotab-docs-html

# Download specific sections only
python geotab-docs/download-docs.py --sections myGeotab,myAdmin --output geotab-docs-html

# Dry run (show what would be downloaded without downloading)
python geotab-docs/download-docs.py --dry-run
```

**Features:**
- Crawls the Geotab documentation website
- Downloads all HTML pages with proper directory structure
- Respects rate limits (adds delays between requests)
- Skips already-downloaded files (can resume interrupted downloads)

**Requirements:**
```bash
pip install requests beautifulsoup4
```

### `sync-docs.py`

Converts downloaded HTML documentation to compressed Markdown format.

**Usage:**

```bash
# Convert HTML to Markdown (default paths)
python geotab-docs/sync-docs.py

# Specify custom source/output directories
python geotab-docs/sync-docs.py --source ./my-html-docs --output ./my-markdown-docs

# Check if compressed docs are up to date
python geotab-docs/sync-docs.py --check
```

**What it does:**
1. Reads HTML files from source directory
2. Extracts clean text content (removes scripts, styles, navigation)
3. Converts to Markdown with proper formatting
4. Updates internal links (`.html` → `.md`)
5. Writes to output directory

**Features:**
- Preserves document structure (headers, lists, tables)
- Converts internal links for seamless navigation
- Optimizes whitespace for readability
- Maintains directory hierarchy

## Workflow: Updating Documentation

To update the documentation to the latest version from Geotab:

```bash
# Step 1: Download latest HTML documentation
python geotab-docs/download-docs.py --output geotab-docs-html

# Step 2: Convert to compressed Markdown
python geotab-docs/sync-docs.py --source geotab-docs-html/developers.geotab.com

# Step 3: (Optional) Remove HTML source if no longer needed
rm -rf geotab-docs-html
```

## Content Overview

### MyGeotab API (~340 files)

Core fleet management API documentation including:

| Category | Count | Description |
|----------|-------|-------------|
| API Objects | ~300 | Device, Trip, LogRecord, StatusData, Zone, etc. |
| API Methods | ~27 | Get, Set, Add, Remove, ExecuteMultiCall, etc. |
| Guides | ~10 | MultiCall, concepts, URL structures |
| AddIns | ~5 | Add-in development, storage |

**Key objects:**
- `Device` - Vehicle tracking devices
- `LogRecord` - GPS position and speed logs
- `Trip` - Trip summaries
- `StatusData` - Diagnostic data
- `Diagnostic` - Vehicle diagnostics
- `Zone` - Geofenced areas
- `User` - User accounts

### MyAdmin API (~160 files)

Administrative API for managing Geotab accounts and devices.

### Zenith (~5 files)

UI component library documentation for building Geotab add-ins.

### Drive (~1 file)

Geotab Drive SDK documentation.

### Hardware (~2 files)

Hardware device documentation.

## Usage for AI Agents

When working with Geotab-related code, AI agents should:

1. **Prefer local docs**: Read from `geotab-docs/developers.geotab.com/` instead of fetching from the web
2. **Use INDEX.md**: Start with `developers.geotab.com/INDEX.md` for navigation
3. **Follow links**: Internal links use `.md` extension and work locally
4. **Search efficiently**: Use grep/text search on clean Markdown content

### Example Queries

```bash
# Find Device API documentation
cat geotab-docs/developers.geotab.com/myGeotab/apiReference/objects/Device/index.md

# Search for rate limits
grep -r "rate limit" geotab-docs/developers.geotab.com/

# Find Trip-related documentation
find geotab-docs/developers.geotab.com/ -name "*Trip*" -type d
```

## License

This documentation is a mirror of https://developers.geotab.com/ and is subject to Geotab's terms of use. The compression and conversion scripts are part of this project.

## Maintenance

- **Last updated**: 2026-02-24
- **Source**: https://developers.geotab.com/
- **Maintained by**: Project maintainers
- **Update frequency**: As needed when Geotab API changes

---

**Note**: This compressed documentation is optimized for AI agent consumption. For the most up-to-date documentation or interactive features, always refer to https://developers.geotab.com/.
