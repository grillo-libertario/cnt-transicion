for ext in jpg jpeg; do
for a in images/*$ext; do
echo $a;
convert $a -set colorspace Gray -separate -average ${a/\.$ext/-byn.$ext};
done
done
