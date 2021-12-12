#!/usr/bin/env python3

from pathlib import Path
import re
from slugify import slugify

original = Path('CNT-y-transicion.md').read_text(encoding='utf8')

parts = re.findall(r'^# .*?(?=^# |\Z)', original, re.DOTALL|re.MULTILINE)

for partnumber, part in enumerate(parts):
	parttitle, partcontent = part.split('\n', 1)

	print(f"{parttitle}")

	partfolder = Path(f"{partnumber:02d}-{slugify(parttitle)}")
	partfolder.mkdir(exist_ok=True)
	chapters = re.split(r"^## ", partcontent, 0, re.MULTILINE)

	(partfolder / f"00-{slugify(parttitle)}.md").write_text(
		f"{parttitle}\n" + chapters[0],
		encoding='utf8',
	)
	for chapternumber, chapter in enumerate(chapters[1:],1):
		chaptertitle, chaptercontent = chapter.split('\n', 1)
		print(f"## {chaptertitle}")
		chapterlines = []
		chapterfile = partfolder/f"{chapternumber:02d}-{slugify(chaptertitle)}.md"
		chapterfile.write_text(
			f"## {chapter}{chaptercontent}",
			encoding='utf8',
		)
	




