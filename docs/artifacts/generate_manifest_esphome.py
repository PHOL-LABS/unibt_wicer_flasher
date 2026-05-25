#!/usr/bin/env python3

import json
from pathlib import Path

ARTIFACTS_DIR = Path("")
MANIFEST_FILE = ARTIFACTS_DIR / "manifest.json"

HOME_ASSISTANT_DOMAIN = "slim_player"
FUNDING_URL = "https://esphome.io/guides/supporters.html"

with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
    manifest = json.load(f)

for entry in manifest:
    manifest_name = entry["manifest_name"]
    output_file = ARTIFACTS_DIR / manifest_name

    details = entry.get("release_details", {})
    platform = details.get("platform", "Unknown")
    version = details.get("version", "0.0.0")

    parts = []

    for bin_file in entry.get("bin_files", []):
        path = bin_file["artifact_relpath"]

        parts.append({
            "path": path,
            "offset": "0x0"
        })

    esphome_manifest = {
        "name": f"{platform}",
        "version": version,
        "home_assistant_domain": HOME_ASSISTANT_DOMAIN,
        "funding_url": FUNDING_URL,
        "new_install_prompt_erase": True,
        "new_install_improv_wait_time": 20,
        "builds": [
            {
                "chipFamily": "ESP32",
                "parts": parts
            }
        ],
        "manifest_name": manifest_name
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(esphome_manifest, f, indent=4)

    print(f"Generated: {output_file}")