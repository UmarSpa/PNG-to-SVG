inputdir='./temp/02/'
outputdir='./temp/03/'
if [ ! -e $"$outputdir" ]
then
   mkdir $"$outputdir"
fi

for g in $inputdir*
do
    FILE1=$(basename "${g}")
    FILE1="${FILE1%%.*}"
    echo $"$outputdir$FILE1.svg"
    autotrace -centerline -color-count 2 -output-file $"$outputdir/$FILE1.svg" -output-format SVG $inputdir$(basename "${g}")
done
