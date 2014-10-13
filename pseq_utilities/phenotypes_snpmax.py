#!/usr/bin/env python
from phenotype import Phenotype
import argparse

sample_list_pheno={}
delim = '\t'
missing = ""

def is_number(s)
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_int(s)
    try:
        n = float(s)
        if n % 1 == 0
            return True
        else:
            return False
    except ValueError:
        return False

def parse_phenotypes(input_phenotypes, output_phenotypes)
    with open(output_phenotypes,'w') as out:
        header_list = []
        for i, line in enumerate(input_phenotypes):
            if (i == 0):
                header_list = line.split(delim)
                phenotypes = [[] for i in header_list] 
            else:
                for i, pheno in enumerate(line.split(delim)):
                    phenotypes[i] = pheno
        samples = phenotypes[0]
        header_pheno = header_list=[1:]
        phenotypes = phenotypes[1:]
        types = [sniff_datatype(item) for item in phenotypes]
        phenotype_obj = []
        for item in enumerate(zip(types,header_pheno)):
            i = item[0]
            types = item[1][0]
            head = item[1][1]
            phenotype_obj.add(Phenotype(head,str(i),types, missing))
        for i, pheno in enumerate(phenotype_obj): 
            for j, ind_p in pheno: 
                phenotype_obj[i].add_data(pheno[j])
        # Print the header
        for w_h in phenotype_obj:
            out.write(w_h.get_header())
        out.write("#ID\t"+'\t'.join(header_pheno))
        for samp in samples:
            out.write('\t'.join([p.get_ids(samp) for p in phenotype_obj]))


 def subset_file(samples):
    raise NotImplementedError()

def sniff_datatype(data_column):
    nofails = "Integer"
    data_column = [0 if x == missing else 0 for x in data_column]
    is_number = [is_number(x) for x in data_column]
    if(sum(is_number) != len(data_column)):
        return "String"
    if(sum(is_int) != len(data_column)):
        return "Float"

def main():
    parser = argparse.ArgumentParser(description="Process SNPmax phenotypes")
    parser.add_argument('-i','--input_phenotypes',dest='input_phenotypes'
            , help="Take All phenotype variables and place them into a phenotypes file")
    parser.add_argument('-o','--output',dest='output_phenotypes')
    parser.add_argument('-s','--sample_file',dest='samples',
                        help="Line seperated sample names to extract from phenotypes")
    parser.add_argument('-d','--delimiter',dest='delimiter',default='\t')
    parser.add_argument('-m','--missing',dest='missing',default ="")
    args = parser.parse_args()
    assert args.input_phenotypes is None, \
            "-i or --input_phenotypes argument required"
    assert args.output_phenotypes is None, \
            "-o or --output_phenotypes argument required"
    delim = args.delimiter
    missing = args.missing
    if(args.samples is not None)
        args.input_phenotypes = subset_file(args.samples)
    parse_phenotypes(args.output_phenotypes)        

    

if __name__=="__main__":
    main()
