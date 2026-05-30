#!/usr/bin/env python3

import json
from pathlib import Path

# repo root/docs/artifacts
ARTIFACTS_DIR = Path(".")

# where releases are stored
RELEASES_DIR = ARTIFACTS_DIR / "wic64" / "releases"

manifest = []

for version_dir in sorted(RELEASES_DIR.iterdir()):
    if not version_dir.is_dir():
        continue

    version = version_dir.name

    # recursively find all .bin files
    for bin_file in version_dir.rglob("*.bin"):

        # relative path from docs/artifacts
        rel_path = bin_file.relative_to(ARTIFACTS_DIR).as_posix()

        # firmware name
        firmware_name = bin_file.stem

        # create two platform entries
        for platform in ["Wicer"]:

            entry = {
                "name": f"{platform}.{version}",
                "branch": "main",
                "description": f"WIC64 firmware release {version}",
                "url": rel_path,
                "release_details": {
                    "version": version,
                    "platform": platform,
                    "branch": "main"
                },
                "bin_files": [
                    {
                        "name": bin_file.name,
                        "offset": "0x0",
                        "artifact_relpath": rel_path
                    }
                ],
                "manifest_name": f"manifest-{platform}-{version}.json"
            }

            manifest.append(entry)
            
RELEASES_DIR = ARTIFACTS_DIR / "bluepad" / "releases"

for version_dir in sorted(RELEASES_DIR.iterdir()):
    if not version_dir.is_dir():
        continue

    version = version_dir.name

    # recursively find all .bin files
    for bin_file in version_dir.rglob("*.bin"):

        # relative path from docs/artifacts
        rel_path = bin_file.relative_to(ARTIFACTS_DIR).as_posix()

        # firmware name
        firmware_name = bin_file.stem

        # create two platform entries
        for platform in ["UniBT"]:

            entry = {
                "name": f"{platform}.{version}",
                "branch": "main",
                "description": f"UniBT firmware release {version}",
                "url": rel_path,
                "release_details": {
                    "version": version,
                    "platform": platform,
                    "branch": "main"
                },
                "bin_files": [
                    {
                        "name": bin_file.name,
                        "offset": "0x0",
                        "artifact_relpath": rel_path
                    }
                ],
                "manifest_name": f"manifest-{platform}-{version}.json"
            }

            manifest.append(entry)

# output file
output_file = ARTIFACTS_DIR / "manifest.json"

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=4)

print(f"Generated: {output_file}")
print(f"Entries: {len(manifest)}")