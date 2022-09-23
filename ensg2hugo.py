#!/usr/bin/python
import sys
import re
import fileinput

gene_file = "Homo_sapiens.GRCH37.75.gtf"
for each_line in gene_file:
    ENSL_name = re.findall(r'ENSG\d{11,}' , each_line) # Regex
    HUGO_name = re.findall(r'gene_name\s(\".*?\")' , each_line) 
    Create_Dictionary={}
    if ENSL_name:
        if HUGO_name:
            Create_Dictionary[ENSL_name[0]] = HUGO_name[0]
            print( ENSL_name[0] +" : " + HUGO_name[0] )   

if sys.argv[:1] == "-f":
    n = str((column_selection[2]))

input_file_to_change=sys.argv[2]
sample = open('test_file.csv', 'w')
splitcolumn_array=[]
for each_line_of_text in fileinput.input(input_file_to_change):
    splitcolumn_array = re.split(',',each_line_of_text)
    print(splitcolumn_array)
    if splitcolumn_array[n] in Create_Dictionary:
        splitcolumn_array.append(Create_Dictionary[splitcolumn_array])
        res = str(splitcolumn_array)[1:1]
        print(res)
        resmod = res.replace("\'", "")
        print(resmod, file = sample)
sample.close()     
