# Setup

Ubuntu

```bash
sudo apt install pandoc texlive-latex-extra texlive-fonts-extra texlive-lang-spanish ttf-mscorefonts-installer texlive-humanities
```

# Build

```bash
./buildme.sh
```

# To retrieve the poems from the docx

```
pandoc original.docx -o original.md
./split_poems.sh original.md
```

The script suposes some structure we found:

- Every chapter is enclosed by `[]`
- Every poem has a `------` before the title

It will generate

- A numbered folder for each chapter
- A 00 poem with the title and any chapter foreword
- As many numbered files as titled poems it finds


