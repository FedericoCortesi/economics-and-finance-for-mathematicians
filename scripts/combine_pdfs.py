"""Combine the compiled Beamer decks, preserving class and section bookmarks."""
from pathlib import Path
import json
from pypdf import PdfReader, PdfWriter

root=Path(__file__).resolve().parent.parent
outline=json.loads((root/'course_outline.json').read_text())
writer=PdfWriter()
for lecture in outline:
    reader=PdfReader(root/f'lecture_{lecture["number"]:02}.pdf')
    if len(reader.pages)!=lecture['slides']:
        raise ValueError(f'Lecture {lecture["number"]}: PDF and outline page counts differ')
    start=len(writer.pages)
    for page in reader.pages:
        # Beamer navigation annotations target the standalone deck's page tree.
        writer.add_page(page,excluded_keys=('/Annots',))
    parent=writer.add_outline_item(f'{lecture["number"]}. {lecture["title"]}',start)
    previous=None
    for slide in lecture['outline']:
        if slide['section']!=previous:
            writer.add_outline_item(slide['section'],start+slide['page']-1,parent=parent)
            previous=slide['section']
writer.add_metadata({'/Title':'Economics and Finance for Mathematicians',
                     '/Author':'Federico Vittorio Cortesi'})
writer.page_mode='/UseOutlines'
writer.write(root/'economics_and_finance.pdf')
print(f'Combined {len(outline)} lectures into {len(writer.pages)} pages.')
