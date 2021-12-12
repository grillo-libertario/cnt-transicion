# Setup

Ubuntu

```bash
sudo apt install pandoc texlive-latex-extra texlive-fonts-extra texlive-lang-spanish ttf-mscorefonts-installer texlive-humanities
```

# Build

```bash
./buildme.sh
```

# To retrieve the chapters from the docx

```
pandoc original.docx --atx-headers -o original.md
./splitchapters.py original.md
```

It will generate

- A numbered folder for each chapter
- A 00 poem with the title and any chapter foreword
- As many numbered files as titled poems it finds


