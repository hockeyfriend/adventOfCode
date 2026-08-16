#!/bin/bash

# day of advent of code
daynumb=$1

if [ -z "$daynumb" ]; then
    echo "Usage: $0 <day_number>"
    exit 1
fi

dayfolder="day$daynumb"
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
template_file="$script_dir/solution_template.py"

# Create folder structure
mkdir -p "$script_dir/$dayfolder/part1" "$script_dir/$dayfolder/part2"

# Create empty puzzle files for both parts
for part in part1 part2; do
    puzzle_file="$script_dir/$dayfolder/$part/puzzle.txt"
    if [ ! -f "$puzzle_file" ]; then
        echo "Create $puzzle_file"
        : > "$puzzle_file"
    else
        echo "File $puzzle_file already exists."
    fi
done

# Create solution.py files from template if they do not already exist
for part in part1 part2; do
    target="$script_dir/$dayfolder/$part/solution.py"
    if [ ! -f "$target" ]; then
        echo "Create $target"
        cp "$template_file" "$target"
    else
        echo "File $target already exists."
    fi
done
