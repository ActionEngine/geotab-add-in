# Geotab Downloader
import argparse

from geotab_downloader.client import create_geotab_client
from geotab_downloader.download import download_all


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="geotab_downloader", description="Geotab Data Downloader"
    )
    parser.add_argument("-u", "--username", required=True, help="Geotab username")
    parser.add_argument("-d", "--database", required=True, help="Geotab database name")
    parser.add_argument("-p", "--password", required=True, help="Geotab password")

    args = parser.parse_args()

    api = create_geotab_client(
        username=args.username,
        database=args.database,
        password=args.password,
    )
    download_all(api)
