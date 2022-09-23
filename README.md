# trgn_assignment3
TRGN510 Assignment 3 Fall 2022

# Extract Phone Number Task 
## Usage
Input a txt file with phone numbers and the program will return the phone numbers only (even if formatted differently)
## Description
Input a txt file with phone numbers and the program will return the phone numbers only (even if formatted differently)
## Known Issues

Works for regular numbers with 888-888-8888 pattern. Does not work for international numbers. 

Found a solution that requires Hard-Wiring. 

Issue: The solution prints the numbers, but the formatting is slightly incorrect. It needs to be fixed. 


# Ensg2Hugo

## Usage

To convernt ENSG to Hugo, we need a file for data. We can use the following gtf file: Homo_sapiens.GRCh37.75.gtf. Using the following wget command to scrape the file off the internet. Then use the gunzip commmand to unzip the file. 

``` python

curl http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf.gz 
gunzip Homo_sapiens.GRCh37.75.gtf.gz 

```

This script works with the following command in bash:

``` bash
python3 ensg2hugo.py [-f][0-9] [file]
```

## Description
Function that Converts Ensemble names in a GTF file to HUGO names for specific columns of a file. 

## Known Issues
Accurate regex commands developed and dictionary is created properly. 
However, program prints output to a created file (need to have a file originally created). For some reason, it removes all values from the file. 

# Histogram

## Usage 
Takes csv file and makes a histogram as a png. When asked, insert the column of the CSV that you want to make a histogram. 

## Description
Takes data and makes a histogram as a png file. 

## Known Issues
Program works to create a histogram. 
Column function works when selecting the columns and saves the specified column to a value. However, program cannot use the specified column and create a histogram (based on values in that specified column) 
