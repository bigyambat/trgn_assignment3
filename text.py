#!/usr/bin/python
import re
file = open("Homo_sapiens.GRCh37.75.gtf")
gene_file = file.read()

f = re.findall(r'ENSG\d{11,}' , gene_file, re.I)
g = re.findall(r'gene_name\ "(.*?)"' , gene_file, re.I) 

dicts = {}
Ensemble_Genes = [f]
Hugo_Genes= [g]
for i in Ensemble_Genes:
    dicts[f] = Hugo_Genes[g]
print(dicts)
               
