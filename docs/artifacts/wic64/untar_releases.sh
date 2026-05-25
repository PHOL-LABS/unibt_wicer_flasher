#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="${1:-releases}"

find "$ROOT_DIR" -type f \( \
    -name "*.tar.gz" -o \
    -name "*.tgz" \
\) | while read -r archive; do

    base="$(basename "$archive")"
    dir="$(dirname "$archive")"

    extract_dir="$dir/${base%.tar.gz}"
    extract_dir="${extract_dir%.tgz}"

    echo "Extracting:"
    echo "  Archive: $archive"
    echo "  Target : $extract_dir"

    mkdir -p "$extract_dir"

    tar -xzf "$archive" -C "$extract_dir"
done

echo "Done."
