#!/bin/sh
# Compile from the course root even when the editor starts in a lecture folder.
set -eu
course_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
lecture_source=$1
build_dir=$2
lecture_dir=$(dirname -- "$lecture_source")
cd "$course_root"
exec latexmk -pdf -synctex=1 -interaction=nonstopmode -file-line-error \
  "-outdir=$build_dir" "-out2dir=$lecture_dir" "$lecture_source"
