""" 
    Parses Phenotype Data from SNPMAX and places the data in a format for use 
    in plink/seq.

    Format looks something like the one shown below.


    PATIENT<TAB>PHENO1<TAB>PHENO2<TAB>
    1<TAB>1<TAB>RED
    2<TAB>0<TAB>BLUE

"""

from phenotype import Phenotype
import argparse

sample_list_pheno={}

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_int(s):
    try:
        n = float(s)
        if n % 1 == 0:
            return True
        else:
            return False
    except ValueError:
        return False

def parse_phenotypes(input_phenotypes, output_phenotypes, missing, delim):
    if (missing == ' '):
        # set to something sensible
        missing = '.'
    with open(input_phenotypes) as input_phenotypes_f:
        with open(output_phenotypes,'w') as out:
            header_list = []
            for i, line in enumerate(input_phenotypes_f):
                if (i == 0):
                    header_list = [x.replace('\n','') for x in line.split(delim)]
                    phenotypes = [[] for i in header_list] 
                else:
                    for i, pheno in enumerate(line.split(delim)):
                        pheno = pheno.replace('\n','')
                        if (pheno == ' '): 
                            pheno = missing 
                        phenotypes[i].append(pheno)
            samples = phenotypes[0]
            header_pheno = header_list[1:]
            phenotypes = phenotypes[1:]
            types = [sniff_datatype(item, missing) for item in phenotypes]
            phenotype_obj = []
            for item in enumerate(zip(types,header_list[1:])):
                i = item[0]
                types = item[1][0]
                head = item[1][1]
                phenotype_obj.append(Phenotype(head,str(i),types, missing))
            for i, pheno in enumerate(phenotype_obj):
                for j, ind_p in enumerate(phenotypes[i]): 
                    pheno.add_data(samples[j],ind_p)
            # Print the header
            for w_h in phenotype_obj:
                out.write(w_h.get_header())
            out.write("#ID"+delim+delim.join(header_pheno)+'\n')
            for samp in samples:
                out.write(samp + delim +  delim.join([p.get_data(samp) for p in phenotype_obj]) + '\n')


def subset_file(samples):
    raise NotImplementedError()

def sniff_datatype(data_column, missing):
    nofails = "Integer"
    is_num = [is_number(x) for x in data_column]
    check_int = [is_int(x) for x in data_column]
    # Preserves order of check_int
    data_column = [0 if x == missing else 1 for x in data_column]
    if(sum(is_num) != sum(data_column)):
        return "String"
    if(sum(check_int) != sum(data_column)):
        return "Float"
    return nofails

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
    if(args.samples is not None):
        args.input_phenotypes = subset_file(args.samples)
    parse_phenotypes(args.input_phenotypes, args.output_phenotypes, args.delimiter, args.missing)        


if __name__=="__main__":
    main()
