# splitter-joiner

Split files into CD/DVD manageable sizes, and rejoin them when required.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

git clone https://github.com/kyle799/splitters

cd splitter/

## Usage to get into CD size

./splitter.py --file rhel.iso --size .7

# join them back into an iso, we need all file parts and the .sha256 file

./joiner.py -d rhel_transfer_directory/


