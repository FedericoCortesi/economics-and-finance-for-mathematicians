#!/bin/sh
set -eu
cd "$(dirname "$0")"
mkdir -p .build dist
for n in 01 02 03 04 05 06 07; do
  lecture_dir="lectures/lecture_$n"
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory=.build "$lecture_dir/lecture_$n.tex" > ".build/lecture_$n.stdout"
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory=.build "$lecture_dir/lecture_$n.tex" > ".build/lecture_$n.stdout"
  cp ".build/lecture_$n.pdf" "$lecture_dir/lecture_$n.pdf"
done
python3 scripts/combine_pdfs.py
