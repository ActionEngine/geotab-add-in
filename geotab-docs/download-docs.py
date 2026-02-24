#!/usr/bin/env python3
"""
Download Geotab Developer documentation as HTML.

This script crawls https://developers.geotab.com/ and downloads all documentation
pages for offline use. The downloaded HTML can then be converted to Markdown
using sync-docs.py.

Usage:
    python download-docs.py [--output DIR] [--sections SECTIONS] [--dry-run]

Options:
    --output DIR        Output directory (default: geotab-docs-html)
    --sections LIST     Comma-separated list of sections to download
                        (default: all sections)
    --delay SECONDS     Delay between requests (default: 0.5)
    --retry COUNT       Retry attempts for failed requests (default: 3)
    --dry-run           Show what would be downloaded without downloading

Examples:
    # Download all documentation
    python download-docs.py

    # Download only MyGeotab documentation
    python download-docs.py --sections myGeotab

    # Download MyGeotab and MyAdmin
    python download-docs.py --sections myGeotab,myAdmin --output ./my-docs

    # Dry run to see what would be downloaded
    python download-docs.py --dry-run
"""

import argparse
import os
import sys
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Error: Required packages not installed.")
    print("Run: pip install requests beautifulsoup4")
    sys.exit(1)

BASE_URL = "https://developers.geotab.com"

# Default sections to crawl
DEFAULT_SECTIONS = [
    "myGeotab",
    "myAdmin",
    "zenith",
    "drive",
    "hardware",
    "ai",
]

# URL patterns to exclude
EXCLUDE_PATTERNS = [
    "/apiReference/objects",  # Will be handled separately with pagination
    ".pdf",
    ".zip",
    ".tar.gz",
    "?",
    "#",
]

# Known API object paths for MyGeotab (common ones)
MYGEOTAB_API_OBJECTS = [
    # Core entities
    "Device", "LogRecord", "Trip", "StatusData", "Diagnostic",
    "Zone", "User", "Group", "Rule", "ExceptionEvent",
    # Location/GPS
    "Coordinate", "Address", "Location", "Route",
    # Diagnostics
    "DiagnosticType", "Source", "FaultData", "FailureMode",
    # Vehicles/Drivers
    "Driver", "DriverChange", "DutyStatusLog",
    # Zones
    "ZoneType", "ZoneStop",
    # AddIns
    "AddIn", "AddInConfiguration",
    # Common
    "Entity", "Id", "NameEntity", "Search",
]

# Known API methods
MYGEOTAB_API_METHODS = [
    "Get", "Set", "Add", "Remove", "GetCountOf",
    "GetFeed", "ExecuteMultiCall", "GetVersion",
]

# Known MyAdmin API objects
MYADMIN_API_OBJECTS = [
    "ApiUser", "ApiDevice", "ApiAccount", "ApiOrder",
    "ThirdPartyLogRecord", "ThirdPartyStatusRecord",
]


class GeotabDocDownloader:
    """Downloader for Geotab Developer documentation."""

    def __init__(self, output_dir, delay=0.5, retry=3, dry_run=False):
        self.output_dir = Path(output_dir)
        self.delay = delay
        self.retry = retry
        self.dry_run = dry_run
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.0"
        })
        self.downloaded = set()
        self.failed = []

    def url_to_path(self, url):
        """Convert URL to local file path."""
        parsed = urlparse(url)
        path = parsed.path.lstrip("/")
        
        # Handle root index
        if not path or path == "/":
            path = "index.html"
        
        # Ensure .html extension for paths ending in /
        if path.endswith("/"):
            path += "index.html"
        
        # Add .html if no extension
        if "." not in Path(path).name:
            path += "/index.html"
        
        return self.output_dir / path

    def should_download(self, url):
        """Check if URL should be downloaded."""
        # Must be from developers.geotab.com
        if "developers.geotab.com" not in url:
            return False
        
        # Exclude patterns
        for pattern in EXCLUDE_PATTERNS:
            if pattern in url:
                return False
        
        # Skip if already downloaded
        if url in self.downloaded:
            return False
        
        return True

    def download_page(self, url):
        """Download a single page."""
        if not self.should_download(url):
            return None

        self.downloaded.add(url)
        
        if self.dry_run:
            print(f"[DRY-RUN] Would download: {url}")
            return None

        # Try downloading with retries
        for attempt in range(self.retry):
            try:
                print(f"Downloading: {url}")
                response = self.session.get(url, timeout=30)
                response.raise_for_status()
                
                # Save to file
                file_path = self.url_to_path(url)
                file_path.parent.mkdir(parents=True, exist_ok=True)
                file_path.write_text(response.text, encoding="utf-8")
                
                # Rate limiting
                time.sleep(self.delay)
                
                return response.text
                
            except requests.RequestException as e:
                print(f"  Attempt {attempt + 1}/{self.retry} failed: {e}")
                if attempt < self.retry - 1:
                    time.sleep(self.delay * 2)
                else:
                    self.failed.append((url, str(e)))
                    return None

    def extract_links(self, html, base_url):
        """Extract links from HTML."""
        if not html:
            return []
        
        soup = BeautifulSoup(html, "html.parser")
        links = []
        
        for a in soup.find_all("a", href=True):
            href = a["href"]
            full_url = urljoin(base_url, href)
            
            # Normalize URL
            full_url = full_url.split("#")[0]  # Remove fragments
            full_url = full_url.split("?")[0]  # Remove query params
            
            if self.should_download(full_url):
                links.append(full_url)
        
        return links

    def crawl_section(self, section):
        """Crawl a documentation section."""
        start_url = f"{BASE_URL}/{section}/introduction/"
        if section == "myGeotab":
            start_url = f"{BASE_URL}/myGeotab/introduction/"
        
        print(f"\n{'='*60}")
        print(f"Crawling section: {section}")
        print(f"{'='*60}")
        
        to_crawl = [start_url]
        crawled = set()
        
        while to_crawl:
            url = to_crawl.pop(0)
            
            if url in crawled:
                continue
            
            crawled.add(url)
            html = self.download_page(url)
            
            if html:
                links = self.extract_links(html, url)
                # Only follow links within the same section
                section_links = [
                    l for l in links 
                    if f"/{section}/" in l and l not in crawled
                ]
                to_crawl.extend(section_links)

    def download_known_api_pages(self):
        """Download known API object and method pages."""
        print(f"\n{'='*60}")
        print("Downloading known API objects and methods")
        print(f"{'='*60}")
        
        # MyGeotab API objects
        for obj in MYGEOTAB_API_OBJECTS:
            url = f"{BASE_URL}/myGeotab/apiReference/objects/{obj}/"
            self.download_page(url)
        
        # MyGeotab API methods
        for method in MYGEOTAB_API_METHODS:
            url = f"{BASE_URL}/myGeotab/apiReference/methods/{method}/"
            self.download_page(url)
        
        # MyAdmin API objects
        for obj in MYADMIN_API_OBJECTS:
            url = f"{BASE_URL}/myAdmin/apiReference/objects/{obj}/"
            self.download_page(url)

    def download(self, sections=None):
        """Download all documentation."""
        if sections is None:
            sections = DEFAULT_SECTIONS
        
        print(f"Output directory: {self.output_dir}")
        print(f"Sections: {', '.join(sections)}")
        print(f"Delay: {self.delay}s, Retries: {self.retry}")
        
        if self.dry_run:
            print("\n*** DRY RUN MODE - No files will be downloaded ***\n")
        
        # Create output directory
        if not self.dry_run:
            self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Download main page
        self.download_page(BASE_URL + "/")
        
        # Crawl each section
        for section in sections:
            self.crawl_section(section)
        
        # Download known API pages (in case crawling missed them)
        self.download_known_api_pages()
        
        # Summary
        print(f"\n{'='*60}")
        print("Download Summary")
        print(f"{'='*60}")
        print(f"Total URLs processed: {len(self.downloaded)}")
        print(f"Failed downloads: {len(self.failed)}")
        
        if self.failed:
            print("\nFailed URLs:")
            for url, error in self.failed:
                print(f"  - {url}: {error}")
        
        if not self.dry_run:
            # Create INDEX.md
            self.create_index()

    def create_index(self):
        """Create INDEX.md for the downloaded documentation."""
        index_path = self.output_dir / "INDEX.md"
        
        content = f"""# Geotab Documentation Index

Downloaded from: https://developers.geotab.com/
Date: {time.strftime("%Y-%m-%d")}
Total Pages: {len(self.downloaded)}

## Structure

### MyGeotab
- **Introduction**: `myGeotab/introduction/`
- **Guides**: 
  - `myGeotab/guides/concepts/` - Core concepts (MultiCall, etc.)
  - `myGeotab/guides/myGeotabUrls/` - URL structures
- **API Reference**:
  - `myGeotab/apiReference/objects/` - API objects (Device, LogRecord, Trip, etc.)
  - `myGeotab/apiReference/methods/` - API methods (Get, Set, Add, Remove, etc.)
- **AddIns**:
  - `myGeotab/addIns/developingAddIns/` - Add-in development guide
  - `myGeotab/addIns/addInStorage/` - Add-in storage
- **Code Samples**: `myGeotab/codeSamples/`

### MyAdmin
- `myAdmin/introduction/`
- `myAdmin/guides/` - Concepts, getting started, code bases
- `myAdmin/apiReference/` - API objects and methods
- `myAdmin/codeSamples/` - .NET and JavaScript examples

### Zenith
- `zenith/introduction/` - UI component library

### Drive
- `drive/introduction/` - Geotab Drive SDK

### Hardware
- `hardware/introduction/`

### AI
- `ai/introduction/` - Geotab AI documentation

## Quick Access

### Key MyGeotab API Objects
- Device: `myGeotab/apiReference/objects/Device/index.html`
- LogRecord: `myGeotab/apiReference/objects/LogRecord/index.html`
- Trip: `myGeotab/apiReference/objects/Trip/index.html`
- StatusData: `myGeotab/apiReference/objects/StatusData/index.html`
- Diagnostic: `myGeotab/apiReference/objects/Diagnostic/index.html`
- User: `myGeotab/apiReference/objects/User/index.html`
- Zone: `myGeotab/apiReference/objects/Zone/index.html`

### Key API Methods
- Get: `myGeotab/apiReference/methods/Get/index.html`
- Set: `myGeotab/apiReference/methods/Set/index.html`
- Add: `myGeotab/apiReference/methods/Add/index.html`
- Remove: `myGeotab/apiReference/methods/Remove/index.html`
- ExecuteMultiCall: `myGeotab/apiReference/methods/ExecuteMultiCall/index.html`

### Add-in Development
- Developing AddIns: `myGeotab/addIns/developingAddIns/index.html`
- AddIn Storage: `myGeotab/addIns/addInStorage/index.html`
"""
        
        index_path.write_text(content, encoding="utf-8")
        print(f"\nCreated index: {index_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Download Geotab Developer documentation as HTML"
    )
    parser.add_argument(
        "--output",
        default="geotab-docs-html",
        help="Output directory (default: geotab-docs-html)"
    )
    parser.add_argument(
        "--sections",
        default=None,
        help="Comma-separated list of sections to download (default: all)"
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.5,
        help="Delay between requests in seconds (default: 0.5)"
    )
    parser.add_argument(
        "--retry",
        type=int,
        default=3,
        help="Retry attempts for failed requests (default: 3)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be downloaded without downloading"
    )

    args = parser.parse_args()

    sections = None
    if args.sections:
        sections = [s.strip() for s in args.sections.split(",")]

    downloader = GeotabDocDownloader(
        output_dir=args.output,
        delay=args.delay,
        retry=args.retry,
        dry_run=args.dry_run
    )
    
    downloader.download(sections=sections)


if __name__ == "__main__":
    main()
