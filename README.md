# trgn_assignment3
TRGN510 Assignment 3 Fall 2022
<<<<<<< HEAD

# Extract Phone Number Task 
## Usage
Input a txt file with phone numbers and the program will return the phone numbers only (even if formatted differently)
## Description
Input a txt file with phone numbers and the program will return the phone numbers only (even if formatted differently)
=======
# Extract Phone Number Task 
## Usage
## Description
>>>>>>> bb331a376315b2dade4aa9d9918b9e4414d8c096
## Known Issues

Works for regular numbers with 888-888-8888 pattern. Does not work for international numbers. Need to find a regex solution that can search for mulitple patterns. 

Requies a hard-wire. Still setting up solution to run with a txt file input. 
<<<<<<< HEAD

# Ensg2Hugo

## Usage

To convernt ENSG to Hugo, we need a file for data. We can use the following gtf file: Homo_sapiens.GRCh37.75.gtf. Using the following wget command to scrape the file off the internet. Then use the gunzip commmand to unzip the file. 

``` python

wget http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf.gz 
gunzip Homo_sapiens.GRCh37.75.gtf.gz 

```
This must be run on local device since Github can't store this gtf file. Perform command and make sure file is in same dierectory as ensg2hug.py
=======


# ENSG to Hugo Task

## Usage

To convernt ENSG to Hugo, we need a file for data. We can use the following gtf file: Homo_sapiens.GRCh37.75.gtf. Using the following wget command to scrape the file off the internet. Then use the gunzip commmand to unzip the file. 

``` python

wget http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf.gz 
gunzip Homo_sapiens.GRCh37.75.gtf.gz 

```
>>>>>>> bb331a376315b2dade4aa9d9918b9e4414d8c096

``` bash
python3 ensg2hugo.py [-f][0-9] [file]
```
<<<<<<< HEAD
However, this bash command does not work currently. 
=======
>>>>>>> bb331a376315b2dade4aa9d9918b9e4414d8c096

## Description
Function that Converts Ensemble names in a GTF file to HUGO anmes

## Known Issues
<<<<<<< HEAD
Accurate regex commands developed. However, dicts {} is not working. It thinks that input is a list and not an integer data type. Need to find a for loop solution that creates a dictionary. Need to add a searchablility feature into function. 
=======
>>>>>>> bb331a376315b2dade4aa9d9918b9e4414d8c096

# Histogram

## Usage 
<<<<<<< HEAD
Takes csv file and makes a histogram as a png. When asked, insert the column of the CSV that you want to make a histogram. 

Make sure to pull the csv file unit test from Dr. Craig's github. Git clone the repository to get the following csv file: expres.anal.csv  

https://github.com/davcraig75/unit
=======
>>>>>>> bb331a376315b2dade4aa9d9918b9e4414d8c096

## Description
Takes data and makes a histogram as a png file. 

## Known Issues
<<<<<<< HEAD
Column function (which selects the column to use for histogram) is not working properly (Unsure why)
Also need to use TSV instead of Csv file
=======
>>>>>>> bb331a376315b2dade4aa9d9918b9e4414d8c096
