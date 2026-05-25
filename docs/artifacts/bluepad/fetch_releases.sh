OWNER=ricardoquesada
REPO=bluepad32
OUT=releases

mkdir -p "$OUT"

gh release list -R "$OWNER/$REPO" --limit 1000 --json tagName \
  --jq '.[].tagName' |
while read -r tag; do
  mkdir -p "$OUT/$tag"
  gh release download "$tag" \
    -R "$OWNER/$REPO" \
    --dir "$OUT/$tag" \
    --clobber
done
