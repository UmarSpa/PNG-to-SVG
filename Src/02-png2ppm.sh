inputdir='./temp/01/'
outputdir='./temp/02/'
if [ ! -e $"$outputdir" ]
then
   mkdir $"$outputdir"
fi

for g in $inputdir*
do
    FILE1=$(basename "${g}")
    FILE1="${FILE1%%.*}"
    echo $"$outputdir$FILE1.ppm"
    convert $inputdir$(basename "${g}") $"$outputdir/$FILE1.ppm"
done
