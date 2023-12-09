#!/bin/bash

# day of advent of code
daynumb=$1

dayfolder=day$daynumb

# Create folder structure
mkdir -p $dayfolder/part1
mkdir -p $dayfolder/part2

# Create blank files
files="$dayfolder/part1/puzzle.txt $dayfolder/part2/puzzle.txt $dayfolder/part1/solution.py $dayfolder/part2/solution.py"

for file in $files 
do
   if [ ! -f $file ]
    then
        echo "Create $file"
        touch $file
    else
        echo "File $file already exists."
    fi
done
