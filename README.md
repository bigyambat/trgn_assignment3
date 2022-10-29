# trgn_assignment3
TRGN510 Assignment 3 Fall 2022

# Extract Phone Number Task 
## Usage
Input a txt file with phone numbers and the program will return the phone numbers only 
## Description
Input a txt file with phone numbers and the program will return the phone numbers only
## Known Issues

Works for regular numbers with 888-888-8888 pattern. Does not work for international numbers. 

Found a solution that requires Hard-Wiring. 

Issue: The solution prints the numbers, but the formatting is slightly incorrect. Additionally, international numbers do not get formatted properly. 

# Ensg2Hugo

## Usage

To convernt ENSG to Hugo, we need a file for data. We can use the following gtf file: Homo_sapiens.GRCh37.75.gtf. Using the following wget command to scrape the file off the internet. Then use the gunzip commmand to unzip the file. 

``` python

wget http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf.gz 
gunzip Homo_sapiens.GRCh37.75.gtf.gz 

#Note that curl does not work properly since the file is too large. wget is a better option. 

```

This script works with the following command in bash:

``` bash
python3 ensg2hugo.py [-f][0-9] [file]
```

## Description
Function that Converts Ensemble names in a GTF file to HUGO names for specific columns of a file. 

## Known Issues
There are no known issues with this code. This script works as expected. 

# Histogram

## Usage 
Takes csv file and makes a histogram as a png. When asked, insert the column of the CSV that you want to make a histogram. 

This script works with the following command in bash:

``` bash
python3 histogram.py [-f][0-9] [file]
```

## Description
Takes data and makes a histogram as a png file. 
expres.anal.csv is the unit test that is used for this program. However, program works with any csv file. 

Program includes a column selector to select a specific column for a histogram. Histogram is saved as "histogram_figure.png" file name.

## Known Issues
The file must be in csv. Currently does not work for a tsv file. 
