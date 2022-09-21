# trgn_assignment3
TRGN510 Assignment 3 Fall 2022
# Extract Phone Number Task 
## Usage
## Description
## Known Issues

Works for regular numbers with 888-888-8888 pattern. Does not work for international numbers. Need to find a regex solution that can search for mulitple patterns. 

Requies a hard-wire. Still setting up solution to run with a txt file input. 


# ENSG to Hugo Task

## Usage

To convernt ENSG to Hugo, we need a file for data. We can use the following gtf file: Homo_sapiens.GRCh37.75.gtf. Using the following wget command to scrape the file off the internet. Then use the gunzip commmand to unzip the file. 

``` python

wget http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf.gz 
gunzip Homo_sapiens.GRCh37.75.gtf.gz 

```

``` bash
python3 ensg2hugo.py [-f][0-9] [file]
```

## Description
Function that Converts Ensemble names in a GTF file to HUGO anmes

## Known Issues

# Histogram

## Usage 

## Description
Takes data and makes a histogram as a png file. 

## Known Issues
