inputdir='./Src/temp/10/'
outputdir='./Output/'
if [ ! -e $"$outputdir" ]
then
   mkdir $"$outputdir"
fi
for g in $inputdir*
do
    FILE=$(basename "${g}")
    FILE1="${FILE%%.*}"
    #echo $outputdir$FILE1
    convert $g -colorspace Gray -resize 256x256 $outputdir$FILE1".png"
done
