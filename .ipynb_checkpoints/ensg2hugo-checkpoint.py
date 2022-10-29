#!/usr/bin/python
import sys
import re
import fileinput

gene_file = open('Homo_sapiens.GRCH37.75.gtf', 'r')

Create_Dictionary={}
for each_line in gene_file:
    ENSL_name = re.findall(r'ENSG\d{11,}' , each_line, re.I) # Regex
    HUGO_name = re.findall(r'gene_name\s(\".*?\")' , each_line, re.I) 
    if ENSL_name:
        if HUGO_name:
            Create_Dictionary[ENSL_name[0]] = HUGO_name[0]
            # print( ENSL_name[0] +" : " + HUGO_name[0] )   

if "-f" in sys.argv[1]:
    n = sys.argv[1]
    column_number= int(n[2])
else: column_number = 1


sample = open('expression_analysis_hugo.csv', 'w')
input_file_to_change = sys.argv[2]
#print(Create_Dictionary)
print(',gene_id,gene_type,logFC,AveExpr', file = sample)
for each_line_of_text in fileinput.input(input_file_to_change):
    splitcolumn_array = re.split(',',each_line_of_text.replace( '"' ,'').replace('\n',''))
    #print(splitcolumn_array[1] in Create_Dictionary)
    if splitcolumn_array[column_number].split('.')[0] in Create_Dictionary:
        splitcolumn_array[column_number] = Create_Dictionary[splitcolumn_array[column_number].split('.')[0]]
        res = str(splitcolumn_array)[1:-1]
        resmod = res.replace("\'", "")
        #print('test')
        print(resmod, file = sample)
sample.close()     
